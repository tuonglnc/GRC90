"""
sync_progress.py
----------------
Reads all weekly/weekXX-*.md files, checks if all tasks are completed,
then updates ROADMAP.md and README.md with current progress.

How it works:
1. Scan weekly/ folder for week*.md files
2. For each file: count total [ ] and [x] checkboxes
3. If all tasks are [x] → mark that week as done in ROADMAP.md
4. Update the overall progress summary in ROADMAP.md and README.md
"""

import os
import re
import glob

# ── Config ──────────────────────────────────────────────────────────────────

WEEKLY_DIR = "weekly"
ROADMAP_FILE = "ROADMAP.md"
README_FILE = "README.md"

# Maps week number → (week_tag, phase)
WEEK_CONFIG = {
    1:  ("W01", 1), 2:  ("W02", 1), 3:  ("W03", 1), 4:  ("W04", 1),
    5:  ("W05", 2), 6:  ("W06", 2), 7:  ("W07", 2), 8:  ("W08", 2),
    9:  ("W09", 3), 10: ("W10", 3), 11: ("W11", 3), 12: ("W12", 3),
}

PHASE_NAMES = {
    1: "🔵 Phase 1 — Foundations",
    2: "🟠 Phase 2 — Offense & Defense",
    3: "🟢 Phase 3 — Portfolio & Hunt",
}

# ── Helpers ──────────────────────────────────────────────────────────────────

def count_tasks(filepath: str) -> tuple[int, int]:
    """Returns (completed, total) task counts from a markdown file."""
    completed = 0
    total = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # Match GitHub-flavored markdown checkboxes
            if re.search(r'- \[x\]', line, re.IGNORECASE):
                completed += 1
                total += 1
            elif re.search(r'- \[ \]', line):
                total += 1
    return completed, total


def get_week_file(week_num: int) -> str | None:
    """Find the weekly file for a given week number."""
    pattern = os.path.join(WEEKLY_DIR, f"week{week_num:02d}-*.md")
    files = glob.glob(pattern)
    return files[0] if files else None


def replace_between_tags(content: str, start_tag: str, end_tag: str, new_content: str) -> str:
    """Replace content between HTML comment tags."""
    pattern = rf'{re.escape(start_tag)}.*?{re.escape(end_tag)}'
    replacement = f'{start_tag}\n{new_content}\n{end_tag}'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def progress_bar(done: int, total: int, width: int = 20) -> str:
    """Generate a simple ASCII progress bar."""
    filled = int(width * done / total) if total > 0 else 0
    bar = '█' * filled + '░' * (width - filled)
    return bar


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    # Always run from repo root regardless of where script is invoked from
    # Script lives at .github/scripts/sync_progress.py → go up 3 levels
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.chdir(repo_root)
    print(f"📂 Working directory: {os.getcwd()}")
    print("🔍 Scanning weekly files...")

    # Collect status for each week
    week_status = {}   # week_num → {"done": bool, "completed": int, "total": int}

    for week_num in range(1, 13):
        filepath = get_week_file(week_num)
        if filepath and os.path.exists(filepath):
            completed, total = count_tasks(filepath)
            is_done = (total > 0 and completed >= total)
            week_status[week_num] = {
                "done": is_done,
                "completed": completed,
                "total": total,
                "file": filepath,
            }
            status_str = "✅ DONE" if is_done else f"{completed}/{total}"
            print(f"  Week {week_num:02d}: {status_str} ({filepath})")
        else:
            week_status[week_num] = {
                "done": False, "completed": 0, "total": 0, "file": None
            }
            print(f"  Week {week_num:02d}: (no file yet)")

    # ── Update ROADMAP.md ────────────────────────────────────────────────────

    with open(ROADMAP_FILE, "r", encoding="utf-8") as f:
        roadmap = f.read()

    # Update each week's status tag
    for week_num, info in week_status.items():
        tag, _ = WEEK_CONFIG[week_num]
        start_tag = f"<!-- {tag}_STATUS -->"
        end_tag   = f"<!-- /{tag}_STATUS -->"

        if info["done"]:
            new_status = "✅ Done"
        elif info["completed"] > 0:
            new_status = f"🔄 In progress ({info['completed']}/{info['total']})"
        elif info["file"]:
            new_status = "⬜ Not started"
        else:
            new_status = "⬜ Not started"

        roadmap = roadmap.replace(
            f"{start_tag}",
            f"{start_tag}"
        )
        # Replace between tags
        pattern = rf'{re.escape(start_tag)}.*?{re.escape(end_tag)}'
        replacement = f'{start_tag}{new_status}{end_tag}'
        roadmap = re.sub(pattern, replacement, roadmap, flags=re.DOTALL)

    # Update overall progress block in ROADMAP.md
    total_done = sum(1 for info in week_status.values() if info["done"])
    pct = int(total_done / 12 * 100)

    phase_lines = []
    for phase_num in [1, 2, 3]:
        weeks_in_phase = [w for w, (_, p) in WEEK_CONFIG.items() if p == phase_num]
        done_in_phase = sum(1 for w in weeks_in_phase if week_status[w]["done"])
        bar = progress_bar(done_in_phase, 4, width=4)
        phase_lines.append(f"Phase {phase_num} [{list(PHASE_NAMES.values())[phase_num-1][0]}] {bar} {done_in_phase}/4")

    progress_block = f"**{total_done} / 12 weeks completed ({pct}%)**\n\n```\n" + \
                     "\n".join(phase_lines) + "\n```"

    roadmap = replace_between_tags(
        roadmap,
        "<!-- ROADMAP_PROGRESS_START -->",
        "<!-- ROADMAP_PROGRESS_END -->",
        progress_block
    )

    with open(ROADMAP_FILE, "w", encoding="utf-8") as f:
        f.write(roadmap)

    print(f"\n✅ ROADMAP.md updated — {total_done}/12 weeks done ({pct}%)")

    # ── Update README.md ─────────────────────────────────────────────────────

    with open(README_FILE, "r", encoding="utf-8") as f:
        readme = f.read()

    # Build phase table rows
    phase_rows = []
    for phase_num in [1, 2, 3]:
        weeks_in_phase = [w for w, (_, p) in WEEK_CONFIG.items() if p == phase_num]
        done_in_phase = sum(1 for w in weeks_in_phase if week_status[w]["done"])
        week_range = f"Week {weeks_in_phase[0]}–{weeks_in_phase[-1]}"
        name = PHASE_NAMES[phase_num]
        bar = progress_bar(done_in_phase, 4, width=8)
        phase_rows.append(f"| {name} | {bar} {done_in_phase}/4 | {week_range} |")

    readme_progress = (
        f"**Overall: {total_done} / 12 weeks completed**\n\n"
        f"| Phase | Progress | Weeks |\n"
        f"|---|---|---|\n"
        + "\n".join(phase_rows)
        + "\n\n> Progress updates automatically when weekly checklists are completed."
    )

    readme = replace_between_tags(
        readme,
        "<!-- PROGRESS_START -->",
        "<!-- PROGRESS_END -->",
        readme_progress
    )

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"✅ README.md updated")
    print(f"\n📊 Summary: {total_done}/12 complete | {12 - total_done} remaining")


if __name__ == "__main__":
    main()
