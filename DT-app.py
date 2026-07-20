import pandas as pd
import numpy as np
import pickle as pkl
import streamlit as st

with open("bankloan.pkl", "rb") as f:
    model = pkl.load(f)

with open("Accuracy.pkl", "rb") as f:
    accuracy = pkl.load(f)

df = pd.read_csv("bankloan.csv")


st.title('🏦 Bank Loan Approval Prediction')
st.image('loan_image.jpg')
st.subheader('Predict whether a customer is likely to be approved for a personal loan based on their financial and demographic information.')
Age = st.number_input("Customer Age (Range: 18–90 Years)",max_value=90,min_value=18,value=18)
Experience = st.number_input("Work Experience (Range: 0–45 Years)",max_value=45,min_value=0,value=0)
Income = st.number_input("Annual Income (Range: 8–250)(Thousands of $)",max_value=250,min_value=8,value=8)
Family = st.number_input("Number of Family Members (Range: 1–9)",max_value=9,min_value=1,value=1)
CCAvg = st.number_input("Average Monthly Credit Card Spending (Thousands of $)",max_value=10,min_value=0,value=0)
Education = st.selectbox("Education Level (1 = Undergraduate, 2 = Graduate, 3 = Advanced/Professional)",[1,2,3])
Mortgage = st.number_input("Mortgage Amount (Range: 0-700)(Thousands of $)",max_value=700,min_value=0,value=0)
Securities_Account = st.selectbox("Has Securities Account? (No = 0, Yes = 1)", [0,1])
CD_Account = st.selectbox("Has Certificate of Deposit (CD) Account? (No = 0, Yes = 1)", [0,1])
Online = st.selectbox("Uses Online Banking? (No = 0, Yes = 1)", [0,1])
CreditCard = st.selectbox("Uses Bank Credit Card? (No = 0, Yes = 1)", [0,1])


x_values = pd.DataFrame({
    'Age':[Age],'Experience':[Experience],'Income':[Income],'Family':[Family],'CCAvg':[CCAvg],
    'Education':[Education],'Mortgage':[Mortgage],'Securities_Account':[Securities_Account],
    'CD_Account':[CD_Account],'Online':[Online],'CreditCard':[CreditCard]
})


if st.button("Predict"):
    prediction = model.predict(x_values)
    if prediction == 1:
        st.success("You are likely to be approved")
        st.subheader('Model Performance')
        st.metric('Model Accuracy :', f'{accuracy * 100:.2f}%')
    else:
        st.error("You are not likely to be approved")

st.header('Input Submitted Processing')
st.table(x_values)


def footer():
    st.write("---")
    st.write("Heart Disease Prediction System")
    st.write("Developed by MEHRAN KHAN")
    st.write("© 2026 All Rights Reserved")
footer()


st.sidebar.title("🏦 Loan Approval System")

st.sidebar.markdown("""
### Requirements  

✔ Age

✔ Gender

✔ Experience

✔ Annual Income

✔ Family Members

✔ Average Credit Card Spending

✔ Education

✔ Mortgage

✔ Securities Account

✔ CD Account

✔ Online Banking

✔ Credit Card
""")




st.markdown("""
<style>

/* ===========================
   Main App Background
=========================== */
.stApp{
    background:
    linear-gradient(rgba(8,20,40,0.85), rgba(8,20,40,0.85)),
    url("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1920&q=80");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* ===========================
   Header
=========================== */
header{
    background: rgba(8,20,40,0.95) !important;
}

header *{
    color:white !important;
}

header svg{
    fill:white !important;
}

/* ===========================
   Footer
=========================== */
footer{
    background: rgba(8,20,40,0.95) !important;
    color:white !important;
}



footer *{
    color:white !important;
}

footer a{
    color:white !important;
}

/* ===========================
   Title
=========================== */
h1{
    color:white !important;
    text-align:center;
    font-size:42px;
    font-weight:bold;
}

/* ===========================
   Subheader
=========================== */
h2,h3{
    color:white !important;
}

/* ===========================
   Labels
=========================== */
label{
    color:black !important;
    font-weight:600;
}

/* ===========================
   General Text
=========================== */
p{
    color:white !important;
}

/* ===========================
   Number Input & Selectbox
=========================== */
.stNumberInput,
.stSelectbox{
    background:rgba(255,255,255,0);
    border-radius:10px;
}

/* ===========================
   Number Input & Selectbox
=========================== */
.stNumberInput,
.stSelectbox{
    background: rgba(255,255,255,0);
    border-radius: 10px;
}

/* Number Input */
div[data-testid="stNumberInput"] input{
    color: black !important;
    background-color: white !important;
}

/* Placeholder */
div[data-testid="stNumberInput"] input::placeholder{
    color: #666 !important;
}

/* Number Input + / - buttons */
div[data-testid="stNumberInput"] button{
    color: black !important;
    background-color: white !important;
}

/* Selectbox */
div[data-baseweb="select"] > div{
    background-color: white !important;
    color: black !important;
}

div[data-baseweb="select"] span{
    color: black !important;
}

div[data-baseweb="select"] svg{
    fill: black !important;
}


/* ===========================
   Predict Button
=========================== */
.stButton>button{
    width:100%;
    height:50px;
    background:#374151;
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:900;
}

.stButton>button:hover{
    background:#2563EB;
}

/* ===========================
   Metric Card
=========================== */
[data-testid="stMetric"]{
    background:rgba(255,255,255,0.10);
    padding:15px;
    border-radius:12px;
}

[data-testid="stMetricLabel"]{
    color:white !important;
}

[data-testid="stMetricValue"]{
    color:white !important;
}

/* ===========================
   Horizontal Line
=========================== */
hr{
    border:1px solid white !important;
}

/* ===========================
   Sidebar
=========================== */

/* Sidebar background */
section[data-testid="stSidebar"]{
    background-color: white !important;
}

/* Sidebar title, labels and text */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] h5,
section[data-testid="stSidebar"] h6,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div{
    color: black !important;
}

/* Sidebar input text */
section[data-testid="stSidebar"] input{
    color: black !important;
}

/* Sidebar selectbox */
section[data-testid="stSidebar"] div[data-baseweb="select"] > div{
    background: white !important;
    color: black !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] span{
    color: black !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] svg{
    fill: black !important;
}

</style>
""", unsafe_allow_html=True)


