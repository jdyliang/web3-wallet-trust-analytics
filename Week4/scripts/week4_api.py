from fastapi import FastAPI, HTTPException
import pandas as pd
from datetime import datetime

app = FastAPI(title = "Wallet Trust API")

df = pd.read_csv("/Users/judy/Desktop/Innovation AI/week 3/csv files/week3_wallet_scored.csv")

df["wallet"] = df["wallet"].astype(str).str.lower()


@app.get("/")
def root():
    return{
        "message": "Wallet Trust API is running"
        }


@app.get("/check")
def check_wallet(wallet: str):
    wallet = wallet.strip().lower()

    result = df[df["wallet"] == wallet]

    if result.empty:
        raise HTTPException(status_code = 404, detail = "Wallet not found")

    row = result.iloc[0]

    return {
        "wallet": row["wallet"],
        "proof": {
            "human_likelihood": row["human_likelihood"],
            "trust_tier": row["trust_tier"],
            "timestamp": datetime.utcnow().isoformat(),
            "version": "v1"
            }
        }
