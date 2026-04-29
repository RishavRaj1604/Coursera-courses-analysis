import streamlit as st
import pandas as pd

st.set_page_config(page_title="Coursera Analysis", layout="wide")

st.title("📊 Coursera Courses Analysis Dashboard")

# Load dataset
df = pd.read_csv("coursera_courses.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Basic stats
st.subheader("Course Difficulty Distribution")
st.bar_chart(df["difficulty"].value_counts())

st.subheader("Ratings Distribution")
st.bar_chart(df["rating"])

# Filters
st.sidebar.header("Filter")
difficulty = st.sidebar.selectbox("Select Difficulty", df["difficulty"].unique())

filtered_df = df[df["difficulty"] == difficulty]

st.subheader(f"Filtered Data: {difficulty}")
st.dataframe(filtered_df)
