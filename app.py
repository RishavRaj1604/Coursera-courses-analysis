import streamlit as st
import pandas as pd

st.set_page_config(page_title="Coursera Dashboard", layout="wide")

st.title("📊 Coursera Courses Analysis Dashboard")

# Load dataset
df = pd.read_csv("coursea_data.csv")

# Show data
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Charts
st.subheader("Course Difficulty Distribution")
if "difficulty" in df.columns:
    st.bar_chart(df["difficulty"].value_counts())

st.subheader("Ratings Distribution")
if "rating" in df.columns:
    st.bar_chart(df["rating"])

# Sidebar filter
st.sidebar.header("Filter")

if "difficulty" in df.columns:
    difficulty = st.sidebar.selectbox("Select Difficulty", df["difficulty"].unique())
    filtered_df = df[df["difficulty"] == difficulty]

    st.subheader(f"Filtered Data: {difficulty}")
    st.dataframe(filtered_df)
