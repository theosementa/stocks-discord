from dataclasses import dataclass
from models.enums.period_type import PeriodType

@dataclass
class TickerResponse:
    period: PeriodType
    open_value_raw: float
    close_value_raw: float
    high_value_raw: float
    low_value_raw: float

    def get_evolution(self) -> float:
        return ((self.close_value_raw / self.open_value_raw) - 1) * 100