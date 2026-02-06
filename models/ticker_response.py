from dataclasses import dataclass
from models.enums.period_type import PeriodType
from converter_logic import convert_currency

@dataclass
class TickerResponse:
    ticker: str
    period: PeriodType
    open_value_raw: float
    close_value_raw: float
    high_value_raw: float
    low_value_raw: float

    def get_evolution(self) -> float:
        return ((self.close_value_raw / self.open_value_raw) - 1) * 100
    
    def get_evolution_amount(self) -> float:
        return self.close_value_raw - self.open_value_raw
    
    def get_symbol(self, value: float) -> str:
        return "+" if value > 0 else ""
    
    def display_informations(self) -> str:
        dates_to_fetch = self.period.get_dates_to_fetch()
        
        start_date_to_fetch_str = dates_to_fetch[0].strftime('%Y-%m-%d')
        end_date_to_fetch_str = dates_to_fetch[1].strftime('%Y-%m-%d')
    
        open_value_eur = round(convert_currency(self.open_value_raw), 2)
        close_value_eur = round(convert_currency(self.close_value_raw), 2)
        
        evolution = round(self.get_evolution(), 2)
        evolution_amount_eur = round(convert_currency(self.get_evolution_amount()), 2)
        
        return f"""
---{self.ticker}---
{self.period.name} : {start_date_to_fetch_str} -> {end_date_to_fetch_str}
Ouverture : {open_value_eur}€
Fermeture : {close_value_eur}€
Évolution : {self.get_symbol(evolution)}{evolution}% ({self.get_symbol(evolution_amount_eur)}{evolution_amount_eur}€)
"""