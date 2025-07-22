# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import joblib
from mistral import generate_mistral_advice, ask_teacher_bot

# Load model
model = joblib.load("dropout_model.pkl")

# Page config
st.set_page_config(page_title="🎓 School Dropout Predictor", layout="wide")

st.title("🎓 School Dropout Predictor with AI Insights")
st.markdown("AI-powered tool to predict dropout risks and suggest support strategies.")
st.markdown("---")

# Navigation tabs
tab1, tab2, tab3 = st.tabs(["📋 Manual Prediction", "📤 Bulk Prediction", "🧑‍🏫 AI Student Advisor"])

# ====================== TAB 1: MANUAL PREDICTION ======================
with tab1:
    st.header("📋 Enter Student Information")

    with st.form("student_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            reg_no = st.text_input("Registration Number")
            age = st.number_input("Age", 10, 30, 18)
        with col2:
            cgpa = st.number_input("CGPA", 0.0, 5.0, 2.5)
            attendance = st.number_input("Attendance Rate (%)", 0, 100, 70)
            behavior = st.number_input("Behavioral Rating (%)", 0, 100, 60)
        with col3:
            study_time = st.number_input("Weekly Study Time (hrs)", 0, 50, 8)
            support = st.selectbox("Parental Support", ["Yes", "No"])
            paid_class = st.selectbox("Attending Paid Extra Class?", ["Yes", "No"])
        submit = st.form_submit_button("🔎 Predict Dropout Risk")

    if submit:
        # Encode
        support_bin = 1 if support.upper() == "YES" else 0
        paid_class_bin = 1 if paid_class.upper() == "YES" else 0

        input_df = pd.DataFrame([{
            "Age": age,
            "CGPA": cgpa,
            "Attendance Rate": attendance,
            "Behavioural Rating": behavior,
            "Study Time": study_time,
            "Parental Support": support_bin,
            "Extra Paid Class": paid_class_bin
        }])
        input_df = input_df[model.feature_names_in_]

        # Prediction
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1] * 100

        # Display Risk Score
        st.markdown("---")
        st.subheader("🎯 Dropout Risk Score")
        st.markdown(f"**{prob:.2f}% Likely to Drop Out**")
        st.progress(min(int(prob), 100))

        # Verdict
        if prediction:
            st.error("❌ This student is at **high risk** of dropping out.")
        else:
            st.success("✅ This student is **not at immediate risk**.")

        # 🔵 Risk Labels
        if prob >= 80:
            st.markdown("🚨 **Critical Risk! Immediate intervention needed.**")
        elif prob >= 50:
            st.markdown("⚠️ **Moderate Risk. Monitor closely.**")
        else:
            st.markdown("🟢 **Low Risk. Keep supporting the student.**")

        # 🧷 Smart Warnings
        st.markdown("### 🧷 Smart Warning Tags")
        if attendance < 60:
            st.warning("⚠️ Very Low Attendance")
        if cgpa < 2.0:
            st.warning("📉 Low CGPA — Academic support needed")
        if behavior < 50:
            st.warning("😟 Behavioural Support May Be Needed")
        if study_time < 5:
            st.info("⏰ Low Study Time — Encourage more structured study")
        if support.upper() == "NO":
            st.info("👨‍👩‍👧‍👦 Consider involving guardians")

        # 🤖 AI Copilot Advice
        st.markdown("### 🤖 AI Risk Insight & Advice")
        ai_advice = generate_mistral_advice(input_df.iloc[0].to_dict())
        st.info(ai_advice)

# ====================== TAB 2: BULK PREDICTION ======================
with tab2:
    st.header("📤 Upload CSV for Bulk Predictions")
    st.markdown("Ensure your CSV matches the expected structure below.")
    
    try:
        sample_data = pd.read_csv("MODEL TRAINING DATASET.csv").head()
        st.markdown("### 📌 Sample Format:")
        st.dataframe(sample_data)
    except:
        st.warning("Sample data not found. Please upload your CSV file.")

    uploaded_file = st.file_uploader("Upload File", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df['Parental Support'] = df['Parental Support'].astype(str).str.upper().map({"YES": 1, "NO": 0})
        df['Extra Paid Class'] = df['Extra Paid Class'].astype(str).str.upper().map({"YES": 1, "NO": 0})

        X = df.drop(columns=['Dropout'], errors='ignore')
        X = X[model.feature_names_in_]

        df['Dropout Prediction'] = model.predict(X)
        df['Dropout Risk (%)'] = model.predict_proba(X)[:, 1] * 100

        # AI Suggestions for each row
        df['AI Suggestion'] = [
            generate_mistral_advice(row.to_dict())
            for _, row in X.iterrows()
        ]

        st.subheader("📊 Results")
        st.dataframe(df)

        # Download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "dropout_predictions.csv", "text/csv")

# ====================== TAB 3: AI Q&A TEACHER COPILOT ======================
with tab3:
    st.header("🧑‍🏫 AI-Powered Support Bot")
    st.markdown("Ask anything like:\n- *What does low CGPA and low attendance mean?*\n- *How can I help a critical-risk student?*")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.text_input("Ask your question here...")

    if st.button("Ask AI") and question:
        st.session_state.chat_history.append(("You", question))
        answer = ask_teacher_bot(question)
        st.session_state.chat_history.append(("AI Support Bot", answer))

    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.chat_message("user").markdown(f"**You:** {msg}")
        else:
            st.chat_message("assistant").markdown(f"🧠 {msg}")

# ====================== FOOTER ======================
st.markdown("---")
st.markdown("💡 [Calculate CGPA Online](https://cgpacalculator.com.ng/)")
st.markdown("Built with ❤️ using Streamlit and Mistral AI")
