# 🎓 DropAlert NG — AI-Powered Student Dropout Predictor

An innovative AI-driven system that predicts student dropout risk and provides actionable insights to support academic success.

> ⚡ Powered by Data Analysis, Machine Learning + AI-Powered Student Advisor  
> 🇳🇬 Built for the Nigerian education system  
> 🧠 Showcased at the July 3MTT Knowledge Showcase

---

## 🚀 Features

- 🎯 **Dropout Risk Score Meter** – Predict likelihood of a student dropping out (0–100%)
- 📘 **AI-Powered Advisor** – Get smart, human-like explanations and academic advice
- 📥 **CSV Upload for Bulk Predictions** – Upload and analyze multiple students at once
- 🧷 **Smart Warning Tags** – Flags low CGPA, low attendance, poor behavior, etc.
- 🧑‍🏫 **Teacher Q&A Chatbot** – Ask the AI for support ideas and early interventions
- 🧾 **Downloadable CSV Reports** – Export predictions + AI insights
- ✅ **Mobile-Friendly Interface** – Streamlit-powered and responsive

---

## 🧠 How It Works

1. **Student data** (like CGPA, attendance, study time) is entered manually or via CSV.
2. A trained machine learning model predicts dropout probability.
3. An AI advisor explains the prediction and recommends interventions.
4. Educators can chat with the **AI Academic Advisor** for guidance.

---

## 📸 Demo Screenshots

| Risk Prediction Page | AI Advisor Chat |
|----------------------|-----------------|
| ![Prediction Screenshot](https://via.placeholder.com/500x300?text=Risk+Score+Screenshot) | ![Chat Screenshot](https://via.placeholder.com/500x300?text=AI+Chat+Screenshot) |

> 🧪 Want to try the app? Head to [Streamlit Cloud Deployment](#) (insert live link if deployed)

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/school-dropout-predictor.git
cd school-dropout-predictor
pip install -r requirements.txt
streamlit run app.py

---

## 🤖 API Integration

This app integrates Mistral AI via [OpenRouter](https://openrouter.ai/) to provide intelligent academic insights and chatbot support for teachers.

### AI Functions Used:

- `generate_mistral_advice(input_data_dict)` – Returns smart intervention suggestions for each student, based on their risk profile.
- `ask_teacher_bot(question)` – Lets teachers ask natural language questions like:
  - *“What support can help a student with low CGPA and poor attendance?”*
  - *“How to reduce dropout risk in SS2 students?”*

🔐 **Note:** You must include your OpenRouter API key as an environment variable or directly in the `mistral_ai.py` file:
```python
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "HTTP-Referer": "https://your-project-url.com"
}
