import requests
import streamlit as st

HF_API_KEY = st.secrets["HF_API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/cohere/command-r-plus"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def generate_cohere_advice(student_data):
    prompt = (
        "As a student advisor AI, analyze this student's profile and suggest how to improve their academic success.\n\n"
        f"Student Details:\n"
        f"- Age: {student_data['Age']}\n"
        f"- CGPA: {student_data['CGPA']}\n"
        f"- Attendance Rate: {student_data['Attendance Rate']}%\n"
        f"- Behavioural Rating: {student_data['Behavioural Rating']}%\n"
        f"- Study Time (hours/week): {student_data['Study Time']}\n"
        f"- Parental Support: {'Yes' if student_data['Parental Support'] else 'No'}\n"
        f"- Extra Paid Class: {'Yes' if student_data['Extra Paid Class'] else 'No'}\n\n"
        f"AI Advice:"
    )

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"].split("AI Advice:")[-1].strip()
    else:
        return f"⚠️ Hugging Face API Error: {response.status_code}\n{response.text}"
