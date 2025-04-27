import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

# 🚨 FIRST Streamlit command
st.set_page_config(layout="wide")

# Now you can start your app
st.title('📊 Bank Churn Full Dashboard')

# Try loading the data
csv_path = 'cleaned_bank_churn_analysis.csv'
df = pd.read_csv(uploaded_file)

#st.title("Upload CSV file")
#uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# ------------------- SECTION 1: Demographics -------------------
