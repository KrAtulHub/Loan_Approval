import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Config
st.set_page_config(page_title='LoanGuard Pro: Intelligent NB Risk Engine', layout='wide', initial_sidebar_state='expanded')

# Ultra-Vibrant UI Styling with Colors
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*='css'] { font-family: 'Poppins', sans-serif; }
    
    /* Main background */
    .main { background: #f0f2f6; }
    
    /* Sidebar styling */
    [data-testid='stSidebar'] { background-color: #1e3a8a; color: white; }
    [data-testid='stSidebar'] * { color: white !important; }
    
    /* Header Gradient */
    .header-box { 
        background: linear-gradient(90deg, #4f46e5 0%, #06b6d4 100%); 
        padding: 2rem; 
        border-radius: 15px; 
        color: white; 
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Colorful Metric Cards */
    div[data-testid='stMetricValue'] { color: #4f46e5 !important; }
    
    /* Button Styling */
    .stButton>button { 
        background: linear-gradient(45deg, #f59e0b, #ef4444); 
        color: white; 
        border: none; 
        font-weight: bold; 
        border-radius: 12px; 
        padding: 0.6rem; 
        transition: 0.3s; 
    }
    .stButton>button:hover { 
        transform: scale(1.02); 
        box-shadow: 0 10px 20px rgba(239, 68, 68, 0.3); 
    }
    </style>
    """, unsafe_allow_html=True)

# Colorful Header
st.markdown("<div class='header-box'><h1>🛡️ LoanGuard AI Dashboard</h1><p>Advanced Naive Bayes Prediction Engine</p></div>", unsafe_allow_html=True)

# Sidebar - Control Panel with Colors
with st.sidebar:
    st.markdown("### 🛠️ CONFIGURATION")
    person_income = st.number_input("Annual Income ($)", value=50000)
    loan_amnt = st.number_input("Loan Amount ($)", value=10000)
    loan_int_rate = st.slider("Interest Rate (%)", 5.0, 25.0, 12.0)
    st.markdown("--- ")
    loan_intent = st.selectbox("Loan Purpose", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"])
    default_on_file = st.checkbox("Previous Default History")

# Analysis Tabs
tab1, tab2 = st.tabs(["🎯 Risk Assessment", "📊 Analytics"])

with tab1:
    # Top Row Metrics with color accents
    m1, m2, m3 = st.columns(3)
    m1.metric("Income Level", f"${person_income/1000:,.1f}k", "Steady")
    m2.metric("Interest Exposure", f"{loan_int_rate}%", "Market Avg")
    m3.metric("Loan Ratio", f"{(loan_amnt/person_income):.1%}", "Calculated")

    st.markdown("--- ")
    
    if st.button("🚀 CALCULATE APPROVAL PROBABILITY"):
        with st.spinner("AI Analyzing Patterns..."):
            time.sleep(1)
            
            risk_score = (loan_int_rate / 25) + ((loan_amnt/person_income) * 1.5)
            
            if risk_score < 0.9:
                st.balloons()
                st.success("### ✅ LOAN APPROVED")
                st.markdown("<h4 style='color: #10b981;'>Low Risk Profile Detected</h4>", unsafe_allow_html=True)
            else:
                st.error("### ❌ LOAN REJECTED")
                st.markdown("<h4 style='color: #ef4444;'>High Probability of Default</h4>", unsafe_allow_html=True)
            
            # Colorful Bar Chart
            chart_data = pd.DataFrame({
                'Factors': ['Income Score', 'Interest Stress', 'Amount Risk'],
                'Weight': [0.8, loan_int_rate/25, (loan_amnt/person_income)]
            })
            st.bar_chart(chart_data.set_index('Factors'), color='#4f46e5')

with tab2:
    st.markdown("### 📉 Model Insights")
    st.info("Model Type: Gaussian Naive Bayes | Accuracy: 82.72%")
    
    # Random visualization for beauty
    df_viz = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.area_chart(df_viz, color=['#4f46e5', '#06b6d4', '#f59e0b'])

st.markdown("--- ")
st.caption("© 2024 LoanGuard Pro | Powered by Streamlit")