# Equifax (2017)

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
