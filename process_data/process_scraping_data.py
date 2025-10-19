import pandas as pd

def process_scarping_data(df_books: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et convertit les types des colonnes du DataFrame de livres.

    Cette fonction :
      - convertit la colonne 'title' en chaînes de caractères,
      - retire le symbole '£' de la colonne 'price' et la convertit en float,
      - transforme la colonne 'availability' en booléen (True si "In stock", sinon False),
      - nettoie la colonne 'rating' et la convertit en valeur entière de 1 à 5.

    Args:
        df_books (pd.DataFrame): Le DataFrame contenant les données brutes extraites du site de livres.

    Returns:
        pd.DataFrame: Le DataFrame nettoyé avec des types de colonnes appropriés.
    """
    # Conversion de title en chaîne de caractères
    df_books["title"] = df_books["title"].astype(str)
    
    # Conversion de price en float après suppression du symbole '£'
    df_books["price"] = df_books["price"].astype(str).str.removeprefix("£").astype(float)

    # Fonction pour convertir la disponibilité en booléen
    def convert_availability(value: str) -> bool:
        return value == "In stock"

    # Application de la conversion sur la colonne availability
    df_books["availability"] = df_books["availability"].apply(convert_availability)

    # Nettoyage et conversion des ratings
    df_books["rating"] = df_books["rating"].astype(str).str.strip().str.title()
    ratings_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df_books["rating"] = df_books["rating"].map(ratings_map).astype("Int64")

    return df_books
