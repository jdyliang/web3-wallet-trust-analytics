# MVP Scope - Web3 Reputation Trust API

## Problem
Web 3 platforms often face issues with fake accounts, bots, and spam activity. Many wallets can interact with decentralized applications without proving whether they represent a real human user.

The goal of this MVP is to design a simple analytics layer that helps platforms determine whether a wallet is likely to belong to a real user.

## Objective
Build a lightweight trust scoring prototype that analyzes wallet activity and output two signals:

Human Likelihood:
- High
- Medium
- Low

Trust Tier:
- Bronze
- Silver
- Gold

## Data Signals Used
This prototype analyzes basic wallet behavior signals including:
- Wallet age
- Transaction counts
- Transaction frequency
- Average transaction value
- Activity consistency
- Active days

## Use Case
A platform could call a simple API with a wallet address and receive a trust assessment.

Example response:

human_likelihood: High
trust_tier: Gold

This allows platforms to filter bots and detect suspicious accounts without accessing private user data.

## Scope Limitations
This MVP focuses only on basic wallet activity signals.

Out of scope:
- Token valuation
- NFT pricing
- DeFi credit scoring
- DAO governance

