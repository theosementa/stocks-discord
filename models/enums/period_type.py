from enum import Enum
import calendar
from datetime import datetime, timedelta
from utils.date_utils import set_to_end_time, set_to_start_time

class PeriodType(Enum):
    NONE = "NONE"
    YESTERDAY = "YESTERDAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    
    def get_dates_to_fetch(self):
        start_date = datetime.now()
        end_date = datetime.now()
    
        match self:
            case self.YESTERDAY:
                start_date = set_to_start_time(datetime.now() - timedelta(1))
                end_date = set_to_end_time(datetime.now() - timedelta(1))
            case self.WEEK:
                now = datetime.now()
                start_date = set_to_start_time(now - timedelta(days=now.weekday()))
                end_date = set_to_end_time(start_date + timedelta(days=6))
            case self.MONTH:
                end_day = calendar.monthrange(start_date.year, start_date.month)[1]
                start_date = set_to_start_time(start_date.replace(day=1))
                end_date = set_to_end_time(end_date.replace(day=end_day))
            
        return (start_date, end_date)  