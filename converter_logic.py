from currency_converter import CurrencyConverter

def convert_currency(
        value: float,
        start_currency: str = 'USD', 
        to_currency: str = 'EUR'
    ) -> float:
    currency_converter = CurrencyConverter()
    value_converted = currency_converter.convert(value, start_currency, to_currency)
    return round(value_converted, 2)