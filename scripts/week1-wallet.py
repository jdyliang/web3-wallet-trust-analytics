import requests
import pandas as pd
from datetime import datetime

API_KEY = "YOUR_API_KEY"

def get_wallet_transactions(wallet_address):
    url = "https://api.etherscan.io/v2/api"

    params = {
        "chainid": "1",
        "module": "account",
        "action": "txlist",
        "address": wallet_address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "1":
        print("No transactions found or API error.")
        print(data)
        return pd.DataFrame()

    return pd.DataFrame(data["result"])

wallet = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
df = get_wallet_transactions(wallet)
print(df.head())
print(df.columns)


df["timeStamp"] = df["timeStamp"].astype(int)
df["datetime"] = pd.to_datetime(df["timeStamp"], unit="s")
df["value"] = df["value"].astype(float)

df_clean = df[["hash", "from", "to", "value", "datetime"]]

print(df_clean.head())

def compute_wallet_features(df, wallet):
    if df.empty:
        return None
    first_tx = df["datetime"].min()
    last_tx = df["datetime"].max()
    wallet_age_days = (last_tx - first_tx).days
    tx_count = len(df)
    tx_frequency = tx_count / max(wallet_age_days, 1)
    avg_tx_value = df["value"].mean()
    active_days = df["datetime"].dt.date.nunique()
    return {
        "wallet": wallet,
        "first_tx": first_tx,
        "last_tx": last_tx,
        "wallet_age_days": wallet_age_days,
        "tx_count": tx_count,
        "tx_frequency": tx_frequency,
        "avg_tx_value": avg_tx_value,
        "active_days": active_days
        }

features = compute_wallet_features(df_clean, wallet)
feature_df = pd.DataFrame([features])

print(feature_df)

feature_df.to_csv("wallet_features.csv", index=False)
df_clean.to_csv("wallet_transactions_clean.csv", index=False)
