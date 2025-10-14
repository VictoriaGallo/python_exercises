

# Solicita al usuario una expresión aritmética
expression = input("Ingrese una expresión aritmética (formato: x y z): ")

# Divide la expresión en sus componentes
x, y, z = expression.split(" ")

# Convierte x y z a enteros
x = int(x)
z = int(z)

# Realiza la operación correspondiente
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Muestra el resultado con un decimal
print(f"{result:.1f}")
