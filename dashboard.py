import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 E-commerce Price Intelligence Dashboard")

# Load dataset
df = pd.read_csv("products.csv")

# Sidebar Filters
st.sidebar.header("Filters")

# Rating Filter
ratings = df["Rating"].unique()
selected_rating = st.sidebar.multiselect(
    "Select Rating",
    ratings,
    default=ratings
)

# Price Filter
min_price = int(df["Price"].min())
max_price = int(df["Price"].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

# Apply Filters
filtered_df = df[
    (df["Rating"].isin(selected_rating)) &
    (df["Price"] >= price_range[0]) &
    (df["Price"] <= price_range[1])
]

# Dataset Preview
st.subheader("📋 Filtered Dataset")
st.dataframe(filtered_df)

# Charts Section
st.subheader("📈 Price Distribution")

fig, ax = plt.subplots()
filtered_df["Price"].hist(ax=ax)
st.pyplot(fig)

# Statistics
st.subheader("📊 Statistics")

st.write("Average Price:", filtered_df["Price"].mean())
st.write("Total Products:", len(filtered_df))
# Product Search System
st.subheader("🔍 Product Search")

search_text = st.text_input("Search Product Title")

if search_text:
    search_result = df[df["Title"].str.contains(search_text, case=False, na=False)]
    st.dataframe(search_result)