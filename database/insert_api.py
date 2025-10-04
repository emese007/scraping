import pandas as pd
import sqlite3

def insert_api_data_to_database(df_clean: pd.DataFrame, db_path: str = "/home/emese/Briefs_test/scraping/book_store.db") -> int:
   
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    df_clean.to_sql('book_store', connection, if_exists='append', index=False)
    cursor.execute("SELECT COUNT(*) FROM book_store")
    books_inserted = cursor.fetchone()[0]

    connection.close()
    return books_inserted