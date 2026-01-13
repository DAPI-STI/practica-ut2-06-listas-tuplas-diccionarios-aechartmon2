"""
EX03 (Tuplas)
Devolver el mínimo y el máximo de una lista.
"""

def min_max_prices(prices: list[float]) -> tuple[float, float]:
    """
    Devuelve una tupla (mínimo, máximo).

    - Si prices está vacía, lanza ValueError.
    """
    if not prices:
        raise ValueError("La lista de precios esta vaciaa")
    return (min(prices), max(prices))

print(min_max_prices([10.5, 7.2, 15.0, 3.8]))
