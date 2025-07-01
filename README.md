1. Giới thiệu dự án
   
1.1. Tên dự án

Tên dự án: Đánh giá và kiểm định chất lượng trang web thương mại điện tử Egagear

1.2. Mô tả

Dự án tập trung vào việc đánh giá và kiểm định chất lượng phần mềm cho website thương mại điện tử Egagear – một nền tảng cho phép người dùng tìm kiếm sản phẩm, đặt hàng và thanh toán trực tuyến. Nhóm đã áp dụng các kỹ thuật kiểm thử như kiểm thử hộp đen, hộp trắng, kiểm thử chức năng, kiểm thử hiệu năng và kiểm thử tự động với Selenium/JMeter nhằm đánh giá tính đúng đắn, hiệu suất, mức độ ổn định và khả năng sử dụng của hệ thống.

Mục tiêu của dự án là phát hiện và khắc phục các lỗi tiềm ẩn trong hệ thống, đồng thời đề xuất các cải tiến giúp website hoạt động ổn định hơn, thân thiện hơn với người dùng và đáp ứng tốt hơn nhu cầu mua sắm trực tuyến.

1.3. Mục tiêu kiểm thử

Các mục tiêu chính của quá trình kiểm thử bao gồm:

Xác minh chức năng: Kiểm tra tính đúng đắn của các chức năng chính như: đăng ký, đăng nhập, tìm kiếm sản phẩm, thêm vào giỏ hàng, thanh toán, và cập nhật hồ sơ cá nhân.

Kiểm tra hiệu suất: Đánh giá khả năng đáp ứng và tốc độ xử lý của hệ thống trong điều kiện người dùng truy cập đồng thời bằng công cụ JMeter.

Đảm bảo khả năng sử dụng (Usability): Kiểm tra mức độ thân thiện và dễ sử dụng của giao diện người dùng, quy trình mua hàng và cập nhật thông tin cá nhân.

Kiểm tra tính tương thích: Đảm bảo giao diện và chức năng hoạt động tốt trên nhiều trình duyệt khác nhau (Chrome, Firefox, Edge) và thiết bị (PC, điện thoại).

Phát hiện lỗi: Ghi nhận các lỗi chức năng, lỗi giao diện và hành vi không mong muốn trong suốt quá trình sử dụng.

Bảo mật cơ bản: Kiểm tra các vấn đề bảo mật ở mức cơ bản như kiểm soát đầu vào, xác thực đăng nhập và ngăn chặn các lỗ hổng phổ biến như XSS, SQL Injection.

2. Yêu cầu hệ thống
   
2.1. Yêu cầu chức năng
   
Các chức năng được đưa vào phạm vi kiểm thử bao gồm:

Đăng ký/Đăng nhập: Cho phép người dùng tạo và đăng nhập tài khoản.

Xem và cập nhật hồ sơ cá nhân: Xem thông tin cá nhân, chỉnh sửa tên, địa chỉ, mật khẩu, ảnh đại diện...

Tìm kiếm sản phẩm: Tìm kiếm sản phẩm theo từ khóa.

Xem chi tiết sản phẩm: Hiển thị thông tin đầy đủ về sản phẩm được chọn.

Thêm sản phẩm vào giỏ hàng: Lưu các sản phẩm đã chọn và thao tác thay đổi số lượng/xóa sản phẩm.

Thanh toán: Chọn phương thức thanh toán (ví điện tử hoặc khi nhận hàng), nhập thông tin giao hàng.

Xem lịch sử đơn hàng: Tra cứu lại các đơn hàng đã thực hiện.

Quản lý (dành cho admin): Quản lý sản phẩm, đơn hàng, danh mục, tài khoản người dùng và thống kê doanh thu.

2.2. Yêu cầu phi chức năng
Hiệu suất:

Thời gian phản hồi dưới 3 giây khi tải trang.

Hệ thống có thể xử lý tối thiểu 100 người dùng đồng thời mà không bị giảm hiệu năng đáng kể (kiểm thử với JMeter).

Khả năng sử dụng (Usability):

Giao diện đơn giản, trực quan, dễ thao tác.

Quy trình mua hàng rõ ràng, phù hợp với người dùng phổ thông.

Tính tương thích:

Tương thích với các trình duyệt phổ biến: Chrome, Firefox, Edge.

Giao diện responsive, hoạt động tốt trên thiết bị di động.

Độ tin cậy:

Tỷ lệ lỗi trên các chức năng chính dưới 1%.

Hệ thống có khả năng phục hồi trạng thái nếu gặp sự cố trong quá trình thanh toán hoặc nhập liệu.

Bảo mật (cơ bản):

Mã hóa mật khẩu người dùng (sử dụng bcrypt).

Bảo vệ chống lại các lỗi phổ biến như XSS, CSRF thông qua Laravel middleware.

Kiểm soát truy cập phân quyền rõ ràng (người dùng thường và admin).

3. Cài đặt và thiết lập
4. Cấu trúc dự án
5. Báo cáo kiểm thử

