# 🏦 Loan Approval Prediction using Machine Learning

A Machine Learning project that predicts whether a loan application will be **approved or rejected** based on applicant financial and demographic information.

This project uses classification algorithms to analyze borrower data and estimate **loan default risk**, helping financial institutions make better lending decisions.

---

## 🚀 Live Demo

🔗 **Try the deployed Streamlit app here:**
https://loanapproval-sgpxjybmqzehv2yjnftqxu.streamlit.app/

---

## 📌 Project Overview

Loan approval is a crucial decision for financial institutions. Incorrect approval can lead to financial loss due to loan defaults.

This project builds a **machine learning model** that predicts the loan approval outcome based on several applicant attributes such as:

* Age
* Income
* Employment Experience
* Credit Score
* Loan Amount
* Loan Intent
* Credit History

The final model is deployed as an interactive **Streamlit web application**.

---

## 📂 Project Structure

```
Loan_Approval
│
├── app.py                 # Streamlit web application
├── requirements.txt       # Project dependencies
├── model.pkl              # Trained ML model
├── Loan_Approval.ipynb    # Jupyter notebook for analysis
└── README.md              # Project documentation
```

---

## 📊 Dataset Features

| Feature                        | Description                             |
| ------------------------------ | --------------------------------------- |
| person_age                     | Age of the loan applicant               |
| person_income                  | Annual income of the applicant          |
| person_emp_exp                 | Years of employment experience          |
| loan_amnt                      | Loan amount requested                   |
| loan_int_rate                  | Interest rate of the loan               |
| loan_percent_income            | Loan amount relative to income          |
| credit_score                   | Applicant credit score                  |
| loan_intent                    | Purpose of the loan                     |
| person_home_ownership          | Home ownership status                   |
| previous_loan_defaults_on_file | Previous loan default history           |
| loan_status                    | Target variable (loan approval outcome) |

---

## ⚙️ Machine Learning Workflow

The project follows a structured machine learning pipeline:

1. Data Exploration (EDA)
2. Data Cleaning
3. Feature Selection
4. Categorical Encoding
5. Outlier Removal
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Deployment using Streamlit

---

## 🤖 Algorithms Used

* Naive Bayes
* Logistic Regression
* Random Forest
* K-Nearest Neighbors (KNN)

These models were compared to determine the best-performing algorithm.

---

## 📈 Model Evaluation

Performance was evaluated using:

* Accuracy
* Confusion Matrix
* Classification Report

---

## 🖥️ Streamlit Application

The Streamlit app allows users to:

* Input applicant information
* Predict loan approval status
* Interact with the machine learning model in real time

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Seaborn
* Matplotlib
* Streamlit

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/KrAtulHub/Loan_Approval.git
cd Loan_Approval
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Atul Kumar Prasad**

* GitHub: https://github.com/KrAtulHub
* LinkedIn: Add your LinkedIn profile here

---

## ⭐ If you like this project

Give the repository a **star ⭐** to support the project!
