import requests
import json
import pandas as pd

def get_books_from_api():
    """
    Récupère les livres depuis l'API Google Books.

    Cette fonction envoie une requête HTTP à l'API Google Books avec les paramètres spécifiés 
    (ici : recherche de livres payants sur le thème "food") et récupère la liste brute des livres.

    Returns:
        list: Une liste de dictionnaires correspondant aux livres retournés par l'API.
              Si la requête échoue, une liste vide est retournée.
    """
    url = "https://www.googleapis.com/books/v1/volumes"

    params = {
        "q": "food",
        "filter": "paid-ebooks",
        "maxResults": 40,
        "orderBy": "relevance"
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data_books_raw = response.json()
        data_books = data_books_raw.get("items", [])
        return data_books
    else:
        return []


def create_list_of_books(data_books):
    """
    Transforme les données brutes récupérées depuis l'API en une liste de dictionnaires structurés.

    Chaque dictionnaire contient uniquement les informations pertinentes : 
    le titre, le prix et la note moyenne du livre.

    Args:
        data_books (list): Liste de dictionnaires bruts issus de l'API Google Books.

    Returns:
        list: Une liste de dictionnaires nettoyés avec les clés 'title', 'price' et 'rating'.
    """
    book_list = []
    for book in data_books:
        book_dict = {
            "title": book.get('volumeInfo', {}).get('title'),
            "price": book.get('saleInfo', {}).get('listPrice', {}).get('amount'),
            "rating": book.get('volumeInfo', {}).get('averageRating')
        }
        book_list.append(book_dict)
    return book_list


def create_df_of_books(book_list):
    """
    Convertit une liste de dictionnaires de livres en DataFrame pandas.

    Args:
        book_list (list): Liste de dictionnaires contenant les informations des livres.

    Returns:
        pd.DataFrame: Le DataFrame contenant les colonnes 'title', 'price' et 'rating'.
    """
    df = pd.DataFrame(book_list)
    return df


