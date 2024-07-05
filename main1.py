from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
 
app = FastAPI()
 
# Define the request and response models
class ChatRequest(BaseModel):
    message: str
 
class ChatResponse(BaseModel):
    response: str
 
# Gemini API endpoint and authentication details
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY"  # Replace with actual endpoint
GEMINI_API_KEY = "AIzaSyD1hHhzOeCpsM0stiahX_kFz4EnyruHlo4"  # Replace with your API key
 
def get_gemini_response(message: str) -> str:
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": message
    }
 
    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        return response_data["response"]
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=response.status_code, detail=str(e))
 
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = get_gemini_response(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))