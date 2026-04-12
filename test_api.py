import requests
import json

# Địa chỉ API mặc định khi chạy uvicorn local
BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("--- Đang kiểm tra trạng thái hệ thống (/health) ---")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}\n")

def test_predict(text_input):
    print(f"--- Đang kiểm tra dự đoán với văn bản: '{text_input}' ---")
    payload = {"text": text_input}
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    
    if response.status_code == 200:
        print("Kết quả thành công!")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Lỗi: {response.status_code}")
        print(response.text)
    print("\n")

if __name__ == "__main__":
    # 1. Kiểm tra Health Check
    test_health()
    
    # 2. Kiểm tra với ít nhất 2 dữ liệu đầu vào (để chuẩn bị cho video demo) [cite: 70, 145]
    test_predict("This project is absolutely amazing and well-structured!")
    test_predict("I am feeling a bit tired today, but the code still works.")