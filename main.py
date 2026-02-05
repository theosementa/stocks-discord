from dotenv import load_dotenv
import sys
import yfinance as yf
from tickers import get_tickers
from models.enums.period_type import PeriodType
from define_period import define_period_to_fetch
from define_date import get_dates_to_fetch
from models.ticker_response import TickerResponse
from utils.date_utils import display_period_fetched

load_dotenv()

tickers_list = get_tickers()

datas = yf.Tickers(tickers_list)
selected_periods = define_period_to_fetch()

if PeriodType.NONE in selected_periods :
    sys.exit("We are Monday, nothing append yesterday")

for ticker in tickers_list:
    
    print("\n")
    print(f"---{ticker}---")
    
    current_ticker = yf.Ticker(ticker)
    
    for period in selected_periods:
        dates_to_fetch = get_dates_to_fetch(period)    
        display_period_fetched(period, dates_to_fetch[0], dates_to_fetch[1])

        history = current_ticker.history(start=dates_to_fetch[0], end=dates_to_fetch[1])
    
        first_index = history.index[0]
        last_index = history.index[len(history.index) - 1]
        open_value = history.loc[first_index]['Open']
        close_value = history.loc[last_index]['Close']
        
        ticker_response = TickerResponse(period, open_value, close_value, 0, 0)
        print(f"Evolution : {round(ticker_response.get_evolution(), 2)}%")
        
    print("\n")