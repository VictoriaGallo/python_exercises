# 💸 Bank Greeting Challenge

Este proyecto está inspirado en el episodio 24 de la temporada 7 de *Seinfeld*, donde Kramer visita un banco que promete dar $100 a quien no sea saludado con un "hola". El gerente del banco negocia con Kramer según el tipo de saludo recibido.

## 🧠 Descripción

El programa `bank.py` solicita al usuario un saludo y determina cuánto dinero se le debe entregar según las siguientes reglas:

- Si el saludo comienza con `"hola"` (ignorando mayúsculas y espacios), se genera `$0`.
- Si el saludo comienza con `"h"` pero **no** con `"hola"`, se genera `$20`.
- Para cualquier otro saludo, se genera `$100`.

## 🛠️ Requisitos

- Python 3.x

## 🚀 Ejecución

Para ejecutar el programa, abre una terminal y escribe:

```bash
python bank.py
