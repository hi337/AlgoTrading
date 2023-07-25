# This file contains the macd strategy for backtesting

from helpers import generate_data_csv

ticker = "BTC-CAD"

# generate the data
generate_data_csv(ticker, "2023-01-01", "2023-07-24", ticker + " data.csv")

# make the strategy class

# run the strategy
