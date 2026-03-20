import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wallet_features_v2.csv")

print("Preview:")
print(df.head())

print("\nSummary:")
print(df.describe())

plt.figure()
plt.hist(df["wallet_age_days"].dropna())
plt.title("Wallet Age Distribution")
plt.xlabel("Days")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("wallet_age_distribution.png")
plt.close()

plt.figure()
plt.hist(df["tx_frequency"].dropna())
plt.title("Transaction Frequency")
plt.xlabel("Tx per day")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("tx_frequency_distribution.png")
plt.close()

plt.figure()
plt.hist(df["stablecoin_tx_ratio"].dropna())
plt.title("Stablecoin Ratio")
plt.xlabel("Ratio")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("stablecoin_ratio_distribution.png")
plt.close()

plt.figure()
plt.scatter(df["wallet_age_days"], df["tx_frequency"])
plt.xlabel("Wallet Age")
plt.ylabel("Tx Frequency")
plt.title("Age vs Frequency")
plt.tight_layout()
plt.savefig("wallet_age_vs_tx_frequency.png")
plt.close()

plt.figure()
plt.scatter(df["tx_frequency"], df["consistency_ratio"])
plt.xlabel("Tx Frequency")
plt.ylabel("Consitency Ratio")
plt.title("Frequency vs Consistency")
plt.tight_layout()
plt.savefig("tx_frequency_vs_consistency.png")
plt.close()

top_burst = df.sort_values("max_tx_per_hour", ascending = False)[
    ["wallet", "max_tx_per_hour", "max_tx_per_minute"]]

print("\nTop Burst Wallets:")
print(top_burst)

top_stablecoin = df.sort_values("stablecoin_tx_ratio", ascending = False)[[
    "wallet", "stablecoin_tx_ratio", "stablecoin_tx_count"]]
print("\nTio Stablecoin Wallets:")
print(top_stablecoin)

top_burst.to_csv("top_burst_wallets.csv", index = False)
top_stablecoin.to_csv("top_stablecoin_wallets.csv", index = False)

print("\nSaved image files:")
print("wallet_age_distribution.png")
print("tx_frequency_distribution.png")
print("stablecoin_ratio_distribution.png")
print("wallet_age_vs_tx_frequency.png")
print("tx_frequency_vs_consistency.png")

print("\nSaved CSV summary files:")
print("top_burst_wallets.csv")
print("top_stablecoin_wallets.csv")
