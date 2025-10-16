import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    """Loads the CSV file and returns a dataFrame"""
    df = pd.read_csv(filename)
    return df

def analyze_data(df):
    """Filter players by image and most common last names"""
    df_with_images = df[df['ImageURL'].notna() & (df['ImageURL'] != '')]
    surname_counts = df_with_images['Surname'].value_counts().head(10)
    return df_with_images, surname_counts



def plot_data(surname_counts):
    """Generate a bar chart showing the most common surnames"""
    plt.figure(figsize=(10, 6))
    surname_counts.plot(kind='bar', color='skyblue')
    plt.title('Apellidos más comunes entre jugadores colombianos')
    plt.xlabel('Apellido')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafico_apellidos.png")
    print("Gráfico guardado como 'grafico_apellidos.png'")

def show_players_with_images(df, count=10):
    """Shows the first players with available images"""
    df_with_images = df[df['ImageURL'].notna() & (df['ImageURL'] != '')]
    top_players = df_with_images.head(10)
    for _, row in top_players.iterrows():
        full_name = f"{row['Forename']} {row['Surname']}"
        image_url = row['ImageURL']
        print(f"{full_name}: {image_url}")

def main():
    print("Cargando datos...")
    df = load_data("SoccerWikiJugadorColombia.csv")
    print("Datos cargados.")

    print("Analizando datos...")
    df_with_images, surname_counts = analyze_data(df)
    print("Anlisis completo.")

    print("Generando gráfico...")
    plot_data(surname_counts)
    print("Grafico generado.")

    print("Mostrando jugadores con imagen...")
    show_players_with_images(df_with_images)

if __name__ == "__main__":
    main()
