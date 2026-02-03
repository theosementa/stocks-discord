from dotenv import load_dotenv
import os
import yfinance as yf
from currency_converter import CurrencyConverter

load_dotenv()

currencyConv = CurrencyConverter()

tickers_raw = os.getenv('TICKERS')

if tickers_raw:
    tickers_list = tickers_raw.split(',')
    print(tickers_list)
else:
    tickers_list = []

data = yf.Ticker('AAPL')
currentValue = data.analyst_price_targets["current"]
print(currentValue)

eurPrice = currencyConv.convert(currentValue, 'USD', 'EUR')
print(round(eurPrice, 2))