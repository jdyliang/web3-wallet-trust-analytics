# Week 1 – Web3 Wallet Data Pipeline Prototype

This project builds a simple data pipeline to analyze blockchain wallet activity and extract behavioral features that may help identify trustworthy users.

The goal is to support a future Trust API that can estimate whether a wallet likely belongs to a real human user.

## Project Overview

This prototype retrieves wallet transaction data from the Ethereum blockchain using the Etherscan API and processes it using Python and pandas.

The pipeline performs:

- Wallet transaction retrieval
- Data cleaning and preprocessing
- Feature engineering
- Feature dataset generation

## Data Source

Transaction data is retrieved using the Etherscan API.

Example wallet analyzed:
- Vitalik Buterin wallet address

## Feature Engineering

The following wallet behavioral features are extracted:

- wallet_age_days
- tx_count
- tx_frequency
- avg_tx_value
- active_days
- first_tx
- last_tx

These features help characterize wallet activity patterns.

## Files

scripts/
- `week1_wallet_multi.py` – Python script that retrieves wallet transactions and generates features

data/
- `wallet_transactions_multi.csv` – cleaned transaction dataset
- `wallet_features_multi.csv` – extracted wallet feature dataset

docs/
- `schema.md` – dataset schema description
- `mvp_scope.md` – project MVP scope
- `architecture.md` – system architecture notes

## Technology Used

- Python
- Pandas
- Etherscan API
- Data pipeline scripting

## Future Work

Future steps may include:

- Designing a wallet trust scoring model
- Detecting bot-like activity patterns
- Building a Trust API for reputation signals
- Creating visualization dashboards

## Project Overview
This project analyzes blockchain wallet transaction data and generates behavioral features that can be used to estimate wallet trust and human likelihood.

The pipeline:
1. Extract wallet transactions from Etherscan API
2. Clean transaction dataset
3. Generate behavioral features
4. Export structured dataset
