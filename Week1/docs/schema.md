# Wallet Features Schema

This document describes the structure of the wallet feature dataset generated in this project.

## wallet_features_multi.csv

wallet: wallet address (string)

first_tx: first observed transaction datetime

last_tx: last observed transaction datetime

wallet_age_days: number of days between first and last transaction

tx_count: total number of transactions

tx_frequency: transactions per day

avg_tx_value: average transaction value

active_days: number of days with at least one transaction
