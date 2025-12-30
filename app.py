import streamlit as st
import pandas as pd
import pickle

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="centered"
)

st.title("📉 Customer Churn Prediction App")
st.write("Predict whether a customer will **Churn (1)** or **Not Churn (0)**")

st.divider()

# =========================
# LOAD MODEL & SCALER
# =========================
with open("finalized_LogReg.sav", "rb") as f:
    model = pickle.load(f)

with open("scaler_model.sav", "rb") as f:
    scaler = pickle.load(f)

# =========================
# FEATURE ORDER (MUST MATCH TRAINING)
# =========================
FEATURES = [
    'SeniorCitizen',
    'TenureMonths',
    'MonthlyCharges',
    'TotalCharges',
    'Gender_Male',
    'ContractType_One year',
    'ContractType_Two year',
    'InternetService_Fiber optic',
    'InternetService_No',
    'PaymentMethod_Electronic check'
]

num_cols = [
    'SeniorCitizen',
    'TenureMonths',
    'MonthlyCharges',
    'TotalCharges'
]

# =========================
# USER INPUTS
# =========================
st.subheader("🧾 Customer Inputs (Model Features)")

col1, col2 = st.columns(2)

with col1:
    SeniorCitizen = st.selectbox("Senior Citizen (0 = No, 1 = Yes)", [0, 1])
    TenureMonths = st.slider("Tenure (Months)", 1, 72, 12)
    MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 75.0)
    TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 900.0)
    Gender_Male = st.selectbox("Gender_Male (1 = Male, 0 = Female)", [0, 1])

with col2:
    Contract_One_Year = st.selectbox("ContractType_One year", [0, 1])
    Contract_Two_Year = st.selectbox("ContractType_Two year", [0, 1])
    Internet_Fiber = st.selectbox("InternetService_Fiber optic", [0, 1])
    Internet_No = st.selectbox("InternetService_No", [0, 1])
    Payment_Electronic = st.selectbox("PaymentMethod_Electronic check", [0, 1])

# =========================
# CREATE INPUT DATAFRAME
# =========================
input_df = pd.DataFrame([{
    'SeniorCitizen': SeniorCitizen,
    'TenureMonths': TenureMonths,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges,
    'Gender_Male': Gender_Male,
    'ContractType_One year': Contract_One_Year,
    'ContractType_Two year': Contract_Two_Year,
    'InternetService_Fiber optic': Internet_Fiber,
    'InternetService_No': Internet_No,
    'PaymentMethod_Electronic check': Payment_Electronic
}])

# Ensure correct column order
input_df = input_df.reindex(columns=FEATURES, fill_value=0)

# =========================
# SCALE NUMERIC FEATURES ONLY
# =========================
input_df[num_cols] = scaler.transform(input_df[num_cols])

# =========================
# PREDICTION
# =========================
if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_df)[0]

    st.divider()

    if prediction == 1:
        st.error("🚨 Prediction: Customer WILL CHURN (1)")
    else:
        st.success("✅ Prediction: Customer will NOT churn (0)")




