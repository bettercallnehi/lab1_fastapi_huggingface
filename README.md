# Lab 1 - Sentiment Analysis Web API 🚀

## 📋 Thông tin sinh viên
* **Họ và tên:** Phan Thế Minh Trí
* **Mã số sinh viên:** 24120506
* **Lớp:** Tư duy tính toán 24CTT3
---

## Mô hình sử dụng
Hệ thống tích hợp mô hình học máy hiện đại từ nền tảng **Hugging Face** để thực hiện tác vụ phân tích cảm xúc văn bản.
* **Tên model:** `distilbert-base-uncased-finetuned-sst-2-english`
* **Nhiệm vụ:** Sentiment Analysis (Phân loại cảm xúc Tích cực/Tiêu cực).
* **Link tham khảo:** [Hugging Face Model Hub](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
---
## Video demo:

https://drive.google.com/file/d/11yf7xo848_uWa-iIecPuDKDsObFvCdwK/view?usp=sharing

---

## Công nghệ triển khai
Dự án được xây dựng với các tiêu chuẩn kỹ thuật chuyên nghiệp, chú trọng vào tính ổn định và kiểm soát dữ liệu:
* **Framework:** FastAPI (Hiệu suất cao, hỗ trợ tài liệu hóa tự động).
* **Xác thực dữ liệu:** Pydantic (Sử dụng `Field` để ràng buộc dữ liệu đầu vào, đảm bảo không nhận chuỗi rỗng).
* **Xử lý ngoại lệ:** Tích hợp khối `try-except` khi khởi tạo pipeline để đảm bảo server không bị crash khi lỗi tải mô hình.
* **Đa luồng:** Chạy server bằng `uvicorn` hỗ trợ xử lý nhiều yêu cầu cùng lúc.

---
## Chi tiết danh sách Endpoints
1. GET /
Mô tả: Trả về thông tin sinh viên và giới thiệu hệ thống.

Response: JSON Object chứa student_info.

2. GET /health
Mô tả: Kiểm tra trạng thái hoạt động của Server và Model.

Response: {"status": "healthy"}

3. POST /predict
Mô tả: Tiếp nhận văn bản tiếng Anh và trả về kết quả phân tích.

Dữ liệu gửi lên (Request Body):
```JSON
{
  "text": "I really enjoy this Computer Science course!"
}
```
Dữ liệu trả về (Response): Bao gồm nhãn cảm xúc và điểm tin cậy (score).

---

## Hướng dẫn cài đặt và thực thi
### 0. Clone repo về VS

https://github.com/bettercallnehi/lab1_fastapi_huggingface

### 1. Cài đặt thư viện cần thiết
Mở Terminal tại thư mục dự án và chạy lệnh sau để cài đặt môi trường:
```bash
pip install -r requirement.txt
```
### 2. Kích hoạt Server
Sử dụng Python để thực thi file chính:
```bash
python main.py
```
### 3. Kiểm thử và Demo
Cách 1: Kiểm thử bằng Script Python
Dự án tách biệt rõ ràng logic server và logic kiểm thử. Bạn có thể chạy script sau để kiểm tra tự động:

```bash
python test_api.py
```

Cách 2: Kiểm thử tương tác (Swagger UI)
Truy cập: http://127.0.0.1:8000/docs

