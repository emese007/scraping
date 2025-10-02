import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(pages:int, base_url: str) -> pd.DataFrame:
    """
    Scrape des informations sur plusieurs pages du site books.toscarpe.com
    et retourne un DataFrame brut contenant les données extraites.

    Args:
        pages(int): nobre de la page à scraper
        base_url(str): URL de base avec un placeholder "{}" pour le numèro de page.
                       Exemple: "http://books.toscrape.com/catalogue/page-{}.html"
        
    Returns: 
        pd.DataFrame: DataFrame contenant les colonnes suivantes:
            -title (str) : titre du livre
            -price (str) : prix du livre 
            -rating (str) : rating du livre (par exemple "Three")
            -availability (str) : disponibilité du livre (par exemple "In stock")

    Raises:
        requests.exeptions.HTTPError: Si une requête échoue
    """

    #Scraping des données sur plusieurs pages

    all_books =[]

    for page_num in range(1, pages + 1):
        url = base_url.format(page_num)
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        #Extraction des données des livres
        books = soup.select("article.product_pod")
        for book in books:
            title = book.h3.a['title']
            price = book.find("p",class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            rating = book.find("p", class_="star-rating")["class"][1]

         # Ajout des données extraites au DataFrame
            all_books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability
            })

    return pd.DataFrame(all_books)