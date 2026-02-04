from dotenv import load_dotenv
import os
import yfinance as yf
from converter_logic import convert_currency
from datetime import datetime, timedelta
from tickers import get_tickers
from models.enums.period_type import PeriodType
import calendar

load_dotenv()

tickers_list = get_tickers()

datas = yf.Tickers(tickers_list)

# for ticker in tickers_list:
    # print(datas.tickers[ticker].analyst_price_targets["current"])

print("\n\n")

data = yf.Ticker('AAPL')
currentValue = data.analyst_price_targets["current"]
#print(convert_currency(currentValue))

def get_dates_to_fetch(period: PeriodType):
    start_date = datetime.now()
    end_date = datetime.now()
    
    match period:
        case PeriodType.YESTERDAY:
            start_date = datetime.now() - timedelta(1)
            end_date = datetime.now() - timedelta(1)
        case PeriodType.WEEK:
            now = datetime.now()
            start_date = now - timedelta(days=now.weekday())
            end_date = start_date + timedelta(days=6)
        case PeriodType.MONTH:
            end_day = calendar.monthrange(start_date.year, start_date.month)[1]
            start_date = start_date.replace(day=1)
            end_date = end_date.replace(day=end_day)
            
    return (start_date, end_date)

def define_period_to_fetch():
    return # TODO: pour yesterday c'est ok, pour week c'est ok, pour month envoyer aussi yesterday

selected_period = PeriodType.YESTERDAY

dates_to_fetch = get_dates_to_fetch(selected_period)
# print(dates_to_fetch)

start_date_to_fetch_str = dates_to_fetch[0].strftime('%Y-%m-%d')
end_date_to_fetch_str = dates_to_fetch[1].strftime('%Y-%m-%d')
print(f"{selected_period.name} : {start_date_to_fetch_str} -> {end_date_to_fetch_str}")

history = data.history(start=dates_to_fetch[0], end=dates_to_fetch[1])
# print(history)


# def is_weekend(d = datetime.today()):
  # return d.weekday() > 4

# if is_weekend(date_to_fetch):
  # print("That the weekend, stocks are closed")
  
def calcul_evolution(
    open_value: float,
    close_value: float
    ) -> float:
    evolution = ((close_value / open_value) - 1) * 100
    
    open_value_eur = convert_currency(open_value)
    close_value_eur = convert_currency(close_value)
    
    print(f"Pourcentage d'évolution : {round(evolution, 2)}% | {round(open_value_eur, 2)} -> {round(close_value_eur, 2)}")
    
    return evolution
  

first_index = history.index[0]
last_index = history.index[len(history.index) - 1]
open_value = history.loc[first_index]['Open']
close_value = history.loc[last_index]['Close']
    
open_value_eur = convert_currency(open_value)
close_value_eur = convert_currency(close_value)
    
evolution = calcul_evolution(open_value, close_value)    