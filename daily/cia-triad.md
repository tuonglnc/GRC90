# Day 1 — CIA Triad foundations

### CIA Triad - Definition:
1. Confidentiality (Tính bảo mật): "Ai có quyền mới được xem" - "Tui hong có quyền mà tui vẫn xem được thì seo 👻"
2. Integrity (Tính toàn vẹn): "Nhỏ Data còn **zin** hong bị mất, hong bị thêm, hong bị sửa..." - "Tui sẽ hủy hoại em Data bằng mọi giá 🤡"
3. Availability (Tính khả dụng): "Tui cần bên anh 24/24" - "Tui sẽ ko cho cô gặp anh ta 😈"

### CIA Triad - Case Study:
1. Confidentiality: [Equifax (2017)](../notes/equifax.md)
2. Integrity: [SolarWinds Orion (2020)](../notes/solarwinds.md)
3. Availability: [WannaCry (2017)](../notes/wannacry.md)

### Threat / Vulnerability / Asset
1. Asset: Là bất cứ thứ gì có giá trị đối với tổ chức hoặc cá nhân mà bạn cần bảo vệ.
2. Vulnerability: Là điểm yếu tồn tại trong hệ thống, quy trình, hoặc con người mà kẻ xấu có thể lợi dụng để xâm nhập hoặc gây hại.
3. Threat: Là bất kỳ tác nhân hoặc sự kiện nào có khả năng khai thác lỗ hổng để gây thiệt hại cho tài sản. Mối đe dọa cần có một tác nhân (Threat Actor) hoặc một nguồn (Threat Source).

   Mối quan hệ: $$\text{Threat} \times \text{Vulnerability} \times \text{Asset Value} = \text{Risk}$$

> Trong một tòa lâu đài kiên cố giữ một chiếc rương báu cổ giá trị (Asset), gã tướng cướp khét tiếng đang rình rập bên ngoài với âm mưu đột nhập chiếm đoạt tài sản (Threat); gã liên tục lượn lờ quanh các bức tường thành cho đến khi phát hiện ra một mật đạo ngầm bị bỏ quên không khóa (Vulnerability), và chính sự giao thoa tại thời điểm gã bước qua cánh cửa hớ hênh đó đã biến nguy cơ tiềm ẩn thành một hiểm họa mất mát nhãn tiền (Risk).

### `Risk = Likelihood × Impact`

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
