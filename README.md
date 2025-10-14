# Validador de Placas Personalizadas - Massachusetts 🚗

Este proyecto en Python implementa un programa que valida placas personalizadas de vehículos según los requisitos establecidos por el estado de Massachusetts, sede de la Universidad de Harvard.

## 📋 Requisitos de las placas

Para que una placa sea considerada válida, debe cumplir con las siguientes reglas:

- ✅ Debe contener entre **2 y 6 caracteres**.
- ✅ Los **dos primeros caracteres deben ser letras**.
- ✅ Solo se permiten **letras y números** (sin espacios, puntos ni signos de puntuación).
- ✅ Si hay números, deben estar **al final** de la placa.
- ✅ El **primer número no puede ser 0**.

Ejemplos válidos:
- `CS50`
- `AB123`
- `HELLO`

Ejemplos inválidos:
- `A1B2C3` (números en medio)
- `AB012` (número comienza con 0)
- `A.` (signo de puntuación)
- `A` (menos de 2 caracteres)

## 🧠 Estructura del programa

El programa se compone de dos funciones principales:

- `main()`: Solicita al usuario una placa y muestra si es válida o no.
- `is_valid(s)`: Verifica si la placa cumple con todos los requisitos.

## ▶️ Cómo ejecutar

1. Asegúrate de tener Python instalado.
2. Ejecuta el programa desde la terminal:

```bash
python plates.py
