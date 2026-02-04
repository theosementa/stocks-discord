import os

def get_tickers() -> list[str]:
    tickers_raw = os.getenv('TICKERS')

    if tickers_raw:
        tickers_list = tickers_raw.split(',')
    else:
        tickers_list = []
        
    return tickers_list