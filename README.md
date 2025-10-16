# Análisis visual de jugadores colombianos

## Descripción

Este proyecto se desarrolló como parte del curso *Introducción a la programación con Python* (CS50P) de HarvardX. El objetivo principal es analizar y visualizar datos sobre futbolistas colombianos utilizando Python, `pandas` y `matplotlib`.

El proyecto se basa en un archivo CSV extraído de SoccerWiki, que contiene información básica sobre más de 1700 jugadores colombianos, incluyendo su nombre, apellido, identificación y URL de la imagen. Aunque el conjunto de datos no incluye estadísticas deportivas como goles o minutos jugados, se utiliza para analizar la frecuencia de los apellidos, filtrar por disponibilidad de imágenes y visualizar a los jugadores más destacados.

## Estructura del proyecto

El proyecto consta de los siguientes archivos:

- `project.py`: Archivo principal que contiene la función `main()` y todas las funciones requeridas por CS50P. Aquí se definen las siguientes:
  - `load_data(filename)`: Carga el archivo CSV y devuelve un DataFrame.
  - `analyze_data(df)`: Filtra a los jugadores con imágenes y cuenta los apellidos más comunes.
  - `plot_data(surname_counts)`: Genera un gráfico de barras con los apellidos más frecuentes.
  - `show_players_with_images(df, count=10)`: Muestra los primeros jugadores con imágenes disponibles.
  - `main()`: Coordina la ejecución del programa.

- `test_project.py`: Archivo de prueba que utiliza `pytest` para verificar el correcto funcionamiento de al menos tres funciones (`load_data`, `analyze_data`, `plot_data`). Las pruebas garantizan que el DataFrame se carga correctamente, que los filtros funcionan y que los gráficos no generan errores.
- `requirements.txt`: Enumera las bibliotecas necesarias para ejecutar el proyecto. Incluye:
  - pandas
  - matplotlib
  - requests

- `SoccerWikiJugadorColombiacsv`: Archivo de datos con información sobre jugadores colombianos. Este archivo debe estar en el directorio raíz del proyecto para que las funciones puedan encontrarlo correctamente.

## Decisiones de diseño

Una de las decisiones clave fue trabajar con un conjunto de datos limitado en términos de estadísticas, lo que llevó a centrar el análisis en aspectos visuales y demográficos, como la frecuencia de los apellidos y la disponibilidad de imágenes. Esto permitió cumplir con los requisitos del curso sin necesidad de datos deportivos complejos.

Se eligió Pandas por sus potentes capacidades de manipulación de datos y matplotlib por su facilidad para generar gráficos.

El código se modularizó en funciones independientes para facilitar las pruebas unitarias y cumplir con la estructura requerida por CS50P. Además, se mantuvo una clara separación entre la lógica de análisis y la de visualización.

## Cómo ejecutar el proyecto

1. Instala las dependencias:

```bash
 pip install -r requirements.txt
```

1. Ejecuta el análisis principal:

```bash
python project.py
```

1. Ejecuta las pruebas:

```bash
pytest test_project.py
```

## Conclusión

Este proyecto muestra cómo aplicar los fundamentos de la programación en Python para resolver un problema real de análisis de datos. A través de la carga, el filtrado, la visualización y la comprobación de datos, se consolidan habilidades clave como el uso de bibliotecas externas, la escritura de funciones modulares y la creación de interfaces interactivas. Me siento orgulloso de haber completado este proyecto como parte de CS50P y de haber aprendido a documentar, comprobar y presentar mi trabajo de forma profesional.
