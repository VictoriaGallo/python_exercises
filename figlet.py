import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Handle command-line arguments
    if len(sys.argv) == 1:
        # No font specified, choose a random one
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Prompt user for input
    text = input("Input: ")

    # Set font and render text
    figlet.setFont(font=font)
    print("Output:")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
