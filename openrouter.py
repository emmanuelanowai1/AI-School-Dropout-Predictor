import requests
import os

# ✅ Replace with your actual OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or "your_openrouter_api_key_here"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# MODEL OPTIONS (You can change to other OpenRouter-supported models)
MODEL_NAME = "mistralai/mistral-7b-instruct:free"

# 1. 🔁 Generate AI Copilot Advice for a Student
def generate_mistral_advice(student_data: dict) -> str:
    prompt = f"""
You are an education expert helping a school detect and prevent student dropouts. A student has the following data:

- Age: {student_data.get("Age")}
- CGPA: {student_data.get("CGPA")}
- Attendance Rate: {student_data.get("Attendance Rate")}
- Behavioural Rating: {student_data.get("Behavioural Rating")}
- Study Time per week: {student_data.get("Study Time")}
- Parental Support: {'Yes' if student_data.get('Parental Support') == 1 else 'No'}
- Attends Paid Class: {'Yes' if student_data.get('Extra Paid Class') == 1 else 'No'}

Based on this, what are 2-3 key suggestions to help this student stay on track and avoid dropping out? Keep it short and practical.
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful educational assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ AI Advice Error: {str(e)}"

# 2. 🧠 Teacher Copilot – Ask Any Question
def ask_teacher_bot(question: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are an educational AI assistant who helps teachers with insights about student performance and dropout prevention."},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ AI Response Error: {str(e)}"
