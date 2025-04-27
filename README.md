# Bank Churning Analysis

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

This project analyzes customer churn for a banking institution. Using a dataset of customer demographics and account information, the goal is to uncover trends, visualize customer behavior, and support data-driven decision-making to reduce churn rates.

## 📁 Project Structure

- `app.py` — Streamlit dashboard application for interactive data exploration.
- `bank_churning_analysis.ipynb` — Jupyter Notebook with detailed exploratory data analysis and statistical insights.
- `summary_report.pdf` — Executive summary report outlining key findings and recommendations.
- `requirements.txt` — Python package dependencies.
- `.gitignore` — Git configuration to ignore unnecessary files.

## ✨ Key Features

- **Exploratory Data Analysis (EDA):**  
  Comprehensive analysis of customer demographics, account activity, and churn distribution.

- **Visualization:**  
  - Customer distribution by country.
  - Demographics (age, gender, income) visualizations.
  - Churn patterns and risk segmentation.

- **Dashboard Application:**  
  A user-friendly Streamlit dashboard to interactively explore insights and monitor churn risk indicators.
  ![Dashboard Overview](/Bank_churn_project/Dashboard_jpeg.jpg)

- **Prediction and Customer Classification:**  
  - Sklearn library was used to label-encode, standardize, split the dataset into train and test sets.
  - Classifying and assessing the classification report.
  - Clustering visualization using seaborn and matplotlib.

## 🚀 Live Dashboard

> **[Click here to view the live Streamlit app](https://bank-churn-analysis-l2ekffyex35m4jxwkfevv3.streamlit.app/)**  

If you haven't deployed the app yet, you can still run it locally by following the instructions below.

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Streamlit
- Scikit-learn
- Jupyter Notebook

## ⚙️ Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## 📊 Project Highlights

- Data cleaning and preprocessing for accurate analysis.
- Visual insights on customer demographics and account behavior.
- Business-driven summary report with actionable insights.
- Interactive web app for real-time data exploration.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✍️ Author

**Fehintolu Samuel**
