import pandas as pd
import numpy as np

df = pd.read_csv("week3_wallet_features.csv")

print("Loaded rows:", len(df))
print(df.head())

def min_max_scale(series):
    series = pd.to_numeric(series, errors = "coerce").fillna(0)

    min_val = series.min()
    max_val = series.max()

    if max_val == min_val:
        return pd.Series([0.0] * len(series), index = series.index)

    return(series - min_val) / (max_val - min_val)


df["wallet_age_score"] = min_max_scale(df["wallet_age_days"])
df["active_days_score"] = min_max_scale(df["active_days"])
df["counterparty_score"] = min_max_scale(df["unique_counterparties"])
df["stablecoin_score"] = min_max_scale(df["stablecoin_tx_ratio"])

df["burst_penalty"] = min_max_scale(df["max_tx_per_hour"])
df["consistency_penalty"] = min_max_scale(df["consistency_ratio"])

df["tx_freq_penalty"] = min_max_scale(df["tx_frequency"])

df["trust_score_raw"] = (
    0.30 * df["wallet_age_score"] +
    0.25 * df["active_days_score"] +
    0.20 * df["counterparty_score"] +
    0.10 * df["stablecoin_score"] +
    0.10 * df["burst_penalty"] +
    0.03 * df["consistency_penalty"] +
    0.02 * df["tx_freq_penalty"]
    )

trust_min = df["trust_score_raw"].min()
trust_max = df["trust_score_raw"].max()

if trust_max == trust_min:
    df["trust_score"] = 50
else:
    df["trust_score"] = (
        (df["trust_score_raw"] - trust_min) / (trust_max - trust_min) *100).round(2)


def human_likelihood_label(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"

df["human_likelihood"] = df["trust_score"].apply(human_likelihood_label)


def trust_tier_label(score):
    if score >= 75:
        return "Gold"
    elif score >= 45:
        return "Silver"
    else:
        return "Bronze"

df["trust_tier"] = df["trust_score"].apply(trust_tier_label)


final_cols = [
    "wallet",
    "wallet_age_days",
    "tx_count",
    "tx_frequency",
    "active_days",
    "unique_counterparties",
    "stablecoin_tx_ratio",
    "max_tx_per_hour",
    "consistency_ratio",
    "trust_score",
    "human_likelihood",
    "trust_tier"
    ]

scored_df = df[final_cols].copy()

scored_df.to_csv("week3_wallet_scored.csv", index = False)

print("\nDone.")
print("Saved file: week3_wallet_scored.csv")

print("\nPreview:")
print(scored_df.head())

print("\nHuman Likelihood distribution:")
print(scored_df["human_likelihood"].value_counts())

print("\nTrust Tier distribution:")
print(scored_df["trust_tier"].value_counts())
    
