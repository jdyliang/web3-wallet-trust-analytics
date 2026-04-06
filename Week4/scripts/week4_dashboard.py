import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/judy/Desktop/Innovation AI/week 3/csv files/week3_wallet_scored.csv")

st.title("Wallet Trust Dashboard")

st.subheader("Data Preview")
st.write(df.head())


st.subheader("Trust Tier Distribution")
tier_counts = df["trust_tier"].value_counts()

fig, ax = plt.subplots()
tier_counts.plot(kind = "bar", ax = ax)
st.pyplot(fig)

st.subheader("Human Likelihood Distribution")
hl_counts = df["human_likelihood"].value_counts()

fig2, ax2 = plt.subplots()
hl_counts.plot(kind = "bar", ax = ax2)
st.pyplot(fig2)
