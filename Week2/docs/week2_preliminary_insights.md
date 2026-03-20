# Week 2 – Preliminary Insights

## Overview
In Week 2, I performed exploratory data analysis (EDA) on wallet transaction features to better understand behavioral patterns across different wallets.

## Key Observations

### 1. Wallet Age Distribution
- Most wallets are relatively young, with a few older wallets.
- This suggests a mix of new and established users in the dataset.

### 2. Transaction Frequency
- Transaction frequency varies significantly across wallets.
- Some wallets have extremely high activity, which may indicate automated behavior or bots.

### 3. Stablecoin Usage
- Most wallets have low stablecoin transaction ratios.
- A small number of wallets show high stablecoin usage, indicating specialized behavior (e.g., trading or arbitrage).

### 4. Wallet Age vs Transaction Frequency
- No clear linear relationship between wallet age and transaction frequency.
- Some newer wallets still exhibit very high activity levels.

### 5. Transaction Frequency vs Consistency
- Some wallets show high frequency but low consistency, indicating burst activity.
- Others maintain stable transaction patterns over time.

### 6. High Burst Wallets
- Identified wallets with very high transactions per hour/minute.
- These may represent bots or high-frequency trading accounts.

### 7. Stablecoin-heavy Wallets
- A subset of wallets heavily relies on stablecoins.
- These wallets may be associated with trading strategies or liquidity management.

## Next Steps
- Develop a wallet trust scoring model
- Detect bot-like patterns using burst and consistency features
- Explore clustering or classification models
