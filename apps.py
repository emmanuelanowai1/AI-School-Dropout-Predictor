# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import joblib
from mistral_ai import generate_mistral_advice
from reportlab.pdfgen import canvas
import tempfile
import base64

# Load model
model = joblib.load("dropout_model.pkl")

# Page config
st.set_page_config(
    page_title="🎓 School Dropout Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("🎓 School Dropout Predictor with AI Copilot")
st.markdown("---")

# Sidebar quick links
with st.sidebar:
    st.header("🔧 Quick Tools")
    if st.button("📄 Generate Sample Parent Report"):
        def create_pdf():
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                c = canvas.Canvas(tmp.name)
                c.drawString(100, 750, "📄 Sample Parent Report")
                c.drawString(100, 730, "This section will generate real report after prediction.")
                c.save()
                return tmp.name

        pdf_path = create_pdf()
        with open(pdf_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="Parent_Report.pdf">📥 Download Sample PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📋 Manual Prediction", "📤 Bulk Upload", "👥 Compare Students"])

# ===========================
# 📋 Manual Prediction
# ===========================
with tab1:
    st.header("📋 Enter Student Data")
    with st.form("manual_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            reg_no = st.text_input("Registration Number")
            age = st.number_input("Age", 10, 30, 18)
        with col2:
            cgpa = st.number_input("CGPA", 0.0, 5.0, 2.5)
            attendance = st.number_input("Attendance Rate", 0, 100, 70)
            behaviour = st.number_input("Behavioural Rating", 0, 100, 60)
        with col3:
            study_time = st.number_input("Study Time", 0, 100, 10)
            support = st.selectbox("Parental Support", ["YES", "NO"])
            paid_class = st.selectbox("Extra Paid Class", ["YES", "NO"])

        submitted = st.form_submit_button("🎯 Predict")

    if submitted:
        ps = 1 if support == "YES" else 0
        pc = 1 if paid_class == "YES" else 0

        input_df = pd.DataFrame({
            "Age": [age],
            "CGPA": [cgpa],
            "Attendance Rate": [attendance],
            "Behavioural Rating": [behaviour],
            "Study Time": [study_time],
            "Parental Support": [ps],
            "Extra Paid Class": [pc]
        })

        input_df = input_df[model.feature_names_in_]
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1] * 100

        st.markdown("---")
        st.subheader("🎯 Dropout Risk Score")
        st.markdown(f"**{prob:.2f}% Likely to Drop Out**")
        st.progress(min(int(prob), 100))

        if prediction:
            st.error("❌ This student is at **high risk** of dropping out.")
        else:
            st.success("✅ This student is **not at immediate risk**.")

        if prob >= 80:
            st.markdown("🚨 **Critical Risk! Immediate intervention needed.**")
        elif prob >= 50:
            st.markdown("⚠️ **Moderate Risk. Monitor closely.**")
        else:
            st.markdown("🟢 **Low Risk. Keep supporting the student.**")

        # Smart Tags
        st.markdown("### 🧷 Smart Warning Tags")
        if attendance < 60:
            st.warning("⚠️ Very Low Attendance")
        if cgpa < 2.0:
            st.warning("📉 Poor Academic Performance")
        if behaviour < 50:
            st.warning("😟 Behavioural Support Needed")
        if study_time < 5:
            st.info("⏰ Encourage More Study Time")
        if support == "NO":
            st.info("👨‍👩‍👧‍👦 Consider engaging guardians")

        # AI Copilot
        st.markdown("### 🤖 AI Copilot Suggestion")
        ai_advice = generate_mistral_advice(input_df.iloc[0].to_dict())
        st.info(ai_advice)

        # 📄 Generate Parent PDF
        st.markdown("### 📄 Downloadable Parent Report")
        if st.button("Generate PDF Report"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                c = canvas.Canvas(tmp.name)
                c.drawString(100, 800, "🎓 School Dropout Report")
                c.drawString(100, 780, f"Student: {reg_no}")
                c.drawString(100, 760, f"Risk Score: {prob:.2f}%")
                c.drawString(100, 740, "AI Advice:")
                text = c.beginText(100, 720)
                for line in ai_advice.split('\n'):
                    text.textLine(line)
                c.drawText(text)
                c.save()
                with open(tmp.name, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                    link = f'<a href="data:application/pdf;base64,{b64}" download="{reg_no}_report.pdf">📥 Download Parent Report</a>'
                    st.markdown(link, unsafe_allow_html=True)

# ===========================
# 📤 Bulk Upload
# ===========================
with tab2:
    st.header("📤 Upload CSV File for Bulk Prediction")

    try:
        sample_data = pd.read_csv("MODEL TRAINING DATASET.csv").head()
        st.markdown("### 📌 Sample Format:")
        st.dataframe(sample_data)
    except:
        st.warning("Sample data not found. Please upload your CSV file.")
        
        uploaded = st.file_uploader("Upload a CSV", type="csv")

    if uploaded:
        df = pd.read_csv(uploaded)
        df['Parental Support'] = df['Parental Support'].str.upper().map({"YES": 1, "NO": 0})
        df['Extra Paid Class'] = df['Extra Paid Class'].str.upper().map({"YES": 1, "NO": 0})
        X = df[model.feature_names_in_]

        df['Dropout Prediction'] = model.predict(X)
        df['Dropout Risk (%)'] = model.predict_proba(X)[:, 1] * 100
        df['AI Advice'] = [generate_mistral_advice(row.to_dict()) for _, row in X.iterrows()]

        st.subheader("📊 Results")
        st.dataframe(df)

        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results CSV", csv_data, "dropout_predictions.csv", "text/csv")

# ===========================
# 👥 Compare Students
# ===========================
with tab3:
    st.header("👥 Compare Two Students Side-by-Side")
    st.markdown("Fill in data for both students below:")

    c1, c2 = st.columns(2)
    student_inputs = []

    for col in [c1, c2]:
        with col:
            st.markdown("### 🎓 Student")
            age = st.number_input(f"Age", 10, 30, 18, key=col)
            cgpa = st.number_input(f"CGPA", 0.0, 5.0, 2.5, key=f"cgpa_{col}")
            attendance = st.number_input(f"Attendance", 0, 100, 70, key=f"att_{col}")
            behaviour = st.number_input(f"Behaviour", 0, 100, 60, key=f"beh_{col}")
            study = st.number_input(f"Study Time", 0, 100, 10, key=f"study_{col}")
            support = st.selectbox(f"Parental Support", ["YES", "NO"], key=f"sup_{col}")
            paid = st.selectbox(f"Paid Class", ["YES", "NO"], key=f"pay_{col}")

            input_dict = {
                "Age": age,
                "CGPA": cgpa,
                "Attendance Rate": attendance,
                "Behavioural Rating": behaviour,
                "Study Time": study,
                "Parental Support": 1 if support == "YES" else 0,
                "Extra Paid Class": 1 if paid == "YES" else 0
            }
            student_inputs.append(input_dict)

    if st.button("🔍 Compare Now"):
        for idx, student in enumerate(student_inputs, start=1):
            df = pd.DataFrame([student])[model.feature_names_in_]
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0][1] * 100

            st.markdown(f"#### Student {idx} - Risk: **{prob:.2f}%**")
            st.progress(min(int(prob), 100))
            if pred:
                st.error("❌ Likely Dropout")
            else:
                st.success("✅ Safe")
            st.markdown("**AI Suggestion:**")
            st.info(generate_mistral_advice(student))

# ===========================
# Footer
# ===========================
st.markdown("---")
st.markdown("💡 [Calculate CGPA Online](https://cgpacalculator.com.ng/)")
