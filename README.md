# 🎓 DropAlert NG – AI-Powered Student Dropout Predictor

An intelligent, data-driven tool that predicts student dropout risk and generates personalized AI insights — designed especially for schools and educators in Nigeria.

Built for the **3MTT Knowledge Showcase (July Edition)** to demonstrate how **AI + Data** can solve real educational problems in Nigeria.

---

## 🚀 Features

- ✅ Predict individual dropout risk using student data (CGPA, attendance, discipline, etc.)
- 📂 Upload Excel/CSV files for **bulk risk analysis**
- 🧠 Get **AI-generated intervention plans** for each student (powered by Mistral/OpenRouter)
- 📊 **Dropout risk meter** + smart warning labels (Low, Medium, High)
- 📥 Downloadable **Parent Report PDF**
- 💬 Chat with an **AI Academic Advisor** (Ask: “How can I help this student?”)
- 🎨 Enhanced UI with tabs, emojis, and icons
- 🧩 Easy deployment via Streamlit Cloud

---

## 🎯 How It Works

1. Collect or upload student academic and behavioral data.
2. Our trained ML model predicts the dropout likelihood.
3. The app displays a **Dropout Risk Score** and alert labels.
4. Mistral AI explains **why** the student is at risk and suggests what to do.
5. Lecturers/ Students can chat with the **AI Academic Advisor** for help.
6. Admins can download PDF reports for follow-up with parents/guardians.

---

## 📂 Project Structure

```bash
├── app.py                 # Main Streamlit app
├── dropout_model.pkl      # Trained machine learning model
├── mistral.py             # Handles Mistral AI chat and advice generation
├── MODEL TRAINING DATASET.csv     # Example data structure for bulk prediction
├── requirements.txt       # Required Python libraries
├── training_log.txt       # Model Training log
├── feature_importance.csv # Feature importance
```

## 🖼️ Demo Screenshots

### 🔍 Single Student Prediction
![bandicam 2025-07-22 16-59-33-850](https://github.com/user-attachments/assets/a87ffabf-f071-4e38-9f63-71a82f954b84)

### 📂 Bulk Upload from Excel
![bandicam 2025-07-22 17-00-06-666](https://github.com/user-attachments/assets/a6b784b5-33d7-42c8-a578-ff6fc44bcc97)

### 🧠 AI-Powered Academic Advisor  
![bandicam 2025-07-22 16-58-45-830](https://github.com/user-attachments/assets/08478559-c52f-4858-bbb4-bf1d16e9418c)

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/dropalert-ng.git
cd dropalert-ng

# Install required packages
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🙏 Acknowledgements

- 🇳🇬 **3MTT Nigeria** – For the learning opportunity and national tech empowerment.
- 🎓 **Darey.io** – For practical training in Data Analysis, Visualization.
- 🧠 **Mistral via OpenRouter** – For accessible powerful AI APIs.
- ⚙️ **Streamlit** – For simplifying the building of powerful data-driven web apps.
- 💡 **The Open Source Community** – For open tools, libraries, and constant inspiration.

---

## 📊 Project Status

- ✅ Trained ML model for dropout prediction
- ✅ Manual & bulk student risk assessment working
- ✅ AI academic advisor and insight generation functional
- ✅ Fully deployed with enhanced UI
- ⏳ In progress:
  - 🌐 Multilingual support (Pidgin, Hausa, Yoruba)
  - 🔊 Voice feedback & alert system

---

## ❤️ Built With Passion

Crafted with purpose to fight student dropout and promote early academic intervention.  
Developed by **Emmanuel Anowai and Adanma Iheanacho** as part of the **3MTT Knowledge Showcase – July Edition**.

> _"Not just a project — but a mission to keep more students in school, using data and AI as a force for good."_

---

## 📎 License

This project is open-source under the **MIT** License.
