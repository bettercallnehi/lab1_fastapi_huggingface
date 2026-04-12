from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import pipeline
import uvicorn

app = FastAPI(
    title="Sentiment Analysis API",
    description="API phục vụ nhận diện cảm xúc từ văn bản sử dụng mô hình Hugging Face.",
    version="1.0.0"
)

class RequestData(BaseModel):
    text: str = Field(..., min_length=1, description="Văn bản tiếng Anh cần phân tích")

try:
    classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    print(f"Lỗi khi tải mô hình: {e}")

# Chức năng 1: GET 
@app.get("/")
async def root():
    return {
        "message": "Chào mừng bạn đến với Sentiment Analysis API!",
        "student_info": {
            "name": "Phan Thế Minh Trí",
            "id": "24120506"
        },
        "function": "API này nhận văn bản tiếng Anh và trả về nhãn cảm xúc (POSITIVE/NEGATIVE).",
        "docs_url": "/docs"
    }

# Chức năng 2: GET /health
@app.get("/health")
async def health_check():
    # Kiểm tra xem classifier đã được khởi tạo thành công chưa
    if classifier:
        return {"status": "healthy", "model": "loaded"}
    else:
        return {"status": "unhealthy", "model": "not_loaded"}

# Chức năng 3: POST /predict
@app.post("/predict")
async def predict(data: RequestData):
    """
    Nhận dữ liệu JSON {"text": "..."}, gọi mô hình và trả kết quả JSON.
    """
    try:
        # Gọi mô hình Hugging Face
        results = classifier(data.text)
        
        # Kết quả trả về phải rõ ràng, có cấu trúc [cite: 43, 118]
        return {
            "input_text": data.text,
            "prediction": results[0]["label"],
            "confidence_score": round(results[0]["score"], 4)
        }
    except Exception as e:
        # Xử lý các trường hợp lỗi trong quá trình suy luận
        raise HTTPException(status_code=500, detail=f"Inference Error: {str(e)}")

# 4. Chạy server (Sử dụng cho môi trường local)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)