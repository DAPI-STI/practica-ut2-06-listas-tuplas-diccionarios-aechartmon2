[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PXTCo7pA)
# Práctica 02.06 · Listas, tuplas y diccionarios (funciones + tests)

En esta práctica vas a resolver **6 ejercicios** para practicar **tipos de datos compuestos**:

- **Listas** (`list`) → 2 ejercicios
- **Tuplas** (`tuple`) → 2 ejercicios
- **Diccionarios** (`dict`) → 2 ejercicios (el último es un compendio)

La corrección se hace automáticamente con **pytest** (tests).  
Además, tendrás un archivo **`src/__main__.py`** para probar tus funciones “a mano”.

---

## Estructura del proyecto

```text
practica_0206_listas_tuplas_diccionarios/
├─ src/                 # Tu código (EDITA AQUÍ)
│  ├─ __init__.py
│  ├─ __main__.py        # Pruebas manuales (no se evalúa)
│  ├─ ex01_reverse_list.py
│  ├─ ex02_unique_preserve_order.py
│  ├─ ex03_min_max_prices.py
│  ├─ ex04_best_student.py
│  ├─ ex05_currency_symbol.py
│  └─ ex06_checkout.py
├─ test/                # Tests (NO TOCAR)
│  └─ test_practica_0206.py
├─ README.md
├─ requirements.txt
└─ .gitignore
```

✅ Regla principal: **solo debes editar `src/`**.  
❌ No modifiques los tests.

---

## Primeros pasos

### 1) (Opcional) Crear entorno virtual

```bash
python -m venv .venv
# Windows (PowerShell/CMD):
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3) Ejecutar tests

```bash
python -m pytest -q
```

---

## Probar sin tests (opcional)

```bash
python -m src
```

Eso ejecuta `src/__main__.py`. Puedes editarlo para hacer pruebas manuales.

---

## Flujo recomendado

1) Ejecuta tests: `python -m pytest -q`  
2) Elige un ejercicio de `src/`  
3) Implementa la función y elimina el `raise NotImplementedError(...)`  
4) Vuelve a ejecutar tests  
5) Repite hasta pasar todo ✅
