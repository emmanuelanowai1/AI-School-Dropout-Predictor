import openai
import streamlit as st

# Set the OpenRouter endpoint and key
openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

def generate_advice_from_openrouter(student_data, reg_no=None):
    id_str = f" for REGISTRATION NUMBER {reg_no}" if reg_no else ""

    prompt = f"""
You're an educational advisor AI. Based on the following student data{id_str}, give supportive, practical advice in plain language.
Help the student understand their situation and suggest realistic ways to avoid dropping out and improve performance.

Student Info:
- Age: {student_data['Age']}
- CGPA: {student_data['CGPA']} / 5.0
- Attendance Rate: {student_data['Attendance Rate']}%
- Behavioural Rating: {student_data['Behavioural Rating']}%
- Study Time: {student_data['Study Time']} hrs/week
- Parental Support: {"YES" if student_data['Parental Support'] == 1 else "NO"}
- Extra Paid Class: {"YES" if student_data['Extra Paid Class'] == 1 else "NO"}

Respond in 3–5 sentences. Be encouraging and practical.
"""

    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful school advisor bot."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"⚠️ OpenRouter API Error: {e}"
