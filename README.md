# 🧩 Extensiones de Archivos — Identificador de Tipo MIME

Este programa en Python solicita al usuario el nombre de un archivo y determina su tipo de medio (MIME type) según su extensión. Si la extensión no es reconocida, se asigna un tipo por defecto: `application/octet-stream`.

## 📂 Extensiones Soportadas

El programa reconoce las siguientes extensiones (sin distinguir entre mayúsculas y minúsculas):

| Extensión | Tipo MIME              |
|-----------|------------------------|
| `.gif`    | `image/gif`            |
| `.jpg`    | `image/jpeg`           |
| `.jpeg`   | `image/jpeg`           |
| `.png`    | `image/png`            |
| `.pdf`    | `application/pdf`      |
| `.txt`    | `text/plain`           |
| `.zip`    | `application/zip`      |

