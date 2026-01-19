"""
EX04 (Tuplas)
Trabajar con una lista de tuplas (nombre, nota) y devolver una tupla.
"""

def best_student(records: list[tuple[str, float]]) -> tuple[str, float]:
    """
    Recibe una lista de tuplas (nombre, nota) y devuelve la tupla del alumno con mayor nota.

    - Si records está vacío, lanza ValueError.
    - Si hay empate, devuelve el primero que aparezca con esa nota.

    Ejemplo:
    [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)] -> ("Luis", 9.0)
    """
    if not records:
        raise  ValueError("La lista de registros está vacía")
    return max(records, key= lambda record: record[1])

alumnos = [("Ana", 7.5), ("Luis", 9.0), ("Marta", 8.0)]
print(best_student(alumnos))