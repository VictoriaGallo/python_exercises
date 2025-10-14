# Solicita al usuario la masa como un entero
mass = int(input("Masa (kg): "))

# Define la velocidad de la luz en metros por segundo
c = 300000000

# Calcula la energia usando la fórmula E = mc^2
energy = mass * c ** 2

# Muestra el resultado como un entero
print(energy)
