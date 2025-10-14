def main():
    # Solicita al usuario el nombre del archivo
    filename = input("Nombre del archivo: ").strip().lower()

    # Diccionario de extensiones y sus tipos MIME
    mime_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Verifica si el nombre del archivo termina con alguna de las extensiones conocidas
    for ext, mime in mime_types.items():
        if filename.endswith(ext):
            print(mime)
            return

    # Si no coincide con ninguna extensión conocida
    print("application/octet-stream")

if __name__ == "__main__":
    main()
