# This file contains the macd+adx strategy for backtesting

from helpers import generate_data_csv
from backtesting import Backtest, Strategy
import talib
import pandas as pd

ticker = "HNU.TO"
output_file = ticker + "_data.csv" 

# generate the data
generate_data_csv(ticker, "2023-01-01", "2023-07-24", output_file)

# make the strategy class
class MACDADX(Strategy):
    timeperiod = 14
    def init(self):
        self.macd, self.signal, self.hist = self.I(talib.MACD, self.data.Close)
        self.adx = self.I(talib.ADX, self.data.High, self.data.Low, self.data.Close, timeperiod=self.timeperiod)
        self.market_is_bullish = False

    def next(self):
        if self.macd[-1] > self.signal[-1]:
            market_is_bullish = True
        elif self.macd[-1] < self.signal[-1]:
            market_is_bullish = False

        if self.adx[-1] > 20:
            if market_is_bullish:
                self.buy()
            else:
                self.sell()

# import the csv data into python
data = pd.read_csv(output_file)
data.columns = [column.capitalize() for column in data.columns]
data = data.dropna()


# backtest the strategy
bt = Backtest(data, MACDADX, cash=100000, commission=0.01)

stats = bt.optimize(maximize="Equity Final [$]", timeperiod=range(10, 30))

print(stats)

bt.plot()