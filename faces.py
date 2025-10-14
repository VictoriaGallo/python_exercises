def convert(text):
    # Reemplaza :) con 🙂 y :( con 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Ingrese un texto: ")
    converted_text = convert(user_input)
    print(converted_text)

# Llamada a la función principal
main()
