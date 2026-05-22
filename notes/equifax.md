# 📚 Mục lục

- [🔎 Tổng quan vụ Equifax (2017)](#-tổng-quan-vụ-equifax-2017)

- [🧨 Diễn biến (1)](#-diễn-biến-1)

- [🕸️ Diễn biến (2) — Pivot vào nội bộ](#️-diễn-biến-2--pivot-vào-nội-bộ)

- [📉 Hậu quả cuối cùng](#-hậu-quả-cuối-cùng)

- [🧠 Case Study kinh điển cho](#-đây-là-case-study-kinh-điển-cho)

- [🎬 Attack Chain — Full Drama](#-attack-chain--full-drama)

- [🛑 Phân tích dưới lăng kính bảo mật cốt lõi](#-bổ-sung-phân-tích-dưới-lăng-kính-bảo-mật-cốt-lõi)

- [📈 Kết luận về Risk](#-kết-luận-về-risk-rủi-ro)

- [🧠 Bài học cốt lõi](#-bài-học-cốt-lõi)

# 🔎 Tổng quan vụ Equifax (2017)

> **Keywords**
> - CVE-2017-5638
> - RCE
> - Apache Struts
> - OGNL Injection
> - Patch Management Failure

- **Victim:** Equifax — đại khái là nhỏ này theo dõi mọi thông tin về tài chính, vay bla bla của phần lớn người dân ở Mỹ  
  *(bị lộ thông tin cỡ 147 triệu người à 😉)*

---

## 🧨 Diễn biến (1)

Vào 1 ngày đẹp trời anh H scan Internet và...

> 💥 BUMP! Apache Struts bị public CVE-2017-5638

Ảnh vội hỏi:

> "Có ai còn chạy Struts vulnerable hemm?" 👀

...và yass chính ẻm — **Equifax** 😭

Trước khi tiếp tục, cần phải tìm hiểu 2 nhỏ:

- **Apache Struts**
- **CVE-2017-5638**

---

## 🧱 Apache Struts là gì?

**Apache Struts** là framework Java dùng để viết web application kiểu MVC. Spring Boot bây giờ phổ biến thế nào thì Struts ngày xưa cũng enterprise như vậy 😭

---

## ☠️ CVE-2017-5638 là gì?

Đây là một lỗ hổng cực kỳ nghiêm trọng trong Apache Struts, cho phép hacker: thực thi lệnh từ xa *(Remote Code Execution — RCE)* chỉ bằng một HTTP request được chế tạo đặc biệt.

---

# 🔍 Lỗ hổng nằm ở đâu?

Nó nằm ở phần xử lý upload file (`multipart/form-data`) của Apache Struts.

Bình thường khi user upload file, browser sẽ gửi request kiểu:

```http
POST /upload

Content-Type: multipart/form-data
```

Server Struts sẽ parse request bằng:

- *Jakarta Multipart Parser*

---

# 😭 Vấn đề là

khi anh H cố tình gửi `Content-Type` bị phá hỏng.

Thay vì gửi như người thường...

anh H là một người nổi loạn 😭  
ảnh nhét thêm payload vào header:

```http
Content-Type: %{...payload...}
```

---

# 💀 Lúc này:

- parser của Struts bị lỗi
- Struts tạo error message để báo lỗi
- nhưng tai hại là nó lại lấy luôn nội dung hacker gửi vào để xử lý tiếp
- và vô tình hiểu đoạn đó như lệnh **OGNL**

> *(OGNL = ngôn ngữ expression của Struts)*

---

# ⚡ Và rồi... RCE

Thay vì chỉ hiện lỗi...

Struts lại:

- evaluate payload như OGNL expression
- và cuối cùng thực thi command trên server 😭

---

## 🧠 Nói đơn giản thì:

Anh H cố tình gửi một request “dị dị” làm Struts hoảng loạn.

Trong lúc xử lý lỗi:

- Struts vô tình đọc payload như code thật
- rồi thực thi luôn trên server 💀

---

# 🕳️ Kết quả

Anh H đã có foothold ban đầu trên hệ thống Equifax 👰

Từ nay ảnh có thể:

- chạy command từ xa (RCE)
- đọc dữ liệu
- tải malware
- chiếm quyền server

chỉ bằng...

> ✨ một HTTP request trên server chưa được vá ✨

---

# 🕸️ Diễn biến (2) — Pivot vào nội bộ

Sau khi có được chỗ đứng trong tim Equifax 😭  
anh H không phải kiểu:

> "hack xong logout"

Ảnh bắt đầu:

- enumerate hệ thống
- pivot sâu hơn vào internal network

---

## 🔎 Ban đầu ảnh làm gì?

- kiểm tra mình đang ở đâu

```bash
whoami
hostname
```

- xem server kết nối database nào
- tìm credential
- tìm config file
- tìm API key
- enumerate internal network

---

# 😳 Và rồi ảnh nhận ra...

> "Ủa khoan… nhỏ này giữ dữ liệu tài chính thật!"

---

## 🏦 Equifax lúc đó lưu:

- Social Security Number (SSN)
- ngày sinh
- địa chỉ
- số bằng lái
- credit history
- thông tin vay nợ
- ...

của hàng chục triệu người Mỹ 😭

---

# 📦 Từ web server vulnerable → Data Breach lịch sử

Từ một web server vulnerable, anh H bắt đầu:

- pivot sâu hơn vào internal network
- truy cập database
- dump dữ liệu
- nén dữ liệu lại
- rồi exfiltrate từ từ ra ngoài

---

# ❓ Nhưng tại sao Equifax không phát hiện?

Một lượng dữ liệu khổng lồ chảy ra Internet suốt nhiều tháng...

mà Equifax không biết 😭

---

## ☠️ Sự thật cay đắng

Equifax có hệ thống giám sát mạng để detect dữ liệu bất thường đi ra ngoài.

Nhưng...

> SSL/TLS Certificate của thiết bị này đã hết hạn từ 10 tháng trước 💀

---

## 🧨 Hậu quả

Do certificate hết hạn:

- thiết bị không thể decrypt traffic HTTPS
- không inspect được dữ liệu outbound
- IDS/IPS gần như bị “mù”

Hacker đã:

- mã hóa dữ liệu đánh cắp
- exfiltrate qua HTTPS hợp lệ
- trong nhiều tháng
- mà không bị phát hiện 😭

---

# 😭 Điều đau đớn nhất

- Apache đã phát hành patch trước đó rồi
- nhưng Equifax chưa update
- hacker ở trong hệ thống rất lâu trước khi bị phát hiện

---

## 🎭 Kiểu kiểu

```text
Apache: "Patch đi bro 😭"

Equifax: "Để mai..."

Hacker: "Okay để tui vào luôn 👋"
```

---

# 📉 Hậu quả cuối cùng

- khoảng 147 triệu người bị lộ dữ liệu
- trở thành một trong những vụ data breach lớn nhất lịch sử Mỹ
- Equifax bị kiện và phạt hàng trăm triệu USD
- CEO và nhiều lãnh đạo bị chỉ trích cực mạnh

---

# 🧠 Đây là case study kinh điển cho:

- Patch Management Failure
- Vulnerability Management
- Asset Inventory Failure
- Internet-wide Scanning
- RCE từ public-facing web application
- Network Segmentation Failure
- Monitoring Failure

---

# 🎬 Attack Chain — Full Drama

```text
Public CVE-2017-5638 (Apache Struts)
            ↓
Hacker scan & phát hiện Equifax chưa patch
(Hỏng Asset & Patch Management)
            ↓
Exploit bằng OGNL Injection qua HTTP Content-Type Header
            ↓
Có RCE (Chiếm quyền Web Server public)
            ↓
Tìm thấy Plaintext Credentials của Database
            ↓
Pivot vào mạng nội bộ
(Thiếu Network Segmentation)
            ↓
Truy cập Database tổng
            ↓
Thu gom & nén dữ liệu nhạy cảm của 147 triệu người
            ↓
Exfiltrate dữ liệu qua HTTPS suốt nhiều tháng
(Hệ thống monitoring bị mù do SSL Cert hết hạn)
            ↓
💀 Combo Identity Theft lịch sử &
Thảm họa truyền thông 😭
```

---

# 🧩 Mapping với MITRE ATT&CK (để thoi chưa học tới =)))

| Giai đoạn | MITRE ATT&CK Technique |
|---|---|
| Scan Internet tìm server vulnerable | T1595 — Active Scanning |
| Exploit Apache Struts | T1190 — Exploit Public-Facing Application |
| Thực thi command từ xa | T1059 — Command and Scripting Interpreter |
| Enumerate hệ thống | T1082 — System Information Discovery |
| Tìm credential/config | T1552 — Unsecured Credentials |
| Pivot vào internal network | T1021 — Remote Services |
| Truy cập database | T1213 — Data from Information Repositories |
| Dump dữ liệu | T1005 — Data from Local System |
| Nén dữ liệu | T1560 — Archive Collected Data |
| Exfiltrate qua HTTPS | T1041 — Exfiltration Over C2 Channel |
| Ẩn trong traffic HTTPS | T1071.001 — Web Protocols |

# 🛑 Bổ sung: Phân tích Dưới Lăng Kính Bảo Mật Cốt Lõi

---

# 1. 🧠 Trụ cột nào trong CIA Triad đã bị xâm phạm?

Trong vụ Equifax 2017, cả ba trụ cột của CIA Triad đều bị ảnh hưởng ở các mức độ khác nhau.

Tuy nhiên, trụ cột bị tàn phá nặng nề nhất — và biến đây thành một thảm họa lịch sử — chính là:

> 🔥 **Confidentiality (Tính bảo mật)**

---

## 🔒 Confidentiality (Tính bảo mật)
### ❌ [BỊ XÂM PHẠM NGHIÊM TRỌNG]

Thông tin định danh cá nhân nhạy cảm *(PII)* và lịch sử tài chính của hơn **147 triệu người** vốn là bí mật cốt lõi đã bị:

- rò rỉ hoàn toàn
- xuất hiện trên thị trường đen
- bị truy cập trái phép bởi attacker

Các dữ liệu bị lộ bao gồm:

- Social Security Number (SSN)
- ngày sinh
- địa chỉ
- số bằng lái
- credit history
- thông tin vay nợ

---

## 🧩 Integrity (Tính toàn vẹn)
### ⚠️ [BỊ ĐE DỌA]

Mục tiêu chính của attacker là:

> trộm dữ liệu

Tuy nhiên, sau khi có được:

- RCE
- quyền điều khiển server
- khả năng truy cập database

thì attacker hoàn toàn có khả năng:

- sửa dữ liệu
- chèn dữ liệu giả
- xóa bản ghi tài chính
- thay đổi lịch sử tín dụng

nếu muốn 😭

Điều này khiến:

> tính toàn vẹn dữ liệu bị đe dọa nghiêm trọng.

---

## 🟢 Availability (Tính sẵn sàng)
### ⚠️ [BỊ ẢNH HƯỞNG GIÁN TIẾP]

Hệ thống không bị sập ngay lúc đó.

Tuy nhiên:

- Equifax phải shutdown nhiều hệ thống để điều tra
- vá lỗi khẩn cấp
- khôi phục hạ tầng
- xử lý khủng hoảng truyền thông

=> làm nhiều dịch vụ bị gián đoạn 😭

Điều này ảnh hưởng trực tiếp tới:

> tính sẵn sàng của dịch vụ.

---

---

# 2. 🧩 Mapping Tương Quan: Threat × Vulnerability × Asset

Áp dụng đúng mô hình nền tảng bảo mật:

```text
Threat × Vulnerability × Asset = Risk
```

case study này được bóc tách như sau 👇

---

# 💎 Asset (Tài sản cần bảo vệ)

## 🗃️ Tài sản dữ liệu (Core Data)

Cơ sở dữ liệu chứa:

- Social Security Number (SSN)
- ngày sinh
- địa chỉ
- số bằng lái
- hồ sơ điểm tín dụng

của hơn **147 triệu công dân Mỹ** 😭

---

## 🖥️ Tài sản công nghệ (Infrastructure)

Bao gồm:

- hệ thống public-facing web server
- ứng dụng Apache Struts
- database backend
- hạ tầng mạng nội bộ

---

## 💰 Tài sản vô hình (Business Asset)

Không chỉ dữ liệu 😭

Equifax còn mất:

- uy tín doanh nghiệp
- niềm tin công chúng
- giá trị cổ phiếu
- hình ảnh thương hiệu
- niềm tin từ đối tác tài chính

---

# 🕳️ Vulnerability (Lỗ hổng tồn tại)

---

## 💥 Lỗ hổng kỹ thuật (Technical Bugs)

### 🔥 CVE-2017-5638

Lỗ hổng:

- OGNL Injection
- dẫn tới Remote Code Execution (RCE)

trong:

> Jakarta Multipart Parser của Apache Struts

---

### 🔑 Plaintext Credentials

Thông tin đăng nhập database được lưu:

- dưới dạng plaintext
- trong hệ thống nội bộ

=> attacker dễ dàng lấy được credential 😭

---

### 🧨 SSL/TLS Certificate hết hạn

Certificate của hệ thống IDS/IPS:

- hết hạn hơn 10 tháng
- khiến hệ thống monitoring bị "mù"

=> không inspect được HTTPS outbound traffic.

---

# 🧾 Lỗ hổng quy trình (Process / GRC Flaws)

## 🐌 Patch Management Failure

Apache đã tung patch từ:

> tháng 3/2017

Nhưng Equifax:

- không update
- không kiểm tra asset đầy đủ
- bỏ quên hệ thống vulnerable

đến tận tháng 5–7/2017 😭

---

## 🕸️ Network Segmentation Failure

Sau khi compromise web server:

- attacker có thể pivot sâu vào internal network
- truy cập thẳng database quan trọng

=> chứng tỏ việc phân tách mạng rất lỏng lẻo.

---

# 🧨 Threat (Mối đe dọa)

---

## 👤 Threat Actor (Tác nhân)

Nhóm attacker có trình độ cao:

- khả năng Internet-wide scanning
- kỹ năng pivot chuyên nghiệp
- kỹ năng exfiltration mạnh
- được Mỹ cáo buộc liên quan đến quân đội nước ngoài

---

## ⚔️ Threat Action (Hành động đe dọa)

Attacker tiến hành:

- scan Internet
- tìm Apache Struts chưa vá
- exploit RCE
- leo thang đặc quyền
- truy cập database
- dump dữ liệu
- exfiltrate dữ liệu qua HTTPS

một cách âm thầm 😭

---

# 📈 Kết luận về Risk (Rủi ro)

Thảm họa này xảy ra khi:

- **Impact cực lớn**
  - dữ liệu tài chính quốc gia
  - PII cực kỳ nhạy cảm

gặp:

- **Likelihood cực cao**
  - RCE public
  - exploit có sẵn
  - exposed ra Internet
  - monitoring bị vô hiệu hóa

---

## 🎯 Công thức Risk

:contentReference[oaicite:0]{index=0}

---

# 🧠 Bài học cốt lõi

Equifax không thể kiểm soát được:

- Threat
- vì hacker luôn scan Internet 😭

Nhưng họ hoàn toàn có thể:

- vá lỗi đúng lúc
- kiểm kê asset đúng cách
- rotate certificate
- segment network
- monitor outbound traffic

Nói cách khác:

> Vulnerability mới chính là cánh cửa bị bỏ quên.

Và việc không vá lỗ hổng kịp thời...

chính là:

> 🔑 chiếc chìa khóa mở toang lâu đài cho kẻ trộm bước vào 😭

