def main():
    time_str = input("Ingrese la hora (formato 24 horas, ej. 7:30): ")
    time_float = convert(time_str)

    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")
    # Si no está en ninguno de los rangos, no imprime nada


def convert(time):
    hours, minutes = time.strip().split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
