import inflect

# Create an inflect engine
p = inflect.engine()

# Initialize an empty list to store names
names = []

# Prompt user for names until EOF (Ctrl-D)
try:
    while True:
        name = input("Name: ")
        if name:  # Avoid adding empty strings
            names.append(name)
except EOFError:
    formatted_names = p.join(names)
    print(f"\nAdieu, adieu, to {formatted_names}")
