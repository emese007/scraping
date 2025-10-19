import pandas as pd
from get_data.get_api_data import get_books_from_api, create_list_of_books, create_df_of_books
from process_data.process_api_data import prepare_api_data, save_raw_to_csv
from database.insert_api import insert_api_data_to_database

def run_api_pipeline() -> pd.DataFrame:
    """
    Exécute le pipeline d'ingestion des données livres depuis l'API jusqu'à la base SQLite.

    Étapes :
      1) Récupère les données brutes via `get_books_from_api()`.
      2) Transforme la réponse en liste de dictionnaires avec `create_list_of_books(...)`.
      3) Construit un DataFrame via `create_df_of_books(...)`.
      4) Sauvegarde un dump CSV des données brutes avec `save_raw_to_csv(df)`.
      5) Prépare/Nettoie les données avec `prepare_api_data(df)`.
      6) Insère en base SQLite via `insert_api_data_to_database(df_clean, db_path=...)`.

    Args:
        None

    Returns:
        pd.DataFrame: Le DataFrame nettoyé (`df_clean`) prêt à être réutilisé en aval.
                      (Les données sont également insérées en base.)

    Side Effects:
        - Écrit un fichier CSV : `data/data_api.csv`.
        - Insère/append des lignes dans la table `book_store` de la base SQLite.

    Raises:
        Aucune exception n'est levée ici par conception ; la fonction intercepte
        les erreurs d'insertion en base pour afficher un message et retourne quand même,
        afin de ne pas interrompre un flux batch. Si tu préfères, tu peux supprimer
        le bloc try/except pour laisser remonter les erreurs.
    """
    data_books = get_books_from_api()
    
    if not data_books:
        print("Aucune donnée récupérée. Arrêt du pipeline.")
        return pd.DataFrame()  # retour « vide » explicite
    
    # Créer la liste de dictionnaires
    books_list = create_list_of_books(data_books)
    
    # Créer le DataFrame
    df = create_df_of_books(books_list)
    
    # Étape 2 : Sauvegarder les données brutes
    save_raw_to_csv(df)
    
    # Étape 3 : Préparer les données avant de les mettre en base
    df_clean = prepare_api_data(df)
    
    # Étape 4 : Insérer les données en base 
    try:
        nb_livres_ajoutes = insert_api_data_to_database(
            df_clean,
            db_path="/home/emese/Briefs_test/scraping/book_store.db"
        )
        print(f"Insertion terminée. Nombre total de lignes en base : {nb_livres_ajoutes}.")
    except Exception as exc:
        # Garde le pipeline “tolérant aux erreurs” d’insertion
        print(f"Erreur lors de l'insertion en base : {exc}")

    return df_clean
