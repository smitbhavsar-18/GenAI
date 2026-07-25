#Task 4: Mini Dashboard
import streamlit as st

st.title("Simple Sales Dashboard")

month = st.selectbox("Select a month", ["January", "February", "March", "April"])
sales  = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

st.metric(label=f"Sales in {month}", value=sales[month])

st.bar_chart(list(sales.values()))