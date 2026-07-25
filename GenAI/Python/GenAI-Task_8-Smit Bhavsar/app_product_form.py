#Task 3 : Product Form

import streamlit as st

st.sidebar.title("Product Form")
product_name = st.sidebar.text_input("Enter product name", key="product_name")  
category = st.sidebar.selectbox("Enter product category", ["Electronics", "Clothing", "Books"], key="category")
price = st.sidebar.number_input("Enter product price", min_value=0.0, step=1.0, key="price")

if(st.sidebar.button("Add Product")):
    st.sidebar.success("Product submitted successfully!")
    st.write(f"Product Name: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price: {price}")