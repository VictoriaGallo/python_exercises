# 😊 faces.py

Este proyecto contiene un pequeño programa en Python que convierte emoticonos de texto en emojis gráficos. Es ideal para practicar funciones, entrada de usuario y manipulación de cadenas.

## 📄 Descripción

El programa busca en una cadena los siguientes emoticonos:

- `:)` → se convierte en `🙂` (cara ligeramente sonriente)
- `:(` → se convierte en `🙁` (cara ligeramente fruncida)

El resto del texto permanece sin cambios.

## 🧠 Funciones

- `convert(text: str) -> str`: Recibe una cadena de texto y reemplaza los emoticonos por sus emojis correspondientes.
- `main()`: Solicita al usuario una entrada, llama a `convert` y muestra el resultado.

## ▶️ Ejecución

Para ejecutar el programa, abre una terminal y escribe:

```bash
python faces.py
