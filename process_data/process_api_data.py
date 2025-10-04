import pandas as pd

def prepare_api_data(df):
    """
    Prepare the data before insertion into a database
    """

    df_clean = df.dropna(subset=["price", "rating"])
    df_clean = df_clean.reset_index(drop=True)
    df_clean["availability"] = False

    return df_clean

def save_raw_to_csv(df):
    """
    """
    df.to_csv('data/data_api.csv', index=False)
