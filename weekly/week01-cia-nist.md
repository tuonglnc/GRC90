# Week 01 — CIA Triad & Risk Mindset (GRC Mindset)

> **Phase 1 · Day 1–7**  
> **Theme:** Technical + GRC  
> **Linked roadmap:** [ROADMAP.md → Week 1](../ROADMAP.md)

---

## 📊 Week Progress

<!-- WEEK_PROGRESS_START -->
**0 / 21 tasks completed**
<!-- WEEK_PROGRESS_END -->

---

## ✅ Daily Checklist

> Tick all tasks in a day before moving to the next.  
> When **all 21 tasks** are checked, GitHub Actions will auto-update ROADMAP.md.

---

### Day 1 — CIA Triad foundations
*~2–3 hours*

- [x] Read and take notes on CIA Triad: Confidentiality, Integrity, Availability — with real-world examples for each
- [x] Learn the 3 core concepts: Threat / Vulnerability / Asset — and how they relate
- [x] Memorize the formula: `Risk = Likelihood × Impact`
- [x] Analyze the Equifax 2017 breach through the CIA lens: which pillar was violated? What was the Threat? The Vulnerability?

**📝 Notes:**
<!-- Write your notes here -->
#### CIA Triad - Definition:
1. Confidentiality (Tính bảo mật): "Ai có quyền mới được xem" - "Tui hong có quyền mà tui vẫn xem được thì seo 👻"
2. Integrity (Tính toàn vẹn): "Nhỏ Data còn **zin** hong bị mất, hong bị thêm, hong bị sửa..." - "Tui sẽ hủy hoại em Data bằng mọi giá 🤡"
3. Availability (Tính khả dụng): "Tui cần bên anh 24/24" - "Tui sẽ ko cho cô gặp anh ta 😈"

#### CIA Triad - Case Study:
1. Confidentiality: [Equifax (2017)](../notes/equifax.md)
2. Integrity: [SolarWinds Orion (2020)](../notes/solarwinds.md)
3. Availability: [WannaCry (2017)](../notes/wannacry.md)

#### Threat / Vulnerability / Asset
1. Asset: Là bất cứ thứ gì có giá trị đối với tổ chức hoặc cá nhân mà bạn cần bảo vệ.
2. Vulnerability: Là điểm yếu tồn tại trong hệ thống, quy trình, hoặc con người mà kẻ xấu có thể lợi dụng để xâm nhập hoặc gây hại.
3. Threat: Là bất kỳ tác nhân hoặc sự kiện nào có khả năng khai thác lỗ hổng để gây thiệt hại cho tài sản. Mối đe dọa cần có một tác nhân (Threat Actor) hoặc một nguồn (Threat Source).

   Mối quan hệ: $$\text{Threat} \times \text{Vulnerability} \times \text{Asset Value} = \text{Risk}$$

> Trong một tòa lâu đài kiên cố giữ một chiếc rương báu cổ giá trị (Asset), gã tướng cướp khét tiếng đang rình rập bên ngoài với âm mưu đột nhập chiếm đoạt tài sản (Threat); gã liên tục lượn lờ quanh các bức tường thành cho đến khi phát hiện ra một mật đạo ngầm bị bỏ quên không khóa (Vulnerability), và chính sự giao thoa tại thời điểm gã bước qua cánh cửa hớ hênh đó đã biến nguy cơ tiềm ẩn thành một hiểm họa mất mát nhãn tiền (Risk).

#### `Risk = Likelihood × Impact`

Để hiểu cách Likelihood (Khả năng xảy ra) và Impact (Mức độ ảnh hưởng) định hình nên nàng Risk, hãy nhìn vào bản chất của từng vế:

- **Likelihood (Khả năng xảy ra):** Xác suất mà một mối đe dọa (Threat) sẽ tìm thấy và khai thác thành công một lỗ hổng (Vulnerability).
  - Yếu tố quyết định: Mật đạo đó dễ tìm không? Gã tướng cướp có công cụ mạnh không? Tần suất kẻ trộm đi qua vùng này có cao không?

- **Impact (Mức độ ảnh hưởng / Hậu quả):** Mức độ thiệt hại đối với tài sản (Asset) nếu lỗ hổng bị khai thác thành công.
  - Yếu tố quyết định: Nếu mất rương báu, lâu đài có bị phá sản không? Danh tiếng của nhà vua có bị hủy hoại không? Chi phí phục hồi là bao nhiêu?

Trong thực tế, người ta thường dùng một ma trận (thường là $3 \times 3$ hoặc $5 \times 5$) để trực quan hóa công thức này. Khi bạn nhân hai giá trị này với nhau, bạn sẽ ra được mức độ nghiêm trọng của Rủi ro (Thấp, Trung bình, Cao, Nghiêm trọng).

**📊 Risk Matrix (3×3)**

| Khả năng xảy ra (Likelihood) ↓ / Ảnh hưởng (Impact) → | Thấp (Low) | Vừa (Medium) | Cao (High) |
|---|---|---|---|
| **Cao (High)** | Trung bình | Cao | 🔥 Nghiêm trọng |
| **Vừa (Medium)** | Thấp | Trung bình | Cao |
| **Thấp (Low)** | Thấp | Thấp | Trung bình |

