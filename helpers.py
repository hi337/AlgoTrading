import yfinance as yf
import pandas as pd


def generate_data_csv(ticker, start_date, end_date, output_file):
    """
    Fetches historical stock data for a given ticker and generates a CSV file compatible with backtest.py library.

    Parameters:
        ticker (str): The stock symbol or ticker.
        start_date (str): The start date for the historical data in the format 'YYYY-MM-DD'.
        end_date (str): The end date for the historical data in the format 'YYYY-MM-DD'.
        output_file (str): The name of the CSV file to be generated.

    Returns:
        None
    """

    # Fetch historical stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Extract relevant columns and rename them to match backtest.py's requirements
    backtest_data = stock_data[["Open", "High", "Low", "Close", "Volume"]]

    # Save the data to a CSV file
    backtest_data.to_csv(output_file, index=False)

    print(f"CSV file '{output_file}' generated successfully.")
