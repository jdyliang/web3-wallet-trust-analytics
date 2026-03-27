import requests
import pandas as pd
import time


API_KEY = "YOUR_API_KEY"

seed_wallets = [
    "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
    "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb7",
    "0x66f820a414680b5bcda5eeca5dea238543f42054",
    "0xfe9e8709d3215310075d67e3ed32a380ccf451c8",
    "0x28c6c06298d514db089934071355e5743bf21d60",
    "0x564286362092d8e7936f0549571a803b203aaced",
    "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
    "0xf977814e90da44bfa03b6295a0616a897441acec",
    "0x3f5ce5fbfe3e9af3971dD833D26BA9b5C936f0bE",
    "0xdc76cd25977e0a5ae17155770273ad58648900d3",
    "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
    "0x00000000219ab540356cBB839Cbe05303d7705Fa"
    ]

def get_wallets_from_seed(seed_address, per_seed = 60):
    url = "https://api.etherscan.io/v2/api"

    params = {
        "chainid": "1",
        "module": "account",
        "action": "txlist",
        "address": seed_address,
        "starblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": API_KEY
        }

    response = requests.get(url, params = params, timeout = 30)
    data = response.json()

    print("\nProcessing seed:", seed_address)
    print("API response status:", data.get("status"))
    print("API ressponse message:", data.get("message"))

    if data.get("status") != "1":
        print("API error:")
        print(data)
        return []

    wallets = set()

    for tx in data["result"]:
        from_addr = str(tx.get("from", "")).strip()
        to_addr = str(tx.get("to", "")).strip()

        if from_addr.startswith("0x") and len(from_addr) == 42:
            wallets.add(from_addr)

        if to_addr.startswith("0x") and len(to_addr) == 42:
            wallets.add(to_addr)

        if len(wallets) >= 20:
            break

    return list(wallets)

all_wallets = set()

for seed in seed_wallets:
    wallets = get_wallets_from_seed(seed, per_seed = 30)

    for w in wallets:
        all_wallets.add(w)

    print("Current unique wallets:", len(all_wallets))
    time.sleep(0.4)

wallet_list = list(all_wallets)[:200]

print("\nFinal number of wallets:", len(wallet_list))
print("\nFirst 20 wallets:")
for w in wallet_list[:20]:
    print(w)

wallet_df = pd.DataFrame({"wallet": wallet_list})
wallet_df.to_csv("week3_wallet_list_200.csv", index = False)

print("\nSaved file: week3_wallet_list_200.csv")
