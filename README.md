# 🛒 Grocery List Program

Este programa en Python permite al usuario crear una lista de la compra ingresando artículos uno por uno. Al finalizar la entrada (presionando `Ctrl+D`), el programa muestra la lista en mayúsculas, ordenada alfabéticamente, junto con la cantidad de veces que cada artículo fue ingresado.

---

## 📄 Descripción

- El usuario ingresa artículos por línea.
- La entrada finaliza al presionar `Ctrl+D` (en Linux/macOS) o `Ctrl+Z` seguido de `Enter` (en Windows).
- La salida muestra:
  - Cada artículo en mayúsculas.
  - Orden alfabético.
  - Número de veces que se ingresó cada artículo.

---

## 🧠 Características

- Ignora diferencias entre mayúsculas y minúsculas (`milk` y `MILK` se cuentan como el mismo artículo).
- Evita errores de clave (`KeyError`) usando el método `dict.get()`.
- Utiliza `try/except` para capturar `EOFError` al finalizar la entrada.

---

## 🖥️ Ejecución

1. Guarda el archivo como `grocery.py`.
2. Ejecuta el programa en la terminal:

```bash
python grocery.py
