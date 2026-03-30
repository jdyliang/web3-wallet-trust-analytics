import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("week3_wallet_scored.csv")

print("Loaded rows:", len(df))
print(df.head())

tier_counts = df["trust_tier"].value_counts()

plt.figure()
plt.bar(tier_counts.index, tier_counts.values)
plt.title("Trust Tier Distribution")
plt.xlabel("Trust Tier")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.savefig("week3_trust_tier_distribution.png")
plt.close()


human_counts = df["human_likelihood"].value_counts()

plt.figure()
plt.bar(human_counts.index, human_counts.values)
plt.title("Human Likelihood Distribution")
plt.xlabel("Human Likelikhood")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.savefig("week3_human_likelihood_distribution.png")
plt.close()

plt.figure()
plt.hist(df["trust_score"].dropna(), bins = 15)
plt.title("Trust Score Distribution")
plt.xlabel("Trust Score")
plt.ylabel("Number of Wallets")
plt.tight_layout()
plt.savefig("week3_trust_score_distribution.png")
plt.close()

tier_order = ["Bronze", "Silver", "Gold"]
data_by_tier = [
    df[df["trust_tier"] == tier] ["trust_score"].dropna()
    for tier in tier_order]

plt.figure()
plt.boxplot(data_by_tier, tick_labels = tier_order)
plt.title("Trust Score by Trust Tier")
plt.xlabel("Trust Tier")
plt.ylabel("Trust Score")
plt.tight_layout()
plt.savefig("week3_trust_score_by_tier.png")
plt.close()


print("\nSaved chart files:")
print("week3_trust_tier_distribution.png")
print("week3_human_likelihood_distribution.png")
print("week3_trust_score_distribution.png")
print("week3_trust_score_by_tier.png")
