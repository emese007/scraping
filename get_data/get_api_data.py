import requests
import json
import pandas as pd

def get_books_from_api():
    """
    Collects the books from API Google Books
    Create a list of books 
    """

    url = "https://www.googleapis.com/books/v1/volumes"

    params = {"q": "food",
            "filter": "paid-ebooks",
            "maxResults": 40,
            "orderBy": "relevance"
             }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
            data_books_raw = response.json()
            data_books = data_books_raw["items"]
            return data_books
    else:
          return[]
    
def create_list_of_books(data_books):
      """
      Create a list of dictionnaires from the collected data of books
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
      Create a dataframe from the list of dictionnaires of books
      """
      df = pd.DataFrame(book_list)
      return df
