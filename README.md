# 🧾 Taquería Felipe's - Programa de Pedido Interactivo

Este proyecto es un pequeño programa en Python que simula el sistema de pedidos de **Felipe's Taqueria**, un popular restaurante en Harvard Square. El usuario puede introducir artículos del menú uno por uno, y el programa mostrará el total acumulado en dólares después de cada entrada válida.

## 📋 Descripción

El programa permite al usuario realizar un pedido ingresando artículos del menú por línea. Cada vez que se introduce un artículo válido, se actualiza y muestra el total acumulado. El programa ignora entradas no válidas y no distingue entre mayúsculas y minúsculas.

El pedido finaliza cuando el usuario presiona `Ctrl+D` (EOF).

## 🧠 Características

- ✅ Reconocimiento de artículos del menú sin distinción entre mayúsculas y minúsculas.
- ✅ Ignora entradas no válidas sin generar errores.
- ✅ Muestra el total acumulado con formato de moneda (`$xx.xx`).
- ✅ Finaliza con `Ctrl+D` y deja el cursor en una nueva línea.

## 🧾 Menú

```python
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
