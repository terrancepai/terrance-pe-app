import streamlit as st
import plotly.express as px
import pandas as pd

# ----------------- CONFIG -----------------
st.set_page_config(page_title="Terrance Pai | IB & PE", layout="wide")

# Custom theme colors
primary_color = "#000000"
secondary_color = "#f5f5f5"
accent_color = "#4A90E2"

# ----------------- HEADER -----------------
st.markdown("""
    <style>
        .main-header {text-align:center; font-size:48px; font-weight:bold; color:black;}
        .sub-header {text-align:center; font-size:20px; color:gray; margin-bottom:20px;}
        .button-container {text-align:center; margin-top:15px;}
        .stButton>button {background-color:black; color:white; border-radius:8px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Terrance Pai</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Investment Management | Private Equity | Finance Enthusiast</div>', unsafe_allow_html=True)

st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("Connect on LinkedIn"):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://www.linkedin.com/in/terrancepai/" />', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- SIDEBAR NAV -----------------
menu = st.sidebar.radio("Navigation", ["About Me", "Projects", "Finance Tools", "Contact"])

# ----------------- ABOUT ME -----------------
if menu == "About Me":
    st.header("About Me")
    st.write("""
        I am a rising senior passionate about Investment Banking and Private Equity, with experience in financial modeling, valuation, and strategic analysis.
        Skilled in Excel, Python, and corporate finance concepts, I aim to create value by combining analytical rigor with strategic thinking.
    """)
    st.subheader("Key Skills")
    st.write("- Financial Modeling (DCF, LBO, M&A)")
    st.write("- Valuation Techniques (Comps, Precedents, Multiples)")
    st.write("- Data Analysis (Python, Excel, SQL)")

# ----------------- PROJECTS -----------------
if menu == "Projects":
    st.header("Smithfield Foods IPO Analysis (2025)")

    st.write("""
    **Highlights:**
    - Projected revenue CAGR: **4.2%** over 5 years
    - EV/EBITDA multiple: **8.5x** (in line with peer group)
    - IPO valuation range: **$6.8B – $7.5B**
    """)

    # Sample financial data for visualization
    years = [2025, 2026, 2027, 2028, 2029]
    revenue = [16000, 16700, 17400, 18200, 19000]
    ebitda = [1800, 1900, 2000, 2100, 2200]

    df = pd.DataFrame({"Year": years, "Revenue ($M)": revenue, "EBITDA ($M)": ebitda})

    st.subheader("Revenue & EBITDA Forecast")
    fig = px.line(df, x="Year", y=["Revenue ($M)", "EBITDA ($M)"], markers=True, title="Revenue & EBITDA Projection")
    fig.update_layout(template="simple_white")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Valuation Multiples")
    multiples_df = pd.DataFrame({
        "Company": ["Smithfield Foods", "Tyson Foods", "Hormel"],
        "EV/EBITDA": [8.5, 9.2, 10.1]
    })
    fig2 = px.bar(multiples_df, x="Company", y="EV/EBITDA", text="EV/EBITDA", title="Comparable EV/EBITDA Multiples", color="Company")
    st.plotly_chart(fig2, use_container_width=True)

# ----------------- FINANCE TOOLS -----------------
if menu == "Finance Tools":
    st.header("Valuation & LBO Tools")

    st.subheader("DCF Calculator")
    wacc = st.number_input("WACC (%)", value=8.0)
    growth = st.number_input("Terminal Growth Rate (%)", value=2.0)
    fcf = st.number_input("Initial Free Cash Flow ($M)", value=500)
    years = st.slider("Projection Years", 3, 10, 5)

    if st.button("Calculate DCF Value"):

        discount_rate = wacc / 100
        term_growth = growth / 100
        pv = 0
        for i in range(1, years + 1):
            pv += fcf / ((1 + discount_rate) ** i)
        terminal_value = (fcf * (1 + term_growth)) / (discount_rate - term_growth)
        terminal_pv = terminal_value / ((1 + discount_rate) ** years)
        enterprise_value = pv + terminal_pv
        st.success(f"Estimated Enterprise Value: ${enterprise_value:,.0f}M")

    st.subheader("LBO Return Estimator")
    entry_price = st.number_input("Entry Price ($M)", value=1000)
    exit_price = st.number_input("Exit Price ($M)", value=1500)
    debt = st.number_input("Debt ($M)", value=500)
    equity = entry_price - debt
    years_lbo = st.slider("Holding Period (Years)", 3, 7, 5)

    if st.button("Calculate LBO IRR"):

        equity_exit = exit_price - debt
        irr = ((equity_exit / equity) ** (1 / years_lbo)) - 1
        st.success(f"Estimated IRR: {irr * 100:.2f}%")

# ----------------- CONTACT -----------------
if menu == "Contact":
    st.header("Contact")
    st.write("Email: terrancepai@gmail.com")
    st.write("LinkedIn: [Connect Here](https://www.linkedin.com/in/terrancepai/)")
