import pandas as pd
from get_data.get_api_data import get_books_from_api, create_list_of_books, create_df_of_books
from process_data.process_api_data import prepare_api_data, save_raw_to_csv
from database.insert_api import insert_api_data_to_database

def run_api_pipeline():
    """
    """
    data_books = get_books_from_api()
    
    if not data_books:
        print("Aucune donnée récupérée. Arrêt du pipeline.")
        return
    
    # Créer la liste de dictionnaires
    books_list = create_list_of_books(data_books)
    
    # Créer le DataFrame
    df = create_df_of_books(books_list)
    
    # Étape 2 : Sauvegarder les données brutes
    save_raw_to_csv(df)
    
    # Étape 3 : Préparer les données avant de les mettre en base
    df_clean = prepare_api_data(df)
    
    # Étape 4 : Insérer les données en base 
    nb_livres_ajoutes = insert_api_data_to_database(df_clean, db_path="/home/emese/Briefs_test/scraping/book_store.db")
    
    return df_clean