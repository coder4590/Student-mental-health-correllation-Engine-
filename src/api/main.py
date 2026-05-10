from fastapi import FastAPI
from .schemas import StudentInput, PredictionResponse, HealthResponse
from .dependencies import get_model
import pandas as pd
from .nlp_engine import generate_full_response
from .chatbot import chat
from .schemas import ChatInput, ChatResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="MindGuard API", description="Student Mental Health Screening Tool")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mount frontend folder as static files
app.mount("/frontend", StaticFiles(directory=os.path.join(ROOT_DIR, "frontend")), name="frontend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = get_model()


@app.get("/")
def root():
    return {"message": "MindGuard API is running", "status": "healthy"}


@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "healthy", "model_loaded": model is not None}

from .nlp_engine import generate_full_response

@app.post("/predict")
def predict(data: StudentInput):
    input_dict = data.model_dump()
    input_df = pd.DataFrame([input_dict])
    
    prediction = int(model.predict(input_df)[0])
    
    if prediction == 0:
        risk = "Low"
    elif prediction == 1:
        risk = "High"
    
    full_response = generate_full_response(data, prediction, risk)
    
    return {
        "prediction": prediction,
        "risk_level": risk,
        "response": full_response
    }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(data: ChatInput):
    return chat(data.message)