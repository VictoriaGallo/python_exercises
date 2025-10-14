# Playback 🎧

Este es un pequeño programa en Python que toma una entrada del usuario y la reproduce reemplazando cada espacio con tres puntos (`...`).

## Descripción

El propósito de este programa es practicar el uso de entrada de usuario y manipulación de cadenas en Python. Cuando el usuario escribe una frase, el programa la transforma visualmente para simular un "efecto de reproducción" al reemplazar los espacios por puntos suspensivos.

## Cómo usarlo

1. Asegúrate de tener Python instalado en tu sistema.
2. Guarda el siguiente código en un archivo llamado `playback.py`:

   ```python
   entrada = input("Ingrese una frase: ")
   salida = entrada.replace(" ", "...")
   print(salida)
