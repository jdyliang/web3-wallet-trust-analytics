## Week 3 - Wallet Trust Scoring Model

## Overview
In week 3, an end-to-end trust scoring system was developed to evaluate Ethereum wallets based on behavioral transaction patterns.

The goal of this project is to estimate the likelihood that a wallet belongs to a real human user and assign a corresponding trust level.

## Pipeline Summary
The full pipeline consists of three main steps:

### 1. Wallet Collection
- Sampled 200 Ethereum wallets using Etherscan API

### 2. Feature Engineering
- Extracted behavioral features from transaction data:
  - Wallet Age
  - Transaction frequency
  - Active days
  - Unique counterparties
  - Stablecoin Usage
  - Burst activity
  - Consistency metrics

### 3. Trust Scoring
- Applied a rule-based scoring model
- Generated:
  - Trust Score (0-100)
  - Human Likelihood (High / Medium / Low)
  - Trust Tier (Gold / Silver / Bronze)

## Project Structure
Week3/
  data/
      week3_wallet_list_200.csv
      week3_wallet_features.csv
  scripts/
      week3_get_wallets.py
      week3_features_engineering.py
      week3_trust_scoring.py
  outputs/
      week3_wallet_scored.csv
  docs/
      week3_methodology.md
      week3_evaluation.md

## Key Outputs

### Trust Score
A numerical score (0-100) that reflects wallet trustworthiness based on behavioral signals.

### Human Likelihood
- High: Likely a real user
- Medium: Mixed signals
- Low: Likely automated or bot-like

### Trust Tier
- Gold: Hight trust
- Silver: Moderate trust
- Bronze: Low trust

## Results Summary
- Most wallets were classified as Low / Bronze
- Only a small number achieved High / Gold

This indicates the model is currently conservative and prioritizes strict filtering.

## Key Insights
- Wallets with long history and consistent activity tend to score higher
- High burst activity is a strong indicator of bot-like behavior
- Diverse counterparties are associated with more human-like usage
- Stablecoin usage contributes positively but is not dominant

## Limitations
- No labeled ground truth for validation
- Small sample size (200 wallets)
- Manually tuned scoring weights
- Some wallets lack token transaction data

## Future Improvements
- Tune scoring thresholds and weights
- Expand dataset size
- Introduce machine learning models
- Add more behavioral features
- Validate against labeled datasets

## Conclusion
This project demosntrate a complete pipeline for wallet trust evaluation using interpretable, rule-based methods.

The system provides a strong foundation for future enhancements, including data-driven modeling and real-world deployment scenarios.
