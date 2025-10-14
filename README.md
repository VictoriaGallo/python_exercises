# 🥗 Meal Time Detector

Este programa en Python determina si una hora ingresada por el usuario corresponde a una de las tres comidas principales del día: desayuno, almuerzo o cena.

## 📋 Descripción

El usuario ingresa una hora en formato de 24 horas (`HH:MM`). El programa convierte esa hora a formato decimal (`float`) y verifica si se encuentra dentro de los rangos definidos para cada comida:

- **Desayuno (`breakfast time`)**: entre 7:00 y 8:00
- **Almuerzo (`lunch time`)**: entre 12:00 y 13:00
- **Cena (`dinner time`)**: entre 18:00 y 19:00

Si la hora no coincide con ninguno de estos rangos, el programa no muestra ningún mensaje.

## 🧠 Estructura del código

```python
def main():
    ...

def convert(time):
    ...

if __name__ == "__main__":
    main()
