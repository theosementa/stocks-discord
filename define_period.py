import calendar
from datetime import datetime, timedelta
from models.enums.period_type import PeriodType
from utils.date_utils import is_weekday

def define_period_to_fetch() -> list[PeriodType]:
    now = datetime.now()
    end_day = calendar.monthrange(now.year, now.month)[1]
    yesterday = now - timedelta(1)
    
    if end_day == now.day:
        if is_weekday(yesterday):
            return [PeriodType.MONTH, PeriodType.YESTERDAY]
        else:
            return [PeriodType.MONTH]
    if is_weekday(yesterday):
        return [PeriodType.YESTERDAY]
    else: # Weekend
        now = datetime.now()
        start_date = now - timedelta(days=now.weekday())
        end_date = start_date + timedelta(days=6)
        
        if now == end_date: # Sunday
            return [PeriodType.WEEK]
        else:
            return [PeriodType.NONE]