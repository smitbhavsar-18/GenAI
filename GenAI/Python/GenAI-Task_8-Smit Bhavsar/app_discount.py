#Task 2: Price Discount Calculator
import streamlit as st

product_price = st.number_input("Enter the product price", min_value=0.0, step=0.01)
discount_percent = st.slider("Select discount percentage", min_value=0, max_value=50, step=10)

if st.button("Calculate Discounted Price"):
    discounted_price = product_price * (1 - discount_percent / 100)
    st.success(f"Discounted Price: {discounted_price:.2f}")
    st.table({
        "Before": [product_price], "After": [discounted_price]
    })
