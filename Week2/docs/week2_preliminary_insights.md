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

## Additional Insights (Behabioral Patterns)
From the exploratory analysis, several behavioral patterns can be observed:

### 1. High Burst Activity
Some wallets exhibit extremely high transaction counts within short time periods. This may indicate automated or bot-like behavior.

### 2. Low Activity Consistency
Wallets with irregular transactions timing (long gaps followed by sudden spikes) tend to have low activity consistency, which can also non-human activity.

### 3. Stablecoin Usage Patterns
Wallets with a high proportion of stablecoin transactions may be engaged in trading, arbitrage, or liquidity-related strategies rather than typical user behavior.

### 4. Transaction Frequency vs Age
Older wallets do not necessarily have higher transaction frequency. Some newer wallets show unsually high activity, which may indicate scripted usage.

### 5. Potential Bot Indicators
A combination of:
- high tx_frequency
- high burst_ratio
- low diverisity (few counterparties)

may sugest bot-like wallets.

These patterns can be used aas inputs for a future wallet trust scoring model. 


## Next Steps
- Develop a wallet trust scoring model
- Detect bot-like patterns using burst and consistency features
- Explore clustering or classification models
