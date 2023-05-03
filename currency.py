from forex_python.converter import CurrencyRates


def currency_converter(amount: float, from_currency: str = 'USD', to_currency: str = 'IDR') -> float:
    """
    This is a python wrapper class to https://theforexapi.com is a free API for current
    and historical. Foreign exchange rates published by
    European Central Bank. The rates are updated daily 3PM CET.
    for list of currencies see https://theforexapi.com/api/latest
    Args:
        amount: Amount to convert
        from_currency: To currency str
        to_currency: From currency str
    """
    return CurrencyRates().convert(from_currency, to_currency, amount)
