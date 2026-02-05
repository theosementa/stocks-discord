from datetime import datetime

from models.enums.period_type import PeriodType

def set_time(
    date: datetime,
    hour: int = 0,
    minute: int = 0,
    second: int = 0,
    microsecond: int = 0
):
    return date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

def set_to_start_time(date: datetime):
    return set_time(date)

def set_to_end_time(date: datetime):
    return set_time(date, 23, 59, 59)

def is_weekend(d = datetime.today()):
  return d.weekday() > 4

def is_weekday(d = datetime.today()):
  return d.weekday() <= 4

def display_period_fetched(period: PeriodType, start_date: datetime, end_date: datetime):
    start_date_to_fetch_str = start_date.strftime('%Y-%m-%d')
    end_date_to_fetch_str = end_date.strftime('%Y-%m-%d')
    print(f"{period.name} : {start_date_to_fetch_str} -> {end_date_to_fetch_str}")