import pandas as pd
import sqlite3

def insert_api_data_to_database(df_clean: pd.DataFrame, db_path: str = "/home/emese/Briefs_test/scraping/data/book_store.db") -> int:
    """
    Insère les données nettoyées provenant d'une API dans une base de données SQLite.

    Cette fonction prend un DataFrame nettoyé (df_clean) et l'ajoute à la table 'book_store' 
    de la base de données spécifiée. Si la table existe déjà, les nouvelles lignes sont ajoutées 
    sans écraser les données existantes.

    Args:
        df_clean (pd.DataFrame): Le DataFrame contenant les données prêtes à être insérées.
        db_path (str, optional): Le chemin complet vers la base de données SQLite.
            Par défaut : "/home/emese/Briefs_test/scraping/book_store.db".

    Returns:
        int: Le nombre total d'enregistrements présents dans la table 'book_store' 
             après l'insertion des nouvelles données.
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    df_clean.to_sql('book_store', connection, if_exists='append', index=False)
    cursor.execute("SELECT COUNT(*) FROM book_store")
    books_inserted = cursor.fetchone()[0]

    connection.close()
    return books_inserted