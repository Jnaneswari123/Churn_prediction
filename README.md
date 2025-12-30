🌐 Customer Churn Prediction – Streamlit Web App
📌 App Overview

This Streamlit web application predicts whether a customer is likely to churn (Yes/No) based on their demographic details, service usage, and payment behavior.

The app uses a trained Machine Learning classification model and provides real-time predictions through an interactive user interface.

🎯 Objective

To help businesses:

Identify customers at high risk of churn

Take proactive retention actions

Reduce customer loss

🖥️ Application Features

Interactive UI built with Streamlit
User-friendly input fields
Real-time churn prediction
Displays prediction as Yes / No
Uses the same preprocessing pipeline as training

📊 Input Features

The app accepts the following inputs:

Feature	Description
Gender - Male / Female
Senior - Citizen	Yes / No
Tenure - (Months)	Number of months with company
Monthly Charges	- nMonthly bill amount
Total Charges - Total bill amount
Contract Type	- Month-to-month / One year / Two year
Internet Service -	DSL / Fiber optic / No
Payment Method	- Credit card / Bank transfer / Electronic check

🧠 Machine Learning Model

Model Type: Classification

Algorithms Used:

*Logistic Regression
*Random Forest
*Gradient Boosting 
*K- Nearest Neighbors
*Navie Baye's
*Decision Tree
*Support Vector Machine

Target Variable:

Churn → Yes / No

⚙️ Preprocessing Pipeline

The same preprocessing steps used during training are applied in the app:

One-Hot Encoding for categorical variables
Feature scaling using StandardScaler
Column alignment with training data
This ensures consistent and accurate predictions.

🚀 How to Run the Streamlit App
1️⃣ Clone the Repository
git clone <>
cd C:\Users\satya\OneDrive\Desktop\4 logistic_reg_multiclass\chrun

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
streamlit run app.py


The app will open automatically in your browser.

📁 Project Structure
customer-churn-streamlit-app/
│
├── app.py
├── finalized_LogReg.sav
├── scaler_model.sav
├── requirements.txt
├── README.md
└── customer_churn_dataset.csv

🔮 Prediction Output

Yes → Customer is likely to churn
No → Customer is likely to stay

The prediction is generated instantly after clicking the Predict button.

🛠️ Technologies Used

Python
Streamlit
Pandas, NumPy
Scikit-learn

Matplotlib, Seaborn

🌱 Future Enhancements

Add churn probability percentage
Feature importance visualization
SHAP-based explanation
Deploy on Streamlit Cloud

👩‍💻 Author


Bongu Jnaneswari
