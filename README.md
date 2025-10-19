# 📚 Scraping — Google Books → CSV & SQLite

A small, educational pipeline that **collects → cleans → stores** book data (theme *food*) from the **Google Books API**, exports a raw CSV, and loads records into a **SQLite** database.

> Built for learning purposes (data collection / light ETL).

---

## ✨ Features

- Fetches books from **Google Books API** with parameters like `q=food`, `filter=paid-ebooks`, `orderBy=relevance`, `maxResults=40`.
- Transforms API results → **list of dicts** → **pandas DataFrame**.
- Cleans/normalizes fields (drop missing `price`/`rating`, add `availability`, reset index).
- Saves a **raw CSV** (`data/data_api.csv`).
- Loads the cleaned DataFrame into **SQLite** (`book_store.db`, table `book_store`).
- A pipeline function `run_api_pipeline()` that chains the steps end‑to‑end.

---

## 🗂️ Repository structure (typical)

```
scraping/
├─ data/                  # CSV exports (e.g., data_api.csv)
├─ get_data/              # Data collection (API / scraping)
├─ process_data/          # Cleaning / typing helpers
├─ pipelines/             # Load functions and orchestration
├─ notebooks/             # Optional exploration
├─ all_books.csv          # Sample consolidated dataset (optional)
├─ book_store.db          # SQLite database (if present)
├─ main.py                # Entry point that runs the pipeline
└─ requirements.txt       # Python dependencies
```

> Folder names may vary slightly in your repo; adjust paths in examples accordingly.

---

## 🔧 Requirements & Setup

- **Python 3.10+** recommended

```bash
git clone https://github.com/emese007/scraping.git
cd scraping

# (Optional) virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

If your `requirements.txt` is minimal, consider adding:
```
pandas
requests
```

(Optional) If you externalize configuration later:
```
python-dotenv
```

---

## ⚙️ Configuration

Public Google Books queries like those used here **do not require an API key**.  
You can customize in `get_books_from_api`:

- `q` (query): default `"food"`  
- `filter`: e.g. `"paid-ebooks"`  
- `orderBy`: e.g. `"relevance"`  
- `maxResults`: up to 40 per page

**Paths** (defaults used in examples):
- Raw CSV: `data/data_api.csv`
- SQLite DB: `book_store.db` (you can pass a different path to the loader function)

---

## ▶️ Usage

### 1) Run the full pipeline

```bash
python main.py
```

Expected flow:
1. Fetch from Google Books API
2. Convert to list → DataFrame
3. Save raw CSV (`data/data_api.csv`)
4. Clean/prepare the DataFrame
5. Insert rows into SQLite `book_store`

### 2) Use functions modularly (example)

```python
from get_data.api import get_books_from_api, create_list_of_books, create_df_of_books
from process_data.clean import prepare_api_data  # API-oriented cleaner
from pipelines.load import insert_api_data_to_database
from pipelines.io import save_raw_to_csv  # or wherever your save function lives

data_books = get_books_from_api()
if not data_books:
    raise SystemExit("No data returned from API.")

book_list = create_list_of_books(data_books)
df = create_df_of_books(book_list)

save_raw_to_csv(df)            # writes to data/data_api.csv
df_clean = prepare_api_data(df)  # dropna on price/rating, availability=False

insert_api_data_to_database(df_clean, db_path="book_store.db")
```

> Ensure the `data/` folder exists or create it programmatically before saving the CSV.

---

## 🧾 Data model (typical columns)

- `title` *(str)*: Book title from `volumeInfo.title`
- `price` *(float)*: Price from `saleInfo.listPrice.amount` (if available)
- `rating` *(float or Int64)*: `volumeInfo.averageRating` (0–5); you may choose to round to integer
- `availability` *(bool/int)*: Defaulted to `False` in the API pipeline (no stock info in Google Books); feel free to define a custom rule

---

## 🗄️ SQLite Notes

- Table name: `book_store`
- Default loader uses `pandas.DataFrame.to_sql(..., if_exists="append")` to append rows.
- You may want to pre-create the table with a schema (types & constraints) if you need strict typing/keys.

---

## 🧪 Quick checks

- `data/data_api.csv` is created and non-empty.
- `book_store.db` contains table `book_store` with the expected number of rows.
- Sanity check types: `price` numeric, `rating` numeric, `availability` boolean-ish (0/1).

---

## 🩺 Code review & cleanup suggestions

1. **Typo:** `process_scarping_data` → **`process_scraping_data`**.  
2. **API vs HTML-scrape logic:**  
   - A function that removes `£` and maps ratings `{One..Five}` is for **HTML scraping** (e.g., *Books to Scrape*), not for **Google Books API**.  
   - For API data, `price` is already numeric and `averageRating` is numeric (float). Keep `rating` as float or convert to integer if needed.
3. **`availability` consistency:**  
   - API data does not provide `"In stock"`; either keep a default (`False`) or derive a rule (e.g., `availability = price.notna()`).
4. **Insert count:**  
   - If you need “inserted now” rather than “total rows”, capture a count **before and after** the insert and return the difference.
5. **Robust CSV save:**  
   - Ensure the folder exists before writing: `os.makedirs("data", exist_ok=True)`.
6. **Safer JSON access:**  
   - Use `.get("items", [])` on the API response to avoid `KeyError` when no results.

> Consider splitting cleaners into two paths: `prepare_api_data_api()` vs `prepare_scraped_html_data()` to avoid confusion.

---

## 🛣️ Roadmap

- CLI via `argparse` (query params, paths, DB file)
- Logging (`logging`) with INFO/ERROR for each stage
- Tests with `pytest` and a temp SQLite DB
- Dockerfile for reproducible runs
- Optional: simple schema migrations

---

## 📝 License

MIT (adjust if needed).

---

## 👤 Author

[@emese007](https://github.com/emese007)
