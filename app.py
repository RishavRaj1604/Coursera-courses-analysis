import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Coursera Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>📊 Coursera Courses Analytics Dashboard</h1>", unsafe_allow_html=True)

# Load data
df = pd.read_csv("coursea_data.csv")

# Clean data
df = df.dropna()

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Courses", len(df))
col2.metric("Unique Providers", df["course_organization"].nunique())
col3.metric("Avg Rating", round(df["course_rating"].mean(), 2))

st.markdown("---")

# Layout
col1, col2 = st.columns(2)

# Difficulty chart
with col1:
    st.subheader("📚 Course Difficulty Distribution")
    fig1 = px.histogram(df, x="course_difficulty", color="course_difficulty")
    st.plotly_chart(fig1, use_container_width=True)

# Rating chart
with col2:
    st.subheader("⭐ Course Ratings Distribution")
    fig2 = px.histogram(df, x="course_rating")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Top organizations
st.subheader("🏫 Top Course Providers")
top_org = df["course_organization"].value_counts().head(10)
fig3 = px.bar(top_org, x=top_org.values, y=top_org.index, orientation='h')
st.plotly_chart(fig3, use_container_width=True)

# Sidebar filter
st.sidebar.header("🔍 Filter")

difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    df["course_difficulty"].unique()
)

filtered_df = df[df["course_difficulty"] == difficulty]

st.subheader(f"📌 Courses: {difficulty}")
st.dataframe(filtered_df.head(20))
