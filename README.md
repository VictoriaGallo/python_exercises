# 🗓️ Conversión de Fechas al Formato ISO 8601

Este proyecto consiste en un programa en Python llamado `outdated.py` que solicita al usuario una fecha en formato estadounidense (mes-día-año) y la convierte al formato internacional ISO 8601 (año-mes-día).

## 📋 Descripción

En Estados Unidos, las fechas suelen escribirse como `MM/DD/YYYY` o `Month D, YYYY`, lo que puede generar ambigüedad y problemas al ordenarlas cronológicamente. Este programa convierte esas fechas al formato estándar `YYYY-MM-DD`, recomendado por la norma ISO 8601.

## 🧠 Formatos aceptados

El programa acepta dos formatos de entrada:

- Numérico: `MM/DD/YYYY` (ej. `9/8/1636`)
- Texto: `Month D, YYYY` (ej. `September 8, 1636`)

> **Nota:** El mes en formato texto debe estar en inglés y con la primera letra en mayúscula.

## 🚫 Validaciones

- El mes debe estar entre 1 y 12.
- El día debe estar entre 1 y 31.
- Si la entrada no es válida, el programa volverá a solicitarla.

## 🧪 Ejemplos de uso

```bash
$ python outdated.py
Date: 9/8/1636
1636-09-08

$ python outdated.py
Date: September 8, 1636
1636-09-08

$ python outdated.py
Date: 23/6/1912
Date: December 80, 1980
# El programa seguirá preguntando hasta recibir una fecha válida.
