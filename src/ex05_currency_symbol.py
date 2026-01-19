"""
EX05 (Diccionarios)
Tabla de búsqueda: divisa -> símbolo.
"""

CURRENCIES: dict[str, str] = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

def currency_symbol(currency: str) -> str | None:
    """
    Devuelve el símbolo de la divisa si existe, o None si no existe.

    - No lanza error si la divisa no está.
    """
    return CURRENCIES.get(currency)
print(currency_symbol("Euro"))
print(currency_symbol("Dollar"))
print(currency_symbol("Peso"))
print(currency_symbol("Yen"))
print(currency_symbol("Libra"))
