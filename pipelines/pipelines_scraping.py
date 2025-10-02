import pandas as pd
from get_data.get_scraping_data import scrape_books
from process_data.process_scraping_data import process_scarping_data
from database.insert_data import creation_bd, insert_data

def run_scraping_pipeline(pages: int = 5, base_url: str = "http://books.toscrape.com/catalogue/page-{}.html") -> pd.DataFrame:
    """
    Pipeline final de scarping, nettoyage et insertion des données des livres.

    Étapes :
    1. Scraping des données sur plusieurs pages
    2. Sauvegarde des données brutes dans `data/data_scraping.csv`
    3. Nettoyage et conversion des types
    4. Insertion des données dans une base SQLite
    5. Affichage du nombre de livres insérés

    Args:
        pages (int, optional): Nombre de la page à scraper. Par défaut 5.
        base_url (str, optional): URL avec placeholder `{}` pour le numéro de page.
        Par défaut : "http://books.toscrape.com/catalogue/page-{}.html"

    Return: pd.DataFrame nettoyé
    """
    # Scraping des données
    print("1. Scraping des données")
    df_raw = scrape_books(pages, base_url)

    # Sauvegarde des données brutes
    print("1. Sauvegarde des données brutes")
    df_raw.to_csv("data/data_scarping.csv", index=True)

    # Nettoyage des données
    df_clean = process_scarping_data(df_raw)
    print("Nettoyage des données")

    # Création et insertion en base
    print("Création et insertion en base")
    connection = creation_bd(df_clean)
    insert_data(connection)
    connection.close()

    print("Pipeline trerminé avec succès.")

    return df_clean
