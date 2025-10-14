def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Requisito 1: longitud entre 2 y 6 caracteres
    if not (2 <= len(s) <= 6):
        return False

    # Requisito 2: los dos primeros caracteres deben ser letras
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Requisito 3: no se permiten puntos, espacios ni signos de puntuación
    if not s.isalnum():
        return False

    # Requisito 4: si hay números, deben estar al final y no comenzar con 0
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not number_started:
                number_started = True
                if s[i] == '0':
                    return False
            # Si ya empezaron los números, todo lo que sigue debe ser número
        elif number_started:
            return False

    return True


main()
