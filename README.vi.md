# 🛡️ GRC90 — Hành trình 90 ngày Cybersecurity & GRC

> Lộ trình tự học hướng đến vị trí **Technical GRC Analyst**.  
> Học công khai. Cập nhật hàng tuần.

[🇬🇧 English](./README.md) · 🇻🇳 Tiếng Việt

---

## 👤 Giới thiệu

Repository này ghi lại hành trình 90 ngày học Cybersecurity với định hướng **Technical GRC (Governance, Risk & Compliance)**. Kết hợp kỹ năng kỹ thuật thực chiến với các framework tuân thủ — đây chính xác là sự kết hợp mà nhà tuyển dụng đang tìm kiếm.

**Tại sao Technical GRC?**  
Hầu hết GRC Analyst thiếu chiều sâu kỹ thuật. Hầu hết Security Engineer lại thiếu kiến thức về compliance. Lộ trình này lấp đầy cả hai khoảng trống đó.

---

## 📂 Cấu trúc thư mục

```
GRC90/
├── README.md                         ← Bản tiếng Anh
├── README_VI.md                      ← Bạn đang ở đây (tiếng Việt)
├── ROADMAP.md                        ← Lộ trình đầy đủ 12 tuần + theo dõi tiến độ
│
├── weekly/
│   ├── TEMPLATE.md                   ← Template trống cho mỗi tuần
│   ├── week01-cia-nist.md            ← Checklist theo ngày, ghi chú, output
│   └── week02-networking.md
│   └── ...
│
├── policies/
│   ├── user-account-policy.md        ← Tuần 3 ⭐
│   └── ai-governance-policy.md       ← Tuần 8 ⭐
│
├── checklists/
│   └── cloud-hygiene-checklist.md    ← Tuần 4 ⭐
│
├── playbooks/
│   └── incident-response-playbook.md ← Tuần 6 ⭐
│
├── reports/
│   ├── identity-risk-assessment.md   ← Tuần 10 ⭐
│   └── pentest-report-[machine].md   ← Tuần 11 ⭐
│
├── labs/
│   └── ...                           ← Lab notes, scripts, queries
│
└── notes/
    └── ...                           ← Ghi chú khái niệm, tóm tắt framework
```

---

## 📊 Tiến độ

<!-- PROGRESS_START -->
**Tổng thể: 0 / 12 tuần hoàn thành**

| Giai đoạn | Tiến độ | Tuần |
|---|---|---|
| 🔵 Giai đoạn 1 — Nền tảng | ░░░░░░░░ 0/4 | Tuần 1–4 |
| 🟠 Giai đoạn 2 — Offense & Defense | ░░░░░░░░ 0/4 | Tuần 5–8 |
| 🟢 Giai đoạn 3 — Portfolio & The Hunt | ░░░░░░░░ 0/4 | Tuần 9–12 |

> Tiến độ tự động cập nhật khi hoàn thành checklist hàng tuần.
<!-- PROGRESS_END -->

---

## 🎯 Vị trí mục tiêu

**Technical GRC Analyst** — cầu nối giữa bảo mật thực chiến và framework tuân thủ.

Kỹ năng đang xây dựng: `Cloud Security` · `Vulnerability Management` · `NIST CSF` · `ISO 27001` · `AI Governance` · `Identity Governance` · `Incident Response` · `MITRE ATT&CK`

---

## ⚡ Hướng dẫn sử dụng nhanh

### Lần đầu setup

```bash
# 1. Clone repo về máy
git clone https://github.com/tuonglnc/GRC90.git
cd GRC90

# 2. Bật quyền write cho GitHub Actions
# Settings → Actions → General → Workflow permissions
# → Chọn "Read and write permissions" → Save
```

### Mỗi ngày học

```
1. Mở    weekly/week01-cia-nist.md
2. Học xong task nào → đổi [ ] thành [x]
3. Commit & push lên GitHub
4. GitHub Actions tự chạy (~30 giây)
5. ROADMAP.md + README.md tự cập nhật ✅
```

### Mỗi tuần mới

```
1. Copy   weekly/TEMPLATE.md
2. Đổi tên → weekly/week02-networking.md  (đúng format: weekXX-topic.md)
3. Điền nội dung theo ROADMAP.md
4. Bắt đầu tick từng ngày như bình thường
```

### Trigger Actions thủ công (khi cần)

```
GitHub repo → tab Actions → "Sync Weekly Progress to Roadmap" → Run workflow
```

### Fallback — chạy script thủ công không cần Actions

```bash
python .github/scripts/sync_progress.py
git add ROADMAP.md README.md
git commit -m "manual sync"
git push
```

---

## 📚 Lộ trình đầy đủ

→ Xem [ROADMAP.md](./ROADMAP.md) để biết chi tiết 12 tuần, tài nguyên học tập và deliverables.
