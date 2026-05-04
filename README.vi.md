# 🛡️ Lộ trình 90 ngày — Cybersecurity & GRC

> **Mục tiêu:** Xây dựng nền tảng Cybersecurity vững chắc, định hướng **Technical GRC Analyst**  
> **Thời gian:** 90 ngày · 12 tuần · 3 giai đoạn  
> **Cập nhật lần cuối:** 2026

---

## 📌 Tổng quan

| | Giai đoạn | Thời gian | Mục tiêu |
|---|---|---|---|
| 🔵 | Nền tảng hệ thống & Định danh | Ngày 1–30 | Hiểu "tài sản" cần bảo vệ, thiết lập cơ chế kiểm soát đầu tiên |
| 🟠 | Offense, Defense & Quản trị AI | Ngày 31–60 | Hiểu cách hacker phá vỡ chính sách để xây rào cản tuân thủ tốt hơn |
| 🟢 | Kho vũ khí, Hồ sơ & The Hunt | Ngày 61–90 | Đóng gói kỹ năng thành bằng chứng thực tế để nhà tuyển dụng không thể từ chối |

---

## 📁 Cấu trúc Repository

```
grc90/
│
├── README.md                          ← File này
│
├── policies/
│   ├── user-account-policy.md         ← Tuần 3 ⭐
│   └── ai-governance-policy.md        ← Tuần 8 ⭐
│
├── checklists/
│   └── cloud-hygiene-checklist.md     ← Tuần 4 ⭐
│
├── playbooks/
│   └── incident-response-playbook.md  ← Tuần 6 ⭐
│
├── reports/
│   ├── identity-risk-assessment.md    ← Tuần 10 ⭐
│   └── pentest-report-[machine].md    ← Tuần 11 ⭐
│
├── labs/
│   ├── week1-risk-register.xlsx
│   ├── week2-wireshark-notes.md
│   ├── week7-kql-queries.md
│   └── week9-cis-audit-report.md
│
├── weekly/
│   ├── week01-cia-nist.md             ← Ngày 1–7
│   ├── week02-networking.md           ← Ngày 8–14
│   ├── week03-linux-access.md         ← Ngày 15–21
│   ├── week04-cloud-lab.md            ← Ngày 22–30
│   ├── week05-owasp-vuln.md           ← Ngày 31–37
│   ├── week06-killchain-ir.md         ← Ngày 38–44
│   ├── week07-blueteam-audit.md       ← Ngày 45–51
│   ├── week08-ai-security.md          ← Ngày 52–60
│   ├── week09-scanning-compliance.md  ← Ngày 61–67
│   ├── week10-ad-identity.md          ← Ngày 68–74
│   ├── week11-ctf-report.md           ← Ngày 75–81
│   └── week12-portfolio-hunt.md       ← Ngày 82–90
│
└── notes/
    ├── cia-triad-analysis.md
    ├── nist-csf-summary.md
    └── mitre-attack-mapping.md
```

---

## 🎯 Định vị bản thân — Technical GRC

### Elevator Pitch

> *"I'm a cybersecurity professional specializing in Technical GRC — bridging the gap between hands-on security (cloud security, vulnerability management, identity governance) and compliance frameworks like NIST CSF and ISO 27001. I also focus on AI governance, helping organizations build guardrails for responsible AI adoption."*

### Điểm khác biệt

| Kỹ năng | GRC Analyst thông thường | Technical GRC (bạn) |
|---|---|---|
| Framework | ✅ Biết NIST, ISO 27001 | ✅ Biết + áp dụng được vào hệ thống thực |
| Cloud | ❌ Lý thuyết | ✅ Đã lab AWS, biết misconfiguration |
| Pentest | ❌ Không có | ✅ Hiểu attack để viết control tốt hơn |
| AI Governance | ❌ Rất ít người có | ✅ Có policy template thực tế |
| Evidence | CV chỉ có chữ | ✅ GitHub portfolio có thể xem được |

---

## 📚 Tài nguyên tổng hợp

### Frameworks & Standards

