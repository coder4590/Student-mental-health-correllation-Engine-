# from fastapi import FastAPI
# from .schemas import StudentInput, PredictionResponse, HealthResponse
# from .dependencies import get_model
# import pandas as pd
# from .nlp_engine import generate_full_response
# from .chatbot import chat
# from .schemas import ChatInput, ChatResponse
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
# import os

# app = FastAPI(title="MindGuard API", description="Student Mental Health Screening Tool")

# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Mount frontend folder as static files
# app.mount("/frontend", StaticFiles(directory=os.path.join(ROOT_DIR, "frontend")), name="frontend")


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/assessment")
# def serve_assessment():
#     return FileResponse(os.path.join(ROOT_DIR, "frontend", "assessment.html"))

# @app.get("/chatbot")
# def serve_chatbot():
#     return FileResponse(os.path.join(ROOT_DIR, "frontend", "chatbot.html"))

# model = get_model()


# @app.get("/")
# def serve_frontend():
#     return FileResponse(os.path.join(ROOT_DIR, "frontend", "index.html"))


# @app.get("/health", response_model=HealthResponse)
# def health():
#     return {"status": "healthy", "model_loaded": model is not None}

# from .nlp_engine import generate_full_response

# @app.post("/predict")
# def predict(data: StudentInput):
#     input_dict = data.model_dump()
#     input_df = pd.DataFrame([input_dict])
    
#     prediction = int(model.predict(input_df)[0])
    
#     if prediction == 0:
#         risk = "Low"
#     elif prediction == 1:
#         risk = "High"
    
#     full_response = generate_full_response(data, prediction, risk)
    
#     return {
#         "prediction": prediction,
#         "risk_level": risk,
#         "response": full_response
#     }


# @app.post("/chat", response_model=ChatResponse)
# def chat_endpoint(data: ChatInput):
#     return chat(data.message)

from fastapi import FastAPI
from .schemas import StudentInput, PredictionResponse, HealthResponse
from .dependencies import get_model
import pandas as pd
from .nlp_engine import generate_full_response
from .chatbot import chat
from .schemas import ChatInput, ChatResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import sqlite3
from datetime import datetime
from pydantic import BaseModel


app = FastAPI(title="MindGuard API", description="Student Mental Health Screening Tool")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = get_model()

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


DB_PATH = os.path.join(ROOT_DIR, "data", "survey.db")

def init_survey_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS survey_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prediction_accurate TEXT,
            chat_helpful TEXT,
            recommend TEXT,
            ease_of_use TEXT,
            extra_sleep TEXT,
            extra_exercise TEXT,
            extra_stress TEXT,
            extra_social TEXT,
            extra_professional_help TEXT,
            extra_lonely TEXT,
            extra_academic TEXT,
            extra_features TEXT,
            extra_comments TEXT,
            submitted_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_survey_db()

class SurveyInput(BaseModel):
    prediction_accurate: str
    chat_helpful: str
    recommend: str
    ease_of_use: str
    extra_sleep: str = ""
    extra_exercise: str = ""
    extra_stress: str = ""
    extra_social: str = ""
    extra_professional_help: str = ""
    extra_lonely: str = ""
    extra_academic: str = ""
    extra_features: str = ""
    extra_comments: str = ""

@app.post("/survey")
def submit_survey(data: SurveyInput):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO survey_responses 
        (prediction_accurate, chat_helpful, recommend, ease_of_use,
         extra_sleep, extra_exercise, extra_stress, extra_social,
         extra_professional_help, extra_lonely, extra_academic,
         extra_features, extra_comments, submitted_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.prediction_accurate, data.chat_helpful, data.recommend, data.ease_of_use,
        data.extra_sleep, data.extra_exercise, data.extra_stress, data.extra_social,
        data.extra_professional_help, data.extra_lonely, data.extra_academic,
        data.extra_features, data.extra_comments,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Survey submitted successfully"}

# Frontend — DEAD LAST, serves everything
app.mount("/", StaticFiles(directory=os.path.join(ROOT_DIR, "frontend"), html=True), name="frontend")