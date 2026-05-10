from pydantic import BaseModel, Field
from typing import Literal


class StudentInput(BaseModel):
    age: int = Field(..., ge=15, le=50, description="Age in years")
    gender: Literal['Female', 'Male'] = Field(..., description="Gender")
    relationship_status: Literal['Divorced', 'In a Relationship', 'Married', 'Single'] = Field(..., description="Relationship status")
    academic_status: Literal['1 Year', '2 Year', '3 Year', '4 Year'] = Field(..., description="Academic year")
    work_and_study: Literal['No', 'Yes'] = Field(..., description="Work and study status")
    residential_area: Literal['Hall', 'Outside Hall', 'With family'] = Field(..., description="Residential area")
    social_economic_status: Literal['Lower', 'Lower-Middle', 'Middle', 'Upper', 'Upper-Middle'] = Field(..., description="Socio-economic status")
    financial_pressure: Literal['No', 'Yes'] = Field(..., description="Financial pressure")
    has_debt: Literal['No', 'Yes'] = Field(..., description="Has debt")
    living_environment_satisfaction: Literal['No', 'Yes'] = Field(..., description="Living environment satisfaction")
    recent_loss: Literal['No', 'Yes'] = Field(..., description="Recent loss")
    physical_activity: Literal['No', 'Yes'] = Field(..., description="Physical activity")
    chronic_illness: Literal['Yes', 'No'] = Field(..., description="Chronic illness")
    medication: Literal['No', 'Yes'] = Field(..., description="On medication")
    smoking: Literal['No', 'Yes'] = Field(..., description="Smoking")
    alcohol: Literal['No', 'Yes'] = Field(..., description="Alcohol consumption")
    sleep_duration_hours: Literal['5 Hours', '6 Hours', '7 Hours', '8 Hours', 'Below 5 Hours', 'More than 8 hours'] = Field(..., description="Sleep duration")
    social_media_hours_daily: Literal['2–4 hours a day', '5–7 hours a day', '8–10 hours a day', 'Less than 2 hours', 'More than 10 hours a day'] = Field(..., description="Daily social media hours")
    academic_work_demands: Literal['No', 'Yes'] = Field(..., description="Academic work demands")


class PredictionResponse(BaseModel):
    prediction: float = Field(..., description="Predicted depression severity score")
    risk_level: str = Field(..., description="Risk level: Low, Moderate, or High")


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool

class ChatInput(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    category: str

    
