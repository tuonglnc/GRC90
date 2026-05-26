# SolarWinds (2020) - CVE-2020-10148

- **SolarWinds (2020)** là 1 *Supply chain attack* - tấn công gián tiếp vào bên thứ 3 cung cấp dịch vụ có quyền truy cập vào hệ thống của tổ chức.
Trong trường hợp này thì bên thứ ba là SolarWinds Orion Platform - một phần mềm giám sát hệ thống mạng được các tổ chức sử dụng (có cả U.S. federal government).
- Backdoor
- Russian group: Cozy Bear aka APT29 
- SUNSPOT -> SUNBURST
- FireEye

# Mục lục

- [1. SolarWinds là gì?](#1-solarwinds-là-gì)
- [2. Bản chất của vụ tấn công](#2-bản-chất-của-vụ-tấn-công)
- [3. Orion là gì và vì sao quan trọng?](#3-orion-là-gì-và-vì-sao-quan-trọng)
- [4. Timeline của vụ tấn công](#4-timeline-của-vụ-tấn-công)
- [5. Attack Chain chi tiết](#5-attack-chain-chi-tiết)
- [6. SUNBURST Backdoor hoạt động như thế nào](#6-sunburst-backdoor-hoạt-động-như-thế-nào)
- [7. Vì sao SolarWinds cực kỳ nguy hiểm](#7-vì-sao-solarwinds-cực-kỳ-nguy-hiểm)
- [8. Threat Actor](#8-threat-actor)
- [9. CIA Triad bị ảnh hưởng như thế nào?](#9-cia-triad-bị-ảnh-hưởng-như-thế-nào)
- [10. So sánh SolarWinds vs Equifax](#10-so-sánh-solarwinds-vs-equifax)
- [11. Lessons Learned](#11-lessons-learned)

---

# 1. SolarWinds là gì?

SolarWinds là công ty cung cấp phần mềm quản trị và giám sát hệ thống IT.

Sản phẩm nổi tiếng nhất:

- SolarWinds Orion

Orion được sử dụng để:

- monitor server
- monitor network
- monitor infrastructure
- quản trị hệ thống nội bộ doanh nghiệp

Nó thường có:

- quyền rất cao trong hệ thống
- truy cập sâu vào network
- khả năng đọc nhiều dữ liệu nhạy cảm

=> Đây là mục tiêu cực kỳ giá trị đối với attacker.

---

# 2. Bản chất của vụ tấn công

Đây KHÔNG phải kiểu:

Hack từng công ty một

Mà là:

Hack nhà cung cấp phần mềm

## Supply Chain Attack

Attacker compromise SolarWinds:

SolarWinds → Orion Update → Thousands of Customers

Tức là:

1. attacker xâm nhập SolarWinds
2. chèn malware vào update Orion
3. SolarWinds ký số update hợp pháp
4. khách hàng tự tải về và cài đặt

=> malware được phân phối thông qua software update chính thức.

---

# 3. Orion là gì và vì sao quan trọng?

Orion là platform quản trị hạ tầng IT.

Nó thường:

- chạy trong internal network
- có quyền admin cao
- kết nối tới:
  - server
  - router
  - switch
  - cloud
  - Active Directory

Nếu compromise Orion:

= compromise "central nervous system" của enterprise

---

# 4. Timeline của vụ tấn công

| Thời gian | Sự kiện |
|---|---|
| 09/2019 | Attacker truy cập trái phép vào SolarWinds |
| 10/2019 | Thử nghiệm inject malicious code |
| 02/2020 | SUNBURST được đưa vào Orion |
| 03/2020 | SolarWinds phát hành update độc hại |
| 2020 | Khách hàng tải và cài update |
| 12/2020 | FireEye phát hiện và công bố vụ việc |

---

# 5. Attack Chain chi tiết

## Giai đoạn 1 — Initial Compromise

Attacker xâm nhập internal network của SolarWinds.

Có thể thông qua:

- credential theft
- compromised account
- CI/CD compromise
- development environment compromise

Mục tiêu:

Build Pipeline

---

## Giai đoạn 2 — Build Pipeline Compromise

Đây là phần nguy hiểm nhất.

Attacker:

- cài implant vào môi trường build
- chèn backdoor vào DLL hợp pháp
- đợi Orion compile bình thường

DLL bị chỉnh sửa:

SolarWinds.Orion.Core.BusinessLayer.dll

---

## Giai đoạn 3 — Code Signing Abuse

SolarWinds ký digital signature hợp pháp lên update.

=> malware trở thành:

Trusted software update

Security products khó detect vì:

- signed binary
- trusted vendor
- legitimate update process

---

## Giai đoạn 4 — Distribution

Khách hàng:

- tải update
- verify signature
- cài đặt bình thường

Khoảng 18,000 organizations đã tải các phiên bản Orion bị ảnh hưởng.

---

## Giai đoạn 5 — Dormant / Stealth Phase

SUNBURST không hoạt động ngay.

Nó:

- sleep nhiều ngày
- kiểm tra environment
- detect sandbox
- tránh forensic tools

Mục tiêu:

Stealth Persistence

---

## Giai đoạn 6 — Command & Control (C2)

Sau thời gian ngủ:

malware kết nối về attacker infrastructure.

Ví dụ:

Victim → C2 Server

Attacker bắt đầu:

- reconnaissance
- victim profiling
- target selection

---

## Giai đoạn 7 — Selective Exploitation

Không phải mọi nạn nhân đều bị exploit sâu.

Attacker chọn:

- US government agencies
- security companies
- telecom
- cloud providers
- technology companies

=> Đây là chiến dịch cyber espionage có chọn lọc.

---

## Giai đoạn 8 — Post Exploitation

Sau khi compromise thành công:

attacker thực hiện:

- lateral movement
- credential theft
- token theft
- persistence
- email access
- cloud compromise

Kỹ thuật nổi bật:

- Golden SAML
- SAML token forgery

---

# 6. SUNBURST Backdoor hoạt động như thế nào

SUNBURST là backdoor stealthy.

Nó:

- chạy bên trong Orion process hợp pháp
- blend vào traffic bình thường
- dùng domain trông hợp pháp
- tránh detection

Điểm nguy hiểm:

Malware hoạt động bên trong trusted software

---

# 7. Vì sao SolarWinds cực kỳ nguy hiểm

## 7.1 Abuse of Trust

Khách hàng bị compromise vì:

Họ tin vendor

---

## 7.2 Scale cực lớn

Một lần compromise:

→ hàng nghìn tổ chức bị ảnh hưởng

---

## 7.3 Rất stealth

Attacker tồn tại trong hệ thống nhiều tháng.

---

## 7.4 Advanced Persistent Threat (APT)

Đây không phải random hacker.

Operation này:

- highly organized
- stealthy
- patient
- multi-stage
- intelligence-driven

---

# 8. Threat Actor

Nhiều phân tích cho rằng chiến dịch liên quan tới:

- APT29
- Cozy Bear
- Nobelium
- SVR (Russian Foreign Intelligence Service)

Tuy nhiên:

Cyber attribution không bao giờ chắc chắn tuyệt đối.

---

# 9. CIA Triad bị ảnh hưởng như thế nào?

| CIA Pillar | Impact | Giải thích |
|---|---|---|
| Confidentiality | Rất nghiêm trọng | Attacker truy cập email, dữ liệu, token |
| Integrity | Rất nghiêm trọng | Build pipeline và software update bị sửa đổi |
| Availability | Ít hơn | Mục tiêu chính là gián điệp, không phải phá hoại |

---

# 10. So sánh SolarWinds vs Equifax

| Yếu tố | SolarWinds | Equifax |
|---|---|---|
| Attack Type | Supply Chain Attack | Web Application Exploit |
| Vector | Software update | Apache Struts CVE |
| Scale | Hàng nghìn tổ chức | Một công ty |
| Goal | Cyber espionage | Data theft |
| Main Weakness | Trust chain | Unpatched vulnerability |
| Sophistication | Rất cao | Trung bình - cao |
| Stealth | Rất stealthy | Ít stealth hơn |

---

# 11. Lessons Learned

## 11.1 Trust cũng là attack surface

Không chỉ public server mới nguy hiểm.

Các thành phần cực kỳ quan trọng:

- CI/CD pipeline
- build server
- software signing
- vendor relationship
- identity infrastructure

---

## 11.2 Vendor compromise cực kỳ nguy hiểm

Một vendor bị hack:

→ kéo theo hàng nghìn khách hàng

---

## 11.3 Monitoring tools là high-value target

Các công cụ như:

- Orion
- SIEM
- monitoring system
- identity system

đều là mục tiêu hấp dẫn.

---

## 11.4 Zero Trust quan trọng hơn bao giờ hết

Không nên tin tưởng tuyệt đối:

- internal software
- signed binaries
- trusted vendors

---

## 11.5 Detection phải dựa trên behavior

Signature-based security là chưa đủ.

Cần:

- anomaly detection
- behavior monitoring
- threat hunting
- least privilege
- segmentation

---

# Chốt lại

SolarWinds 2020 là một chiến dịch:

Supply Chain Compromise
+
APT Cyber Espionage
+
Trust Exploitation

Đây là ví dụ kinh điển cho thấy:

"Trusted software"
không đồng nghĩa với
"Safe software"

# Resources
- https://www.ibm.com/docs/en/randori?topic=2022-solarwinds-orion-cve-2020-10148
- https://nvd.nist.gov/vuln/detail/CVE-2020-10148
- https://www.techtarget.com/whatis/feature/SolarWinds-hack-explained-Everything-you-need-to-know

