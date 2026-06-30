# Day 3 — NIST CSF 2.0 deep read

---

## Notes:
<!-- task 1: Open NIST CSF 2.0 PDF — read Preface and Section 1 (Overview): understand the purpose, who uses it, and why -->
### Overview:

- *Nội dung chính (Preface & Overview):* **NIST CSF 2.0** cung cấp 3 thành phần cốt lõi ***(Core, Profiles, Tiers)*** cùng các **tài nguyên bổ trợ**. Tổ chức sẽ kết hợp chúng lại để ***understand & assess, prioritize, và communicate*** về rủi ro an ninh mạng to manage and reduce their cybersecurity risks.

<!-- Read Section 2 (CSF Core): understand all 6 Functions — **GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER** — note that GOVERN is new in v2.0 -->
### CSF Core:

***1. GOVERN (GV)***: *The organization’s cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored*
- Outcomes của chức năng này là cơ sở định hướng cho tổ chức trong việc *achive* và *prioritize* các outcomes của 5 functions còn lại dựa trên bối cảnh hoạt động cũng như các kỳ vọng của các bên liên quan. 
- Các governace activities đóng vai trò then chốt trong việc tích hợp cybersecurity vào chiến lược quản lý rủi ro doanh nghiệp (ERM).
- Đề cập đến việc: hiểu organizational context; thiết lập cybersecurity strategy và cybersecurity supply chain risk management; các vai trò, trách nhiệm, thẩm quyền; chính sách; công tác giám sát (oversight) chiến lược An ninh mạng. 

***2. IDENTIFY (ID)***: *The organization’s current cybersecurity risks are understood.*
- Hiểu assests, suppliers, related cybersecurity risks
- Giúp doanh nghiệp prioritize các nỗ lực phù hợp với strategy và các yêu cầu khác đã được xác định trong Govern.
- Nhận diện được *improvement opportunities* của các chính sách, kế hoạch, quy trình, thủ tục,...

***3. PROTECT (PR)***: *Safeguards to manage the organization’s cybersecurity risks are used.*
- Được thực hiện sau khi các tài sản và rủi ro đã được xác định (identified) và sắp xếp thứ tự ưu tiên (prioritized).
- Bảo mật các tài sản để ngăn chặn hoặc làm giảm khả năng xảy ra (likelihood) cũng như tác động (impact) của các sự cố an ninh mạng bất lợi. Tăng khả năng và tác động của việc tận dụng các cơ hội công nghệ.
- Các kết quả mục tiêu (Outcomes) cụ thể được bao gồm: 
    + Quản lý danh tính, xác thực và kiểm soát truy cập (identity management, authentication, and access control).
    + Nhận thức và đào tạo (awareness and training).
    + Bảo mật dữ liệu (data security).
    + Bảo mật nền tảng – bao gồm bảo mật phần cứng, phần mềm và các dịch vụ của các nền tảng vật lý lẫn ảo hóa (platform security).
    + Tính kiên cường/khả năng chống chịu của hạ tầng công nghệ (the resilience of technology infrastructure).

***4. DETECT (DE):*** *Possible cybersecurity attacks and compromises are found and analyzed.*
- Cho phép phát hiện và phân tích kịp thời các hành vi bất thường (anomalies), các dấu hiệu hệ thống bị xâm nhập (indicators of compromise), và các sự kiện có khả năng bất lợi khác có thể cho thấy các cuộc tấn công và sự cố an ninh mạng đang diễn ra.
- Hỗ trợ cho các hoạt động ứng phó sự cố (incident response) và phục hồi (recovery) thành công.

***5. RESPOND (RS):*** *Actions regarding a detected cybersecurity incident are taken.*
- Hỗ trợ khả năng cô lập/chứa đựng (contain) các tác động của sự cố an ninh mạng.
- Các kết quả mục tiêu (Outcomes) cụ thể được bao gồm: quản lý sự cố (incident management), phân tích (analysis), giảm thiểu thiệt hại (mitigation), báo cáo (reporting), và truyền thông/giao tiếp (communication).

***6. RECOVER (RC):*** *Assets and operations affected by a cybersecurity incident are restored.*
- Hỗ trợ việc khôi phục kịp thời các hoạt động bình thường để giảm thiểu tác động của các sự cố an ninh mạng.
- Cho phép thực hiện việc truyền thông/giao tiếp phù hợp trong suốt các nỗ lực phục hồi.

