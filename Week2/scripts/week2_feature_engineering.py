import requests
import pandas as pd
import time
from datetime import datetime

API_KEY = "YOUR_API_KEY"
wallet_list = ["0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb7",
    "0x66f820a414680b5bcda5eeca5dea238543f42054",
    "0xfe9e8709d3215310075d67e3ed32a380ccf451c8",
    "0x28c6c06298d514db089934071355e5743bf21d60",
    "0x564286362092d8e7936f0549571a803b203aaced",
    "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
    "0xf977814e90da44bfa03b6295a0616a897441acec",
    "0x3f5ce5fbfe3e9af3971dD833D26BA9b5C936f0bE",
    "0xdc76cd25977e0a5ae17155770273ad58648900d3"
               ]

STABLECOIN_ADDRESSES = [
    "0xdac17f958d2ee523a2206206994597c13d831ec7", 
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", 
    "0x6b175474e89094c44da98b954eedeac495271d0f"
    ]

def get_normal_transactions(wallet_address):
    url = "https://api.etherscan.io/v2/api"

    params = {
        "chainid": "1",
        "module": "account",
        "action": "txlist",
        "address": wallet_address,
        "starblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": API_KEY
        }

    response = requests.get(url, params = params, timeout = 30)
    data = response.json()

    if data.get("status") != "1":
        print("[WARN] Normal tx API issue for", wallet_address)
        print(data)
        return pd.DataFrame()

    return pd.DataFrame(data["result"])

def get_token_transfers(wallet_address):
    url = "https://api.etherscan.io/v2/api"

    params = {
        "chainid": "1",
        "module": "account",
        "action": "tokentx",
        "address": wallet_address,
        "starblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": API_KEY
        }

    response = requests.get(url, params = params, timeout = 30)
    data = response.json()

    if data.get("status") != "1":
        print("[WARN] Token tx API issue for", wallet_address)
        print(data)
        return pd.DataFrame()

    return pd.DataFrame(data["result"])

def clean_normal_transactions(df, wallet):
    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    df["wallet"] = wallet
    df["timeStamp"] = pd.to_numeric(df["timeStamp"], errors = "coerce")
    df["datetime"] = pd.to_datetime(df["timeStamp"], unit = "s", errors = "coerce")
    df["value"] = pd.to_numeric(df["value"], errors = "coerce")
    df["gasPrice"] = pd.to_numeric(df["gasPrice"], errors = "coerce")
    df["gasUsed"] = pd.to_numeric(df["gasUsed"], errors = "coerce")

    df["from"] = df["from"].astype(str).str.lower()
    df["to"] = df["to"].astype(str).str.lower()

    keep_cols = [
        "wallet",
        "hash",
        "from",
        "to",
        "value",
        "gasPrice",
        "gasUsed",
        "datetime" ]

    df = df[keep_cols]
    df = df.dropna(subset = ["datetime"])

    return df

def clean_token_transfers(df, wallet):
    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    df["wallet"] = wallet
    df["timeStamp"] = pd.to_numeric(df["timeStamp"], errors = "coerce")
    df["datetime"] = pd.to_datetime(df["timeStamp"], unit = "s", errors = "coerce")
    df["contractAddress"] = df["contractAddress"].astype(str).str.lower()
    df["from"] = df["from"].astype(str).str.lower()
    df["to"] = df["to"].astype(str).str.lower()

    keeps_cols = [
        "wallet",
        "hash",
        "from",
        "to",
        "contractAddress",
        "tokenSymbol",
        "datetime"
        ]

    df = df[keeps_cols]
    df = df.dropna(subset = ["datetime"])

    return df


