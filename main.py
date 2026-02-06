from dotenv import load_dotenv
import sys
import os
import requests
import yfinance as yf
from tickers import get_tickers
from models.enums.period_type import PeriodType
from define_period import define_period_to_fetch
from models.ticker_response import TickerResponse

load_dotenv()

tickers_list = get_tickers()
informations = []
datas = yf.Tickers(tickers_list)
selected_periods = define_period_to_fetch()

if PeriodType.NONE in selected_periods :
    sys.exit("We are Monday, nothing append yesterday")

for period in selected_periods:
    
    dates_to_fetch = period.get_dates_to_fetch()
    
    start_date_to_fetch_str = dates_to_fetch[0].strftime('%Y-%m-%d')
    end_date_to_fetch_str = dates_to_fetch[1].strftime('%Y-%m-%d')
    period_header = f"{selected_periods[0].name} : {start_date_to_fetch_str} -> {end_date_to_fetch_str}"
    informations.append(period_header)
    
    for ticker in tickers_list:
        current_ticker = yf.Ticker(ticker)
        history = current_ticker.history(start=dates_to_fetch[0], end=dates_to_fetch[1])
    
        first_index = history.index[0]
        last_index = history.index[len(history.index) - 1]
        open_value = history.loc[first_index]['Open']
        close_value = history.loc[last_index]['Close']
        
        ticker_response = TickerResponse(ticker, period, open_value, close_value, 0, 0)
        informations.append(ticker_response.display_informations())
        
    delimiter = "\n"
    join_str = delimiter.join(informations)
    data = { "content": join_str }

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    requests.post(webhook_url, json=data)