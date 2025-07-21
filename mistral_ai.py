import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {
    "Authorization": f"Bearer {st.secrets['HF_API_KEY']}"
}

def generate_mistral_advice(student_data):
    prompt = (
        "You're an academic advisor AI. Analyze the student's data and provide personalized advice.\n\n"
        f"Student Profile:\n"
        f"- Age: {student_data['Age']}\n"
        f"- CGPA: {student_data['CGPA']}\n"
        f"- Attendance Rate: {student_data['Attendance Rate']}%\n"
        f"- Behavioural Rating: {student_data['Behavioural Rating']}%\n"
        f"- Study Time: {student_data['Study Time']} hours/week\n"
        f"- Parental Support: {'Yes' if student_data['Parental Support'] else 'No'}\n"
        f"- Extra Paid Class: {'Yes' if student_data['Extra Paid Class'] else 'No'}\n\n"
        f"Advice:"
    )

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7,
        }
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"].split("Advice:")[-1].strip()
    else:
        return f"⚠️ Hugging Face API Error {response.status_code}: {response.text}"