> Nhà vua không thể dời chiếc rương báu (Impact rất lớn) đi nơi khác, nhưng ngài lập tức ra lệnh cho lính canh trám xi măng và khóa chặt mật đạo lại. Bằng cách triệt hạ lỗ hổng, nhà vua đã kéo xác suất gã trộm đột nhập thành công xuống gần bằng 0 (Likelihood tối thiểu). Khi Likelihood sụp đổ, mức độ Risk chung của cả lâu đài tự động biến mất, dù gã tướng cướp ngoài kia có hung hãn đến thế nào đi nữa.

️🎯Mục tiêu cốt lõi của việc quản trị rủi ro chính là tìm ra những chỗ có sự giao thoa giữa Likelihood cao và Impact lớn để dồn nguồn lực vào xử lý trước.
---

### Day 2 — SolarWinds case study
*~2–3 hours*

- [ ] Read a summary of the SolarWinds 2020 attack — the most significant supply chain breach in history
- [ ] Fill in the analysis table: which CIA pillar(s) were violated? Who was the Threat Actor? Where was the Vulnerability?
- [ ] Compare SolarWinds vs Equifax: same attack type or different? What lessons apply to any organization?

**📝 Notes:**
<!-- Write your notes here -->

**🔗 Resources:**
- [CISA Emergency Directive on SolarWinds](https://www.cisa.gov/news-events/news/emergency-directive-21-01)
- [Wikipedia: SolarWinds attack 2020](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach)

---

### Day 3 — NIST CSF 2.0 deep read
*~3 hours*

- [ ] Open NIST CSF 2.0 PDF — read Preface and Section 1 (Overview): understand the purpose, who uses it, and why
- [ ] Read Section 2 (CSF Core): understand all 6 Functions — **GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER** — note that GOVERN is new in v2.0
- [ ] Read Section 3 (Profiles & Tiers): understand Current Profile vs Target Profile, and the 4 Tiers (Partial → Adaptive)
- [ ] Summarize all 6 Functions in your own words (e.g. "GOVERN = who is accountable for cybersecurity in the org")

**📝 Notes:**
<!-- Write your notes here -->

**🔗 Resources:**
- [NIST CSF 2.0 — Official PDF](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- [nist.gov/cyberframework — Quick Start Guides](https://www.nist.gov/cyberframework)

---

### Day 4 — Map real breach to NIST CSF
*~2–3 hours*

- [ ] Take the Equifax breach and map it to NIST CSF: which Functions did they FAIL at? *(hint: IDENTIFY — didn't know about the vulnerability; DETECT — too slow to detect)*
- [ ] Write ~150 words: "If Equifax had properly applied NIST CSF, what should they have done differently at each Function?"
- [ ] Start TryHackMe Pre-Security path — complete the first module (What is Networking)

**📝 Notes:**
<!-- Write your notes here -->

> 💡 **GRC Insight:** This exercise — mapping a real breach to a framework — is exactly what GRC Analysts do daily. Save this note for your portfolio.

---

### Day 5 — Risk Assessment basics
*~2 hours*

- [ ] Learn how to use a 5×5 Risk Matrix: X-axis = Likelihood (1–5), Y-axis = Impact (1–5), red zones = immediate action required
- [ ] Create a simple Risk Register in Excel: list 5 security risks, score Likelihood and Impact, calculate Risk Score
- [ ] Continue TryHackMe Pre-Security — complete 1–2 more modules

**📝 Notes:**
<!-- Write your notes here -->

> 💡 **GRC Insight:** A Risk Register is the most fundamental GRC document. Keep this file — it goes into your portfolio later.

---

### Day 6 — Business Impact Analysis
*~2 hours*

- [ ] Learn Business Impact Analysis (BIA): when a system is compromised, what are the financial, legal, and reputational impacts?
- [ ] Learn two key metrics: **RTO** (Recovery Time Objective) and **RPO** (Recovery Point Objective) — understand how they differ
- [ ] Apply to Equifax: what was their actual business impact? ($575M fine, class action lawsuits, reputation damage...)

**📝 Notes:**
<!-- Write your notes here -->

> 💡 **Forward link:** RTO and RPO will appear again in Week 6 when you build the IR Plan. Understanding them early gives you a big advantage.

---

### Day 7 — Week review & GitHub setup
*~2–3 hours*

- [ ] Create GitHub repo `cybersec-grc-journey` (or use this repo)
- [ ] Upload your Risk Register and CIA/NIST analysis notes as the first commit
- [ ] Self-check: answer the 5 questions below **without looking at your notes**

**📝 Reflection:**
<!-- What was the most surprising thing you learned this week? -->

---

## 🧠 End-of-Week Self-Check

> Answer all 5 without notes = ready for Week 2 ✅

1. What is the CIA Triad? Give a real-world example for each pillar.
2. What is Risk? Explain it in language a CEO would understand.
3. How many Functions does NIST CSF 2.0 have? Name and briefly describe each.
4. Which Function is **new** in CSF 2.0 compared to v1.1?
5. Which CIA pillar(s) did the Equifax breach violate?

**My answers:**
<!-- Write your answers here — good practice for interviews -->

---

## 📦 Week 1 Deliverables

- [ ] `labs/week01-risk-register.xlsx` — Risk Register with 5 risks scored
- [ ] `notes/cia-triad-analysis.md` — CIA analysis of Equifax + SolarWinds
- [ ] `notes/nist-csf-summary.md` — Personal summary of NIST CSF 2.0 Functions
- [X] GitHub repo initialized with first commit

---

## ➡️ Up Next

**Week 2 — Networking & Network Segmentation** → [`week02-networking.md`](./week02-networking.md)

*Topics: OSI 7 layers · TCP/IP · Wireshark · VLAN · DMZ · PCI DSS network requirements*