def compute_wallet_features(normal_df, token_df, wallet):
    if normal_df.empty:
        return None

    normal_df = normal_df.copy()

    first_tx = normal_df["datetime"].min()
    last_tx = normal_df["datetime"].max()

    wallet_age_days = (last_tx - first_tx).days
    if wallet_age_days < 1:
        wallet_age_days = 1

    tx_count = len(normal_df)
    tx_frequency = tx_count / wallet_age_days
    avg_tx_value = normal_df["value"].mean()
    active_days = normal_df["datetime"].dt.date.nunique()

    normal_df["date"] = normal_df["datetime"].dt.date
    tx_per_day = normal_df.groupby("date").size()

    tx_per_day_mean = tx_per_day.mean()
    if len(tx_per_day) > 1:
        tx_per_day_std = tx_per_day.std()
    else:
        tx_per_day_std = 0

    if tx_per_day_mean > 0:
        consistency_ratio = tx_per_day_std / tx_per_day_mean
    else:
        consistency_ratio = 0

    normal_df["hour"] = normal_df["datetime"].dt.floor("h")
    tx_per_hour =normal_df.groupby("hour").size()
    max_tx_per_hour = tx_per_hour.max()

    normal_df["minute"] = normal_df["datetime"].dt.floor("min")
    tx_per_minute = normal_df.groupby("minute").size()
    max_tx_per_minute = tx_per_minute.max()

    unique_to_addresses = normal_df["to"].nunique()
    unique_from_addresses = normal_df["from"].nunique()

    combined_addresses = pd.concat([normal_df["from"], normal_df["to"]])
    unique_counterparties = combined_addresses.nunique()

    if token_df.empty:
        stablecoin_tx_count = 0
        total_token_tx_count = 0
        stablecoin_tx_ratio = 0
    else:
        total_token_tx_count = len(token_df)
        stablecoin_tx_count = token_df["contractAddress"].isin(STABLECOIN_ADDRESSES).sum()

        if total_token_tx_count > 0:
            stablecoin_tx_ratio = stablecoin_tx_count / total_token_tx_count
        else:
            stablecoin_tx_ratio = 0

        return {
            "wallet": wallet,
            "first_tx": first_tx,
            "last_tx": last_tx,
            "wallet_age_days": wallet_age_days,
            "tx_count": tx_count,
            "tx_frequency": tx_frequency,
            "avg_tx_value": avg_tx_value,
            "active_days": active_days,
            "tx_per_day_mean": tx_per_day_mean,
            "tx_per_day_std": tx_per_day_std,
            "consistency_ratio": consistency_ratio,
            "max_tx_per_hour": max_tx_per_hour,
            "max_tx_per_minute": max_tx_per_minute,
            "unique_to_addresses": unique_to_addresses,
            "unique_from_addresses": unique_from_addresses,
            "unique_counterparties": unique_counterparties,
            "stablecoin_tx_count": stablecoin_tx_count,
            "stablecoin_tx_ratio": stablecoin_tx_ratio
            }


all_normal_tx = []
all_token_tx = []
all_features = []

for wallet in wallet_list:
    print("Processing wallet:", wallet)

    normal_raw = get_normal_transactions(wallet)
    normal_clean = clean_normal_transactions(normal_raw, wallet)

    token_raw = get_token_transfers(wallet)
    token_clean = clean_token_transfers(token_raw, wallet)

    if not normal_clean.empty:
        all_normal_tx.append(normal_clean)

        if not token_clean.empty:
            all_token_tx.append(token_clean)

            features = compute_wallet_features(normal_clean, token_clean, wallet)
            if features is not None:
                all_features.append(features)

        time.sleep(0.4)

if len(all_normal_tx) > 0:
    transactions_df = pd.concat(all_normal_tx, ignore_index = True)
else:
    transactions_df = pd.DataFrame()

if len(all_token_tx) > 0:
    token_transactions_df = pd.concat(all_token_tx, ignore_index = True)
else:
    token_transactions_df = pd.DataFrame()

features_df = pd.DataFrame(all_features)

transactions_df.to_csv("wallet_transactions_multi.csv", index = False)
token_transactions_df.to_csv("wallet_token_transfers_multi.csv", index = False)
features_df.to_csv("wallet_features_v2.csv", index = False)

print("\nDone.")
print("Saved files:")
print("wallet_transactions_muilti.csv")
print("wallet_token_transfers_mulri.csv")
print("wallet_features_v2.csv")

print("\nFeature preview:")
print(features_df.head())


    
        