![](/media/nist-csf-1.png)

```
GOVERN nằm ở tâm của bánh xe bởi vì nó định hình cách thức một tổ chức sẽ triển khai năm Chức năng còn lại
```

<!-- Read Section 3 (Profiles & Tiers): understand Current Profile vs Target Profile, and the 4 Tiers (Partial → Adaptive) -->
### CSF Profiles

Describes an organization’s current and/or target cybersecurity posture in terms of the Core’s outcomes.
Mỗi Organizational Profile bao gồm 1 hoặc cả 2: *Current Profile* và *Target Profile*. Ngoài ra còn có *Communiti Profile* có thể dùng để làm baseline.

![](/media/nist-csf-2.png)
- ***Step 1: scope.*** Thay vì làm cho toàn bộ thì chia ra, profile chỉ dành riêng cho *Phòng chống Ransomware cho hệ thống ERP*, hoặc *Hệ thống thanh toán của khách hàng*.
- ***Step 2: gather.*** Tìm kiếm thông tin làm context viết, ví dụ đọc về policies, BIA Register, work roles,...
- ***Step 3: create.*** Tạo 2 profiles. Tận dụng Community Profile để Target Profile ko bị quá cao siêu.
- ***Step 4: gap between current and target.*** Bạn phải viết ra một tài liệu cực kỳ quan trọng trong GRC là POA&M (Plan of Action and Milestones). Đây là một bảng tiến độ ghi rõ: "Để vá cái Gap về MFA này, chúng ta cần mua bản quyền phần mềm X, giao cho anh Bình phòng IT triển khai, ngân sách 10.000 USD, phải xong trước ngày 30/9."
- ***Step 5: implement action plan & update.*** Khi kế hoạch hành động (POA&M) được phê duyệt, đội ngũ kỹ thuật sẽ bắt tay vào cấu hình hệ thống, mua sắm thiết bị, đào tạo nhân viên. Tính liên tục: Khi các hạng mục trong kế hoạch hành động hoàn thành, trạng thái "Hiện tại" (Current Profile) của doanh nghiệp đã được nâng cấp lên một tầm cao mới. Lúc này, bạn lại cập nhật lại Hồ sơ tổ chức, tìm kiếm các khoảng cách mới và tiếp tục vòng lặp bảo mật của mình để đối phó với các mối đe dọa luôn biến đổi trong tương lai.

### CSF Tiers



<!-- Summarize all 6 Functions in your own words (e.g. "GOVERN = who is accountable for cybersecurity in the org") -->



--- 

## Socrates:

### Tại sao có sự xuất hiện của NIST CSF 2.0?
#### 1. Ai chủ trương thực hiện tài liệu này? (Tác giả & Người đứng sau)
- Người ra lệnh: Tổng thống Mỹ Barack Obama. Vào ngày 12 tháng 2 năm 2013, ông đã ký Sắc lệnh hành pháp 13636 (Executive Order 13636) về việc "Nâng cao năng lực an ninh mạng cho hạ tầng trọng yếu". Sắc lệnh này chính là "lệnh bài" bắt buộc phải tạo ra bộ khung này.
- Cơ quan thực hiện: NIST (National Institute of Standards and Technology) - Viện Tiêu chuẩn và Công nghệ Quốc gia Mỹ (thuộc Bộ Thương mại Mỹ). NIST là cơ quan cực kỳ uy tín trên thế giới về việc đặt ra các tiêu chuẩn kỹ thuật.
- Bên tham gia phối hợp: Chính phủ Mỹ yêu cầu NIST không được tự đóng cửa viết một mình, mà phải phối hợp chặt chẽ với khối tư nhân (các tập đoàn công nghệ, năng lượng, tài chính) để đảm bảo tài liệu này thực tế, dễ dùng chứ không bị nặng tính lý thuyết hay quan liêu.

