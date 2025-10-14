import sys
import requests

def main():
    # Verificar si se proporcionó el argumento de línea de comando
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Intentar convertir el argumento a float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Consultar la API de CoinCap
    try:
        api_key = "YourApiKey"  # Reemplaza esto con tu clave real
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching data from CoinCap API")

    # Calcular el costo total
    total = n * price

    # Mostrar el resultado con formato
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