- [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [EU AI Act](https://artificialintelligenceact.eu/the-act/)

### Platforms thực hành

- [TryHackMe](https://tryhackme.com/) — bắt đầu từ đây
- [HackTheBox](https://www.hackthebox.com/) — sau khi có nền tảng
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — web security
- [Gandalf by Lakera](https://gandalf.lakera.ai/) — AI security

### Tools

- [Wireshark](https://www.wireshark.org/) · [Nmap](https://nmap.org/) · [Burp Suite](https://portswigger.net/burp) · [BloodHound](https://github.com/SpecterOps/BloodHound) · [Prowler](https://github.com/prowler-cloud/prowler)

---

## 📊 Progress Tracker

> Cập nhật thủ công — thay `[ ]` thành `[x]` khi hoàn thành

### Giai đoạn 1

- [ ] Tuần 1 — CIA Triad & Tư duy rủi ro
- [ ] Tuần 2 — Networking & Network Segmentation
- [ ] Tuần 3 — Linux & Kiểm soát truy cập
- [ ] Tuần 4 — Cloud Lab & Cloud Security Posture

### Giai đoạn 2

- [ ] Tuần 5 — OWASP Top 10 & Vulnerability Management
- [ ] Tuần 6 — Kill Chain & Incident Response Plan
- [ ] Tuần 7 — Blue Team & Continuous Auditing
- [ ] Tuần 8 — AI Security & AI Governance

### Giai đoạn 3

- [ ] Tuần 9 — Công cụ quét & Compliance Automation
- [ ] Tuần 10 — Active Directory & Identity Risk
- [ ] Tuần 11 — CTFs & Pentest Report Writing
- [ ] Tuần 12 — Portfolio & Định vị Technical GRC

---

## 🔵 GIAI ĐOẠN 1: Nền tảng hệ thống & Định danh (Ngày 1–30)

### Tuần 1 — CIA Triad & Tư duy rủi ro (GRC Mindset)

**Ngày 1–7 · Kỹ thuật + GRC**

#### Nội dung học

- Phân tích 2–3 vụ hack lớn (SolarWinds, Equifax) qua lăng kính CIA Triad
- Học định nghĩa `Risk = Likelihood × Impact`, phân biệt Threat / Vulnerability / Asset
- Đọc tổng quan NIST CSF 2.0 — nắm 6 Functions: **GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER**
- Đọc Section 3: hiểu Current Profile vs Target Profile, 4 cấp độ Tier (Partial → Adaptive)
- Học Business Impact Analysis (BIA), RTO và RPO

#### Checklist theo ngày

| Ngày | Nhiệm vụ |
|---|---|
| Ngày 1 | Đọc CIA Triad, học Risk = Likelihood × Impact, phân tích vụ Equifax qua CIA |
| Ngày 2 | Phân tích vụ SolarWinds 2020 qua CIA, so sánh với Equifax |
| Ngày 3 | Đọc NIST CSF 2.0 PDF — Section 1, 2, 3. Tóm tắt 6 Functions bằng ngôn ngữ cá nhân |
| Ngày 4 | Map vụ Equifax vào NIST CSF — họ FAIL ở Function nào? Bắt đầu TryHackMe Pre-Security |
| Ngày 5 | Tạo Risk Matrix 5×5, làm Risk Register đơn giản trong Excel (5 rủi ro bảo mật) |
| Ngày 6 | Học BIA, RTO, RPO — áp dụng vào vụ Equifax (phạt 575 triệu USD, mất uy tín…) |
| Ngày 7 | Tổng kết, tạo GitHub repo `cybersec-grc-journey`, upload Risk Register + ghi chú |

#### Output tuần 1

- [ ] GitHub repo đã tạo
- [ ] File Risk Register Excel (5 rủi ro, có Likelihood + Impact + Risk Score)
- [ ] Ghi chú phân tích 2 vụ hack qua CIA & NIST CSF

#### Tài nguyên

- 📄 [NIST CSF 2.0 — PDF chính thức](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- 🌐 [nist.gov/cyberframework — Quick Start Guides](https://www.nist.gov/cyberframework)
- 🎓 [TryHackMe — Pre-Security Path](https://tryhackme.com/path/outline/presecurity)
- 📖 [Wikipedia: Equifax data breach 2017](https://en.wikipedia.org/wiki/2017_Equifax_data_breach)
- 📖 [CISA: SolarWinds Emergency Directive](https://www.cisa.gov/news-events/news/emergency-directive-21-01)

#### Tự kiểm tra cuối tuần

> Trả lời được hết = sẵn sàng sang tuần 2 ✅

1. CIA Triad là gì? Cho ví dụ thực tế cho mỗi loại.
2. Risk = ? Giải thích bằng ngôn ngữ cho CEO hiểu.
3. NIST CSF 2.0 có mấy Functions? Kể tên và mô tả ngắn.
4. Function nào là **mới nhất** trong CSF 2.0?
5. Equifax bị tấn công vi phạm CIA nào?

---

### Tuần 2 — Networking qua lăng kính Kiểm soát (Control)

**Ngày 8–14 · Kỹ thuật + GRC**

#### Nội dung học

- Làm chủ OSI 7 lớp, TCP/IP, IP addressing, Ports & Protocols phổ biến (80, 443, 22, 3389)
- Thực hành Wireshark: capture và phân tích gói tin cơ bản
- Hiểu Network Segmentation, VLAN, DMZ — đọc yêu cầu PCI DSS về phân vùng mạng
- Bổ sung GRC: hiểu tại sao Network Segmentation là kiểm soát bắt buộc trong PCI DSS

#### Output tuần 2

- [ ] Lab notes Wireshark (capture ít nhất 1 session HTTP/HTTPS)
- [ ] Sơ đồ mạng đơn giản có phân vùng: Internet → DMZ → Internal Network

#### Tài nguyên

- 🎓 [TryHackMe Pre-Security — Phần Networking](https://tryhackme.com/path/outline/presecurity)
- 🎥 [Professor Messer Network+ (YouTube, miễn phí)](https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/)
- 🛠️ [Wireshark — tải về](https://www.wireshark.org/download.html)

---

### Tuần 3 — Linux & Kiểm soát truy cập (Access Control)

**Ngày 15–21 · Kỹ thuật + GRC**

#### Nội dung học

- Thành thạo terminal cơ bản: navigation, file permissions (`chmod`/`chown`), user management
- Thực hành Privilege Escalation cơ bản trên TryHackMe
- Áp dụng nguyên tắc **Least Privilege** (đặc quyền tối thiểu)
- Viết Policy quản lý tài khoản người dùng (1 trang)

#### Output tuần 3 ⭐

- [ ] `📄 policies/user-account-policy.md` — chính sách quản lý tài khoản người dùng

#### Tài nguyên

- 🎓 [TryHackMe — Linux Privilege Escalation](https://tryhackme.com/room/linprivesc)

---

### Tuần 4 — Cloud Lab & Cloud Security Posture

**Ngày 22–30 · Lab + GRC**

#### Nội dung học

- Dựng AWS Free Tier lab: tạo IAM roles, S3 bucket, EC2 instance
- Bật CloudTrail logging, kết nối Wazuh SIEM (hoặc AWS Security Hub)
- Thực hành Misconfiguration Assessment: kiểm tra bucket public, security group mở quá rộng
- Đọc CIS Benchmark AWS cơ bản — hiểu "benchmark" là gì trong GRC

#### Output tuần 4 ⭐

- [ ] `📄 checklists/cloud-hygiene-checklist.md` — Cloud Hygiene Checklist theo CIS

#### Tài nguyên

- 🌐 [AWS Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- 🛠️ [CloudGoat — Rhino Security Labs (AWS lab dễ bị tấn công)](https://github.com/RhinoSecurityLabs/cloudgoat)
- 🌐 [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

### 🏆 Mốc Giai đoạn 1

> GitHub có **2 tài liệu GRC đầu tiên**: User Account Policy + Cloud Hygiene Checklist

---

## 🟠 GIAI ĐOẠN 2: Offense, Defense & Quản trị AI (Ngày 31–60)

### Tuần 5 — OWASP Top 10 & Vulnerability Management

**Ngày 31–37 · Kỹ thuật + GRC**

#### Nội dung học

- Thực hành SQL Injection, XSS, IDOR trên DVWA hoặc PortSwigger Web Security Academy
- Học CVSS scoring: phân biệt Critical (9.0+), High (7.0–8.9), Medium (4.0–6.9), Low (0.1–3.9)
- Xây dựng SLA Vulnerability Management:
  - 🔴 Critical = fix trong 24 giờ
  - 🟠 High = fix trong 7 ngày
  - 🟡 Medium = fix trong 30 ngày
  - 🟢 Low = fix trong 90 ngày
- Phân loại lỗ hổng theo business impact (không chỉ theo điểm CVSS)

#### Output tuần 5

- [ ] Vuln SLA framework document
- [ ] Ghi chú thực hành SQLi và XSS trên PortSwigger

#### Tài nguyên

- 🎓 [PortSwigger Web Security Academy (miễn phí)](https://portswigger.net/web-security)
- 📖 [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- 🌐 [NVD — CVSS Calculator](https://nvd.nist.gov/vuln-metrics/cvss)

---

### Tuần 6 — Cyber Kill Chain & Incident Response Plan

**Ngày 38–44 · Kỹ thuật + GRC**

#### Nội dung học

- Thực hành full Kill Chain: Recon → Weaponization → Delivery → Exploitation → Reverse Shell
- Học MITRE ATT&CK framework: mapping kỹ thuật tấn công vào tactics
- Xây dựng Incident Response Playbook 6 bước:
  1. **Preparation** — chuẩn bị trước khi xảy ra
  2. **Detection & Analysis** — phát hiện và phân tích
  3. **Containment** — ngăn chặn lan rộng
  4. **Eradication** — loại bỏ nguyên nhân gốc
  5. **Recovery** — khôi phục hệ thống
  6. **Lessons Learned** — rút kinh nghiệm
- Bổ sung: quy trình thông báo sự cố (GDPR 72h, NIS2) và escalation matrix

#### Output tuần 6 ⭐

- [ ] `📄 playbooks/incident-response-playbook.md` — IR Playbook hoàn chỉnh

#### Tài nguyên

- 🌐 [MITRE ATT&CK Framework](https://attack.mitre.org/)
- 🎓 [TryHackMe — Jr Penetration Tester Path](https://tryhackme.com/path/outline/jrpenetrationtester)

---

### Tuần 7 — Blue Team & Continuous Auditing

**Ngày 45–51 · Kỹ thuật + Lab**

#### Nội dung học

- Viết truy vấn KQL (Microsoft Sentinel) và SPL (Splunk) để phát hiện anomaly trong log
- Thực hành threat hunting: tìm dấu hiệu Lateral Movement, Privilege Escalation trong event log
- Coi log analysis là hoạt động **Continuous Auditing**: map findings vào control violations
- Dùng AI (Claude/ChatGPT) để tóm tắt policy violation từ raw log data

#### Output tuần 7

- [ ] Thư viện KQL/SPL queries cơ bản (lưu vào repo)

#### Tài nguyên

- 🎓 [Microsoft Learn — KQL (miễn phí)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)
- 🎓 [TryHackMe — SOC Level 1 Path](https://tryhackme.com/path/outline/soclevel1)

---

### Tuần 8 — AI Security & AI Governance

**Ngày 52–60 · Kỹ thuật + GRC**

#### Nội dung học

- Thực hành Prompt Injection trên Gandalf (lakera.ai) và OWASP Top 10 for LLMs
- Nghiên cứu EU AI Act: phân loại rủi ro AI 4 cấp:
  - 🚫 **Unacceptable Risk** — bị cấm hoàn toàn
  - 🔴 **High Risk** — yêu cầu giám sát nghiêm ngặt
  - 🟡 **Limited Risk** — yêu cầu minh bạch
  - 🟢 **Minimal Risk** — không có yêu cầu đặc biệt
- Xây dựng AI Usage Policy cho doanh nghiệp: data classification, approved tools, guardrails

#### Output tuần 8 ⭐

- [ ] `📄 policies/ai-governance-policy.md` — AI Governance Policy template

> 💡 **Ghi chú:** Đây là điểm khác biệt lớn trên thị trường — rất ít GRC Analyst có nền tảng AI Security

#### Tài nguyên

- 🎮 [Gandalf — Lakera AI (Prompt Injection game)](https://gandalf.lakera.ai/)
- 📖 [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- 🌐 [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf)
- 📖 [EU AI Act — Tóm tắt](https://artificialintelligenceact.eu/the-act/)

### 🏆 Mốc Giai đoạn 2

> GitHub có **IR Playbook + AI Policy**. Đã map được ít nhất 1 attack vào MITRE ATT&CK.

---

## 🟢 GIAI ĐOẠN 3: Kho vũ khí, Hồ sơ & The Hunt (Ngày 61–90)

### Tuần 9 — Công cụ quét & Compliance Automation

**Ngày 61–67 · Lab + GRC**

#### Nội dung học

- Thực hành Nmap (port scanning), Nikto (web scanner), Burp Suite Community (manual testing)
- Dùng Scout Suite hoặc Prowler để audit AWS theo CIS Benchmarks tự động
- So sánh kết quả quét với CIS Benchmarks — document findings dạng compliance report
- Hiểu sự khác biệt: vulnerability scan vs compliance scan

#### Output tuần 9

- [ ] CIS Benchmark audit report (AWS)

#### Tài nguyên

- 🛠️ [Kali Linux — tải về](https://www.kali.org/get-kali/)
- 🎓 [HackTheBox Starting Point](https://app.hackthebox.com/starting-point)
- 🌐 [CIS Benchmarks (cisecurity.org)](https://www.cisecurity.org/cis-benchmarks)
- 🛠️ [Prowler — AWS Security Tool](https://github.com/prowler-cloud/prowler)

---

### Tuần 10 — Active Directory & Identity Risk

**Ngày 68–74 · Kỹ thuật + GRC**

#### Nội dung học

- Dựng Active Directory lab (Windows Server trên VirtualBox)
- Dùng BloodHound để vẽ bản đồ tấn công — "Attack Paths to Domain Admin"
- Mỗi attack path = 1 control gap cần remediate
- Liên kết với Identity Governance: PAM, JIT Access, Tiered Admin Model
- Đề xuất kiểm soát kỹ thuật để chặn từng attack path

#### Output tuần 10 ⭐

- [ ] `📄 reports/identity-risk-assessment.md` — Identity Risk Assessment với đề xuất kiểm soát

#### Tài nguyên

- 🎓 [TryHackMe — Active Directory Basics](https://tryhackme.com/room/winadbasics)
- 🛠️ [BloodHound Community Edition](https://github.com/SpecterOps/BloodHound)

---

### Tuần 11 — CTFs & Pentest Report Writing

**Ngày 75–81 · Kỹ thuật + Output**

#### Nội dung học

- Giải 2–3 machine trên TryHackMe (Easy/Medium) hoặc HackTheBox Starting Point
- Với mỗi machine: viết báo cáo pentest đầy đủ **thay vì chỉ lấy flag**
- Cấu trúc báo cáo pentest chuyên nghiệp:

```
1. Executive Summary      — tóm tắt cho lãnh đạo (không technical)
2. Scope & Methodology    — phạm vi và phương pháp kiểm thử
3. Findings               — danh sách lỗ hổng, mỗi lỗi có:
   - Mô tả
   - Điểm CVSS
   - Evidence (screenshot/payload)
   - Remediation (cách khắc phục)
4. Risk Rating Summary    — bảng tổng hợp Critical/High/Medium/Low
5. Conclusion             — kết luận và khuyến nghị
```

#### Output tuần 11 ⭐

- [ ] `📄 reports/pentest-report-[machine-name].md` — Báo cáo pentest hoàn chỉnh

#### Tài nguyên

- 🎓 [TryHackMe](https://tryhackme.com/)
- 🎓 [HackTheBox Starting Point](https://app.hackthebox.com/starting-point)

---

### Tuần 12 — Portfolio & Định vị "Technical GRC"

**Ngày 82–90 · Output + Career**

#### Nội dung học

- Tổng hợp GitHub portfolio: code labs + policy templates + risk reports + pentest report + AI governance
- Tối ưu LinkedIn với keywords đúng target
- Viết 1–2 bài LinkedIn post về hành trình học (tăng visibility với recruiter)
- Cân nhắc chứng chỉ tiếp theo
- Bắt đầu apply

#### LinkedIn Keywords

```
Cloud Compliance · AI Risk Assessment · Identity Governance
Vulnerability Management · NIST CSF · ISO 27001 · PCI DSS
GRC Analyst · Security Analyst · Cloud Security · MITRE ATT&CK
SIEM · KQL · Threat Modeling · CSPM
```

#### Chứng chỉ đề xuất (sau 90 ngày)

| Chứng chỉ | Phù hợp | Ghi chú |
|---|---|---|
| **CompTIA Security+** | ⭐⭐⭐⭐⭐ | Chuẩn nhất cho entry-level, được công nhận rộng rãi |
| **ISC² CC** | ⭐⭐⭐⭐ | Miễn phí, GRC-friendly, tốt cho người mới |
| **AWS Security Specialty** | ⭐⭐⭐ | Sau khi có Security+ |

#### Output tuần 12 ⭐

- [ ] GitHub portfolio hoàn chỉnh với README đẹp
- [ ] LinkedIn profile tối ưu với keywords
- [ ] Đã apply ít nhất 5 vị trí: GRC Analyst / Compliance Analyst / Security Analyst (Junior)

### 🏆 Mốc Giai đoạn 3

> Portfolio đầy đủ trên GitHub. LinkedIn tối ưu. Sẵn sàng apply vị trí GRC/Security Analyst.

---

*Lộ trình được xây dựng cho hành trình học cá nhân. Cập nhật và điều chỉnh khi cần thiết.*

---
Hi vọng mọi kiến thức sẽ được bạn học tiếp nhận một cách đơn giản và vui vẻ. Rất mong nhận được sự thảo luận của bạn học khi có thắc mắc hoặc có vấn đề cần chỉnh sửa qua brandya337@gmail.com ^^ Cảm ơn vì đã ghé thăm, see ya~~~

🚀 **You are what you do!**
