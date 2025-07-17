import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Terrance Pai | IB & PE", layout="wide")

st.title("Terrance Pai")
st.markdown("Investment Management | Private Equity | Finance Enthusiast")

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["About Me", "Projects", "Finance Tools", "Contact"])

if menu == "About Me":
    st.header("About Me")
    st.write(
        """
        I am a rising senior passionate about Investment Banking and Private Equity,
        experienced in financial modeling, valuation, and strategic analysis.
        Skilled in Excel, Python, and corporate finance concepts.
        """
    )
    st.subheader("Key Skills")
    st.write(
        """
        - Financial Modeling (DCF, LBO, M&A)  
        - Valuation Techniques (Comps, Precedents, Multiples)  
        - Data Analysis (Python, Excel, SQL)
        """
    )

elif menu == "Projects":
    st.header("Smithfield Foods IPO Analysis (2025)")
    st.write(
        """
        **Highlights:**  
        - Projected revenue CAGR: 4.2% over 5 years  
        - EV/EBITDA multiple: 8.5x (in line with peer group)  
        - IPO valuation range: $6.8B – $7.5B  
        """
    )

    years = [2025, 2026, 2027, 2028, 2029]
    revenue = [16000, 16700, 17400, 18200, 19000]
    ebitda = [1800, 1900, 2000, 2100, 2200]
    df = pd.DataFrame({"Year": years, "Revenue ($M)": revenue, "EBITDA ($M)": ebitda})

    fig = px.line(df, x="Year", y=["Revenue ($M)", "EBITDA ($M)"], markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Finance Tools":
    st.header("DCF Calculator")
    wacc = st.number_input("WACC (%)", value=8.0)
    growth = st.number_input("Terminal Growth Rate (%)", value=2.0)
    fcf = st.number_input("Initial Free Cash Flow ($M)", value=500)
    years = st.slider("Projection Years", 3, 10, 5)

    if st.button("Calculate DCF Value"):
        discount_rate = wacc / 100
        term_growth = growth / 100
        pv = 0
        for i in range(1
