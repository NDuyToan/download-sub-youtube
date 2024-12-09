# YouTube Subtitle Downloader

Ứng dụng web đơn giản để tải phụ đề từ video YouTube với hai định dạng: SRT và TXT.

## Tính năng

- Tải phụ đề từ video YouTube thông qua URL
- Hỗ trợ hai định dạng file:
  - SRT (SubRip Subtitle): định dạng phụ đề chuẩn với timestamp
  - TXT: chỉ chứa nội dung text thuần túy
- Giao diện đơn giản, dễ sử dụng

## Yêu cầu hệ thống

- Python 3.6 trở lên
- pip (Python package installer)

## Cài đặt

1. Clone repository này về máy:

bash
git clone [url-repository-của-bạn]
cd youtube-subtitle-downloader

2. Cài đặt các thư viện cần thiết:

bash
pip install flask youtube_transcript_api

## Cấu trúc thư mục

youtube-subtitle-downloader/
├── app.py
├── templates/
│ └── index.html
└── README.md

## Cách sử dụng

1. Chạy ứng dụng:
   bash
   python app.py

2. Mở trình duyệt web và truy cập:

```
http://localhost:5000
```

3. Nhập URL video YouTube và chọn định dạng file muốn tải (SRT hoặc TXT)

4. Nhấn nút "Tải Phụ Đề" để tải file về máy

## Lưu ý

- Chỉ hoạt động với các video có phụ đề
- Cần có kết nối internet
- Một số video có thể bị hạn chế và không thể tải phụ đề
- Mặc định sẽ tải phụ đề tiếng Anh (nếu có)

## Lỗi thường gặp

1. "URL không hợp lệ": Kiểm tra lại URL video YouTube
2. "Transcript not available": Video không có sẵn phụ đề
3. "Video unavailable": Video không tồn tại hoặc đã bị xóa

## Phát triển trong tương lai

- [ ] Thêm tùy chọn chọn ngôn ngữ phụ đề
- [ ] Thêm preview phụ đề trước khi tải
- [ ] Hỗ trợ thêm các định dạng phụ đề khác
- [ ] Cải thiện giao diện người dùng

## Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo pull request hoặc báo cáo lỗi qua mục Issues.

## Giấy phép

[MIT License](LICENSE)

## Tác giả

[Nguyen Duy Toan]

## Liên hệ

- Email: [nguyenduytoanbkdn@gmail.com]
- GitHub: [https://github.com/NDuyToan]
