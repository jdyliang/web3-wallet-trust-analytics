## Week 3 - Model Evaluation

## Overview
This evaluation assesses the performance and behavior of the rule-based trusting scoring model developed in Week 3.

The model assigns each wallet a numerical trust score (0-100), along with two categorical outputs:
- Human Likelihood(High / Medium / Low)
- Trust Tier (Gold / Silver / Bronze)

## Data Summary
- Total wallets analyzed: 200
- Data source: Ethereum transaction data via Etherscan API
- Features: behavioral metrics derived from transaction patterns

## Results
### Human Likelihood Distribution
- Low: 188 wallets
- Medium: 11 wallets
-  High: 1 wallet

### Trust Tier Distribution
- Bronze: 191 wallets
- Silver: 8 wallets
- Gold: 1 wallet

## Key Observations
### 1. Strong Class Imbalance
The majority of wallets fall into the Low / Bronze category.
This suggests:
- The model is highly conservative
- Only wallets with strong behavioral signals are classified as trustworthy

### 2. Strict Filtering Behavior
The scoring system emphasizes:
- Low wallet history
- Consistency activity over time
- Diverse interactions with counterparties

Wallets lacking these characteristics are heavily penalized.

### 3. Detection of Potential Bot Activity
Wallets with:
- High burst activity
- Low consistency
- Extremely high transaction frequency

are consistently assigned low trust scores.

This indicated the model is effective at identifying bot-like behavior patterns.

### 4. Limited High-Trust Wallets
Only a very small number of wallets are classified as:
- High Human Likelihood
- Gold Tier

This suggests: 
- Either truly high-quality wallets are rare in the sample
- Or the scoring thresholds are too strict

## Model Strengths
- Interpretable
  Each component of the score has a clear meaning
- Behavior-driven
  Relies on real transaction patterns instead of arbitrary labels
- Robust to missing token data
  Handles wallets without token transfers gracefully

## Model Limitations
- No Gound Truth Labels
  Cannot directly measure accuracy or precision
- Manual Weight Selection
  Feature weights are heuristic and not optimized
- Small Sample Size
  Only 200 wallets analyzed
- Conservative Bias
  Model favors low-risk classification (may reduce recall)

## Recommendations for Improvement
### 1. Threshold Tuning
Adjust classification thresholds to achieve a more balanced distribution.

### 2. Feature Weight Optimization
Use data-driven methods (e.g., regression or ML models) to determine optimal weights.

### 3. Larger Dataset
Expand analysis to thousands of wallets to improve robustness.

### 4. Supervised Learning
Introduce labeled datasets to train classification models.

### 5. Additional Featurs
Consider adding:
- Time between transactions
- Token diversity
- Gas usage patterns
- DeFi interaction signals

## Concluion
The rule-based trust scoring model provides a strong baseline for evaluating wallet behavior.

While the model currently produces conservative results, it successfully captures key behavioral differences between normal and potentially automated wallets.

Future iterations should focus on:
- Improving balance
- Incorporating machine learning
- Expanding data coverage
