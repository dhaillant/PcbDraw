from decimal import Decimal
from typing import List


def erase(string: str, what: List[str]) -> str:
    """
    Given a  string and a list of string, removes all occurrences of items from
    what in the string
    """
    for x in what:
        string = string.replace(x, "")
    return string


def read_resistance(value: str) -> Decimal:
    """
    Given a string, try to parse resistance and return it as Ohms (Decimal)

    This function can raise a decimal.InvalidOperation if the value is invalid
    """
    p_value = erase(value, ["Ω", "Ohms", "Ohm"]).strip()
    p_value = p_value.replace(" ", "") # Sometimes there are spaces after decimal place
    unit_prefixes = {
        "m": [Decimal(1e-3), Decimal(1e-6)],
        "K": [Decimal(1e3), Decimal(1)],
        "k": [Decimal(1e3), Decimal(1)],
        "M": [Decimal(1e6), Decimal(1e3)],
        "G": [Decimal(1e9), Decimal(1e6)]
    }
    numerical_value = None
    for prefix, table in unit_prefixes.items():
        if prefix in p_value:
            split = [Decimal(x) if x != "" else Decimal(0) for x in p_value.split(prefix)]
            numerical_value = split[0] * table[0] + split[1] * table[1]
            break
    if numerical_value is None:
        # Handle values that don't have a prefix. If this fails, a InvalidOperation will be raised
        #       which will be catched by the exception
        numerical_value = Decimal(p_value)
    return numerical_value
