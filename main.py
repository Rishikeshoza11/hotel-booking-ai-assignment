from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Hotel Booking Analytics API")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """Replace this with your RAG system"""
    return {"answer": "Implementation pending", "question": request.question}

@app.get("/analytics")
async def get_analytics():
    """Replace with your analytics"""
    return {"revenue_trends": "Data not loaded"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
