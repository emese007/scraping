import pandas as pd

def prepare_api_data(df):
    """
    Prépare les données avant leur insertion dans la base de données.

    Cette fonction nettoie le DataFrame brut en :
    - supprimant les lignes où les colonnes 'price' ou 'rating' sont manquantes,
    - réinitialisant les index,
    - ajoutant une colonne 'availability' initialisée à False.

    Args:
        df (pd.DataFrame): Le DataFrame brut obtenu depuis l'API.

    Returns:
        pd.DataFrame: Le DataFrame nettoyé et prêt pour l'insertion en base de données.
    """

    df_clean = df.dropna(subset=["price", "rating"])
    df_clean = df_clean.reset_index(drop=True)
    df_clean["availability"] = False

    return df_clean

def save_raw_to_csv(df):
    """
    Sauvegarde les données brutes issues de l'API dans un fichier CSV local.

    Cette fonction enregistre le DataFrame fourni dans le dossier 'data' sous le nom 'data_api.csv'.
    Si le dossier n'existe pas, il doit être créé avant l'appel de cette fonction.

    Args:
        df (pd.DataFrame): Le DataFrame contenant les données brutes à sauvegarder.

    Returns:
        None
    """
    df.to_csv('data/data_api.csv', index=False)
