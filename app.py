# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="News Sentiment", layout="wide")
st.title("Real-Time News Sentiment Dashboard")

# Load CSV
df = pd.read_csv("news_sentiment.csv")

# Show summary
st.subheader("Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

# Show detailed data
st.subheader("News Articles and Sentiment")
st.dataframe(df)
