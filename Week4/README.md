# Week 4 — API & Dashboard

## Overview
In Week 4, I extended the wallet analytics system into a usable application layer by building an API and a dashboard.

## Components

### 1. API (FastAPI)
- Built a wallet trust API using FastAPI
- Allows querying a wallet address
- Returns structured trust evaluation

### 2. Proof JSON Output
- Designed a proof-style JSON response
- Includes:
  - human_likelihood
  - trust_tier
  - timestamp
  - version

### 3. Dashboard (Streamlit)
- Built a dashboard to visualize results
- Includes:
  - Trust tier distribution
  - Human likelihood distribution

## Output
- API endpoint: `/check?wallet=...`
- Dashboard: local Streamlit app

## Summary
This completes the end-to-end pipeline:
Data → Features → Model → API → Dashboard
