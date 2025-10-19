# 📚 Scraping — Google Books → CSV & SQLite

Ce projet illustre un petit pipeline éducatif pour **collecter → nettoyer → stocker** des données de livres à partir de l’**API Google Books**, avec export en **CSV** et insertion dans une base **SQLite**.

---

## 🚀 Fonctionnalités

- Récupération de livres via **Google Books API** avec les paramètres : `q=food`, `filter=paid-ebooks`, `orderBy=relevance`, `maxResults=40`  
- Transformation de la réponse API → **liste de dictionnaires** → **DataFrame pandas**
- Nettoyage des données : suppression des valeurs manquantes (`price`, `rating`), ajout d’une colonne `availability`, réinitialisation des index
- Sauvegarde en **CSV brut** (`data/data_api.csv`)
- Insertion dans une **base SQLite** (`book_store.db`, table `book_store`)
- Fonction principale `run_api_pipeline()` qui exécute toutes les étapes automatiquement

---

## 🗂️ Structure du projet

```
scraping/
├─ data/                  # Exports CSV
├─ get_data/              # Récupération de données (API / scraping)
├─ process_data/          # Nettoyage et typage
├─ pipelines/             # Fonctions de chargement et pipeline complet
├─ notebooks/             # (Optionnel) Exploration
├─ main.py                # Point d’entrée principal
└─ requirements.txt       # Dépendances Python
```

---

## ⚙️ Installation

**Prérequis :** Python 3.10 ou plus

```bash
git clone https://github.com/emese007/scraping.git
cd scraping

# (Optionnel) environnement virtuel
python -m venv .venv
source .venv/bin/activate  # sous Windows : .venv\Scripts\activate

# Installation des dépendances
pip install -r requirements.txt
```

Si le fichier `requirements.txt` est incomplet, ajoutez :  
```
pandas
requests
```

---

## ▶️ Exécution du pipeline

Lancer simplement :

```bash
python main.py
```

Le script :
1. interroge l’API Google Books,  
2. crée une liste de dictionnaires,  
3. convertit la liste en DataFrame,  
4. enregistre les données brutes en CSV,  
5. nettoie les données,  
6. insère les résultats dans la base SQLite.

---

## 🧾 Données générées

- **CSV brut :** `data/data_api.csv`  
- **Base SQLite :** `data/book_store.db` (table `book_store`)

Colonnes principales :  
- `title` → titre du livre  
- `price` → prix (float)  
- `rating` → note moyenne (float ou entier)  
- `availability` → booléen (par défaut `False`)

---

## 👤 Auteurs

Projet réalisé par [@emese007]
Formation IA - Simplon Montpellier (2025–2026)