#### 2. Bối cảnh lịch sử lúc đó là gì? (Context)
Vào những năm 2011 - 2013, thế giới chứng kiến một sự dịch chuyển đáng sợ của tội phạm mạng:
- Hạ tầng quốc gia bị đe dọa: Các cuộc tấn công mạng không còn dừng lại ở việc hack website hay ăn cắp thẻ tín dụng thông thường, mà bắt đầu nhắm vào hạ tầng trọng yếu (Critical Infrastructure) như: lưới điện, hệ thống cấp nước, viễn thông, và các nhà máy hạt nhân. Sự kiện sâu máy tính Stuxnet phá hủy các máy ly tâm hạt nhân của Iran trước đó vài năm là một hồi chuông cảnh tỉnh cực lớn.
- Khối tư nhân nắm giữ hạ tầng: Tại Mỹ, phần lớn các hạ tầng trọng yếu này (như các công ty điện lực, ngân hàng lớn, hãng hàng không) lại thuộc sở hữu của các công ty tư nhân, không phải của chính phủ.
- Sự bất lực của chính phủ: Chính phủ Mỹ không thể ép buộc các công ty tư nhân phải cấu hình máy móc theo ý mình vì luật pháp không cho phép can thiệp sâu vào kinh doanh. Do đó, nước Mỹ đứng trước nguy cơ bị tê liệt nếu các công ty tư nhân này bị hacker tấn công.
- Thiếu một ngôn ngữ chung về rủi ro an ninh mạng: Mỗi tổ chức, mỗi ngành và mỗi bộ tiêu chuẩn đều sử dụng thuật ngữ, cách đánh giá và phương pháp quản lý rủi ro khác nhau. Điều này khiến ban lãnh đạo doanh nghiệp, đội ngũ kỹ thuật và các cơ quan quản lý khó trao đổi, đánh giá và phối hợp hiệu quả. Vì vậy, một trong những mục tiêu quan trọng khi xây dựng NIST CSF là tạo ra một ngôn ngữ chung (common language) để mọi bên có thể thảo luận, đánh giá và quản lý rủi ro an ninh mạng một cách thống nhất.

#### 3. Nguyên nhân hình thành cốt lõi là gì? (Why)
Có ***3 nguyên nhân lớn*** dẫn đến việc hình thành NIST CSF:
**A. Cần một "Cây cầu" thay vì một "Bộ luật"**
- Chính phủ Mỹ cần một công cụ để thuyết phục và giúp đỡ các công ty tư nhân tự bảo vệ mình, thay vì dùng luật để ép buộc. Công cụ đó phải:
    + Miễn phí và tự nguyện (Voluntary): Ai dùng cũng được, không dùng không phạt (ở giai đoạn đầu).
    + Dễ hiểu: Giám đốc của một công ty cấp nước vùng nông thôn đọc cũng phải hiểu được mình cần làm gì, không cần phải là một chuyên gia mật mã học.
**B. Giải quyết tình trạng "Loạn tiêu chuẩn"**
- Lúc bấy giờ, trên thế giới có quá nhiều bộ tiêu chuẩn bảo mật (ISO 27001, COBIT, NIST SP 800-53, CIS Controls...). Doanh nghiệp giống như đứng giữa một ma trận, không biết nên theo chuẩn nào, bỏ chuẩn nào.
👉 NIST CSF đóng vai trò như một "khung chung", giúp doanh nghiệp kết nối và ánh xạ nhiều tiêu chuẩn khác nhau (ISO/IEC 27001, COBIT, NIST SP 800-53, CIS Controls...) vào một ngôn ngữ quản lý thống nhất.
**C. Sự tiến hóa lên Phiên bản 2.0 (Bối cảnh gần đây)**
- Phiên bản đầu tiên (v1.0 năm 2014 và v1.1 năm 2018) chỉ thiết kế riêng cho "Hạ tầng trọng yếu". Tuy nhiên, trong bối cảnh công nghệ ngày nay, bất kỳ doanh nghiệp nào (dù là một tiệm bánh hay một startup) cũng có thể bị phá sản vì ransomware.
👉 Đó là lý do vì sao bản CSF 2.0 được ra đời để mở rộng đối tượng cho TẤT CẢ các tổ chức trên thế giới, đồng thời thêm vào chức năng GOVERN (Quản trị). Việc bổ sung chức năng Govern phản ánh nhận thức rằng quản trị, quản lý rủi ro và sự tham gia của lãnh đạo là nền tảng để triển khai an ninh mạng hiệu quả, bên cạnh các biện pháp kỹ thuật..
