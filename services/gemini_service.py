import os
import requests
from dotenv import load_dotenv
import certifi

# Load API key từ file .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Endpoint REST cho Gemini 2.0 Flash
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

def get_health_advice_from_gemini(prompt: str) -> str:
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, verify=certifi.where())
        response.raise_for_status()
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"[Lỗi REST API] {e}"

# Test
print(get_health_advice_from_gemini("Give me a health tip for people who sit at desks all day."))
