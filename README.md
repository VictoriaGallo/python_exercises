# ⛽ Fuel Indicator

Este proyecto implementa un programa en Python que interpreta fracciones como indicadores de nivel de combustible en un tanque. El usuario ingresa una fracción en formato `X/Y`, y el programa muestra el porcentaje correspondiente, redondeado al entero más cercano.

## 📋 Descripción

El programa solicita al usuario una fracción (`X/Y`) donde `X` y `Y` son enteros positivos. Luego:

- Calcula el porcentaje de combustible restante.
- Si el porcentaje es **1% o menos**, muestra `E` (Empty).
- Si el porcentaje es **99% o más**, muestra `F` (Full).
- En otros casos, muestra el porcentaje como `25%`, `50%`, etc.

El programa valida la entrada y vuelve a solicitarla si:

- `X` o `Y` no son enteros positivos.
- `X > Y`.
- `Y == 0`.
- El formato no es válido (`cat/dog`, `1.5/3`, etc.).

## 🧪 Ejemplos de uso

```bash
$ python fuel.py
Fraction: 3/4
75%

$ python fuel.py
Fraction: 4/4
F

$ python fuel.py
Fraction: 0/4
E

$ python fuel.py
Fraction: -3/4
# Vuelve a pedir la fracción

$ python fuel.py
Fraction: three/four
# Vuelve a pedir la fracción
```
## ✅ Cómo ejecutar las pruebas
Asegúrate de tener pytest instalado. Luego ejecuta:

```bash
pytest test_fuel.py
```
Esto verificará que tus funciones convert y gauge se comporten correctamente en todos los casos relevantes.
