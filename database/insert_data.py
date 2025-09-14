import sqlite3
import pandas as pd
import os

def creation_bd(df_books: pd.DataFrame) -> sqlite3.Connection:
    """
    Crée un base de données SQLite dans le dossier `database/`et insère les données`
    du DataFrame dans un table nommée `book_store`.

    Si le dossier `database/` n'existe pas, il est créé automatiquement.

    Args:
        df_books (pd.DataFrame): DataFrame avec les données à insérer.

    Returns:
        sqlite3.Connection: Connection ouverte à la base de données `book_store.db`.
    
    Exemple:
        >>> conn = create_db(df)
        >>> conn.execute("SELECT COUNT(*) FROM book_store").fetchone()
        (50,)
    """

    # Création de la BDD
    connection = sqlite3.connect("database/book_store.db")
    cursor = connection.cursor()

    # Création manuelle de la table si elle n'existe pas
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS book_store (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   price REAL,
                   availability TEXT,
                   rating TEXT
                   )                       
    """)

    # Insertion des données
    df_books.to_sql('book_store', connection, if_exists='replace')
    return connection