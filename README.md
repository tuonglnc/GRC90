# 🛡️ GRC90 — 90-Day Cybersecurity & GRC Journey

> A self-paced learning roadmap targeting a **Technical GRC Analyst** role.  
> Built in public. Updated weekly.

🇬🇧 English · [🇻🇳 Tiếng Việt](./README.vi.md)

---

## 👤 About This Repo

This repository documents my 90-day journey into Cybersecurity with a focus on **Technical GRC (Governance, Risk & Compliance)**. It combines hands-on technical skills with compliance frameworks — the combination most employers are looking for.

**Why Technical GRC?**  
Most GRC analysts lack technical depth. Most security engineers lack compliance knowledge. This roadmap bridges both.

---

## 📂 Structure

```
GRC90/
├── README.md                         ← You are here (intro, English)
├── README_VI.md                      ← Vietnamese version
├── ROADMAP.md                        ← Full 12-week plan with progress tracking
│
├── weekly/
│   ├── TEMPLATE.md                   ← Blank template for each week
│   ├── week01-cia-nist.md            ← Daily checklist, notes, output
│   └── week02-networking.md
│   └── ...
│
├── policies/
│   ├── user-account-policy.md        ← Week 3 ⭐
│   └── ai-governance-policy.md       ← Week 8 ⭐
│
├── checklists/
│   └── cloud-hygiene-checklist.md    ← Week 4 ⭐
│
├── playbooks/
│   └── incident-response-playbook.md ← Week 6 ⭐
│
├── reports/
│   ├── identity-risk-assessment.md   ← Week 10 ⭐
│   └── pentest-report-[machine].md   ← Week 11 ⭐
│
├── labs/
│   └── ...                           ← Raw lab notes, scripts, queries
│
└── notes/
    └── ...                           ← Concept notes, framework summaries
```

---

## 📊 Progress

<!-- PROGRESS_START -->
**Overall: 0 / 12 weeks completed**

| Phase | Progress | Weeks |
|---|---|---|
| 🔵 Phase 1 — Foundations | ░░░░░░░░ 0/4 | Week 1–4 |
| 🟠 Phase 2 — Offense & Defense | ░░░░░░░░ 0/4 | Week 5–8 |
| 🟢 Phase 3 — Portfolio & Hunt | ░░░░░░░░ 0/4 | Week 9–12 |

> Progress updates automatically when weekly checklists are completed.
<!-- PROGRESS_END -->

---

## 🎯 Target Role

**Technical GRC Analyst** — bridging hands-on security and compliance frameworks.

Key skills being built: `Cloud Security` · `Vulnerability Management` · `NIST CSF` · `ISO 27001` · `AI Governance` · `Identity Governance` · `Incident Response` · `MITRE ATT&CK`

---

## ⚡ Quick Start

### First-time setup

```bash
# 1. Clone the repo
git clone https://github.com/tuonglnc/GRC90.git
cd GRC90

# 2. Enable write permissions for GitHub Actions
# Settings → Actions → General → Workflow permissions
# → Select "Read and write permissions" → Save
```

### Every study day

```
1. Open   weekly/week01-cia-nist.md
2. Finish a task → change [ ] to [x]
3. Commit & push to GitHub
4. GitHub Actions runs automatically (~30 seconds)
5. ROADMAP.md + README.md update themselves ✅
```

### Every new week

```
1. Copy   weekly/TEMPLATE.md
2. Rename → weekly/week02-networking.md  (follow format: weekXX-topic.md)
3. Fill in content based on ROADMAP.md
4. Start ticking daily tasks as usual
```

### Trigger Actions manually (if needed)

```
GitHub repo → Actions tab → "Sync Weekly Progress to Roadmap" → Run workflow
```

### Fallback — run sync script locally without Actions

```bash
python .github/scripts/sync_progress.py
git add ROADMAP.md README.md
git commit -m "manual sync"
git push
```

---

## 📚 Full Roadmap

→ See [ROADMAP.md](./ROADMAP.md) for the complete 12-week plan, resources, and deliverables.
