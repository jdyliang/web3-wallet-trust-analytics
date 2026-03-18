import requests
import pandas as pd
from datetime import datetime
import time

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
        print(f"API error for {wallet_address}")
        print(data)
        return pd.DataFrame()

    return pd.DataFrame(data["result"])

def clean_transactions(df):
    if df.empty:
        return pd.DataFrame()

    df["timeStamp"] = df["timeStamp"].astype(int)
    df["datetime"] = pd.to_datetime(df["timeStamp"], unit="s")
    df["value"] = df["value"].astype(float)

    return df[["hash", "from", "to", "value", "datetime"]]

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

wallet_list = [
    "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "0x66f820a414680b5bcda5eeca5dea238543f42054"
]

all_features = []
all_transactions = []

for wallet in wallet_list:
    print(f"Processing {wallet}...")
    raw_df = get_wallet_transactions(wallet)
    clean_df = clean_transactions(raw_df)

    if not clean_df.empty:
        features = compute_wallet_features(clean_df, wallet)
        if features:
            all_features.append(features)

        clean_df["wallet"] = wallet
        all_transactions.append(clean_df)

    time.sleep(0.3)

feature_df = pd.DataFrame(all_features)

if all_transactions:
    transactions_df = pd.concat(all_transactions, ignore_index=True)
else:
    transactions_df = pd.DataFrame()

print(feature_df)
print(transactions_df.head())

feature_df.to_csv("wallet_features_multi.csv", index=False)
transactions_df.to_csv("wallet_transactions_multi.csv", index=False)
    

