import pandas as pd
from project import load_data, analyze_data, plot_data

def test_load_data():
    df = load_data("SoccerWikiJugadorColombia.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "Forename" in df.columns
    assert "Surname" in df.columns

def test_analyze_data():
    df = load_data("SoccerWikiJugadorColombia.csv")
    df_with_images, surname_counts = analyze_data(df)
    assert isinstance(df_with_images, pd.DataFrame)
    assert isinstance(surname_counts, pd.Series)
    assert not df_with_images.empty
    assert surname_counts.size > 0

def test_plot_data():
    df = load_data("SoccerWikiJugadorColombia.csv")
    _, surname_counts = analyze_data(df)
    try:
        plot_data(surname_counts)
    except Exception as e:
        assert False, f"plot_data raised an exception: {e}"
