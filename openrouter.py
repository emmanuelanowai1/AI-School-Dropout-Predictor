import requests
import streamlit as st

# Get your API key from .streamlit/secrets.toml
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

def generate_openrouter_advice(student_data):
    prompt = f"""
You are an educational advisor.

Here is a student at risk of dropping out:
- Age: {student_data['Age']}
- CGPA: {student_data['CGPA']}
- Attendance Rate: {student_data['Attendance Rate']}%
- Behavioural Rating: {student_data['Behavioural Rating']}%
- Study Time: {student_data['Study Time']} hours/week
- Parental Support: {"Yes" if student_data['Parental Support'] == 1 else "No"}
- Extra Paid Class: {"Yes" if student_data['Extra Paid Class'] == 1 else "No"}

Please give brief and supportive advice (3–5 lines) to help this student stay motivated.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a caring education advisor who helps at-risk students stay in school."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ OpenRouter API Error:\n\n{e}"
