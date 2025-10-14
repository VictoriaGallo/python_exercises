def main():
    texto = input("Input: ")
    print("Output:", sin_vocales(texto))

def sin_vocales(s):
    vocales = "aeiouAEIOU"
    return "".join([c for c in s if c not in vocales])

if __name__ == "__main__":
    main()
