months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_input = input("Date: ").strip()

    try:
        # Intentar formato MM/DD/YYYY
        if "/" in date_input:
            parts = date_input.split("/")
            if len(parts) == 3:
                month, day, year = map(int, parts)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        # Intentar formato Month D, YYYY
        elif "," in date_input:
            month_day, year = date_input.split(",")
            month_day = month_day.strip()
            year = int(year.strip())

            parts = month_day.split(" ")
            if len(parts) == 2:
                if parts[0] in months:
                    month = months.index(parts[0]) + 1
                    day = int(parts[1])
                    if 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break
    except:
        pass

    # Si no se pudo analizar, volver a pedir
    continue
