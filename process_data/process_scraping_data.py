import pandas as pd

def process_scarping_data(df_books: pd.DataFrame) -> pd.DataFrame:
    """Convert the types of the DataFrame columns to appropriate types.

    Args:
        df_books (pd.DataFrame): The DataFrame containing book data.

    Returns:
        pd.DataFrame: The DataFrame with converted types.
    """
    # Conversion de title en chaîne de caractères
    df_books["title"] = df_books["title"].astype(str)
    
    # Convertir la colonne price en type décimal
    df_books["price"] = df_books["price"].astype(str).str.removeprefix("£")
    df_books["price"] = df_books["price"].astype(float)

    # Fonction pour convertir la valeur de availability en booléen
    def convert_availability(value : str) -> bool:
        if value == "In stock":
            return True
        else:
            return False

    # Convertir la colonne availability en booléen (True/False)
    df_books["availability"] = df_books["availability"].apply(convert_availability)

    df_books["rating"] = df_books["rating"].astype(str).str.strip().str.title()
    ratings_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df_books["rating"] = df_books["rating"].map(ratings_map).astype("Int64")

    return df_books