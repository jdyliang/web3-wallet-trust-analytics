## Week3 - Trust Scoring Methodology

## Overview
In Week3, a rule-based trust scoring model was developed to evaluate Ethereum wallet based on behavioral features derived from transaction data. The goal of this model is to estimate the likelihood that a wallet represents a real human user rather than automated or bot-like activity.

## Input Data
The model uses a dataset of 200 wallets and their engineered features generated in Week2.
Each wallet is represented by behavioral metrics such as:
- Wallet age
- Transaction frequency
- Active days
- Counterparty diversity
- Stablecoin usage
- Activity consistency
- Burst transaction behavior

## Feature Signals

### Positive Signals (Increase Trust)
- Wallet Age ('walle_age_days')
- Active Days ('actoive_days')
- Unique Counterparties ('unique_counterparties')
- Stablecoin Usage ('stablecoin_tx_ratio')

### Negative Signals (Decrease Trust)
- Burst Activity ('max_tx_per_hour')
- Low Consistency ('consistency_ratio')
- High Transaction Frequency ('tx_frequency')

## Normalization
All features are normalized using min_max scaling to ensure comparability across different metrics.

## Trust Score Calculation
The trust score is computed using a weighted rule-based formula:

- Positive contributions:
    - wallet_age_score
    - active_days_score
    - counterparty_score
    - stablecoin_score
 
- Negative penalties:
    - burst_penalty
    - consistency_penalty
    - tx_frequency_penalty

The final score is scaled to a range of 0-100.

## Human Likelihood Classification
- High: score >= 70
- Medium: 40 <= score < 70
- Low: score < 40

## Trust Tier Classification
- Gold: score >= 75
- Silver: 45 <= score < 75
- Bronze: score < 45

## Observations
- Most wallets are classified as Low / Bronze
- Only a small number reach High / Gold

This suggests the model is conservative and favors strict filtering.

## Limitations
- No labeled ground truth
- Small dataset (200 wallets)
- Manually selected weights
- Some wallets lack token data

## Feature Improvements
- Tune scoring weights
- Expand dataset
- Apply machine learning models
- Add more behavioral features

## Conclusion
This rule-based model provides an interpretable baseline for evaluating wallet trustworthiness and can be extended in future iterations.
