def main():
    answer = input("¿Cuál es la respuesta a la Gran Pregunta de la Vida, el Universo y Todo?\n")
    normalized = answer.strip().lower()

    if normalized in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
