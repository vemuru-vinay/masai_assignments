# TMDB EDA Assignment

import ast
import os
import sqlite3
from pathlib import Path

import pandas as pd
import requests

# ==========================
# 1. Setup & Configuration
# ==========================


def load_env_file():
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env_file()
API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise ValueError("TMDB_API_KEY was not found. Add it to the .env file.")

# ==========================
# 2. Fetch Data from TMDB API
# ==========================

url = "https://api.themoviedb.org/3/discover/movie"
params = {
    "api_key": API_KEY,
    "language": "en-US",
    "sort_by": "popularity.desc",
    "page": 1
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()
data = response.json()

movies = data.get("results", [])

# Convert to DataFrame
movies_df = pd.DataFrame(movies)

# Keep only relevant columns
movies_df = movies_df[[
    "id",
    "title",
    "release_date",
    "vote_average",
    "vote_count",
    "popularity",
    "genre_ids"
]]

print("Fetched Movies:", len(movies_df))
print("\nFetched Data Preview:")
print(movies_df.head())

# ==========================
# 3. Store in SQLite
# ==========================

conn = sqlite3.connect("tmdb_movies.db")

# Convert list columns to strings before saving to SQL
for col in movies_df.columns:
    if movies_df[col].apply(lambda x: isinstance(x, list)).any():
        movies_df[col] = movies_df[col].apply(lambda x: str(x) if isinstance(x, list) else x)

movies_df.to_sql("movies", conn, if_exists="replace", index=False)
conn.close()

print("Data saved to SQLite database.")

# ==========================
# 4. Load Data from SQLite
# ==========================

conn = sqlite3.connect("tmdb_movies.db")
loaded_df = pd.read_sql("SELECT * FROM movies", conn)
conn.close()

# Convert stored string values like "[28, 12]" back into Python lists
loaded_df["genre_ids"] = loaded_df["genre_ids"].apply(
    lambda value: ast.literal_eval(value) if isinstance(value, str) else value
)

# ==========================
# 5. EDA
# ==========================

# 5.1 Display first 5 rows
print("\nFirst 5 Rows:")
print(loaded_df.head())

# 5.2 Summary statistics
print("\nSummary Statistics:")
print(loaded_df.describe())

print("\nTop 5 Most Popular Movies:")
print(loaded_df[["title", "popularity"]].sort_values("popularity", ascending=False).head())

print("\nTop 5 Highest Rated Movies:")
print(
    loaded_df[["title", "vote_average", "vote_count"]]
    .sort_values(["vote_average", "vote_count"], ascending=[False, False])
    .head()
)

# 5.3 Count movies per genre

# TMDB genre mapping (static mapping)
genre_map = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}

# Explode genre_ids
genre_df = loaded_df.copy()
genre_df = genre_df.explode("genre_ids")

# Map genre IDs to names
genre_df["genre_name"] = genre_df["genre_ids"].map(genre_map)

# Count per genre
genre_counts = genre_df["genre_name"].value_counts()

print("\nMovies per Genre:")
print(genre_counts)

# 5.4 Missing values
print("\nMissing Values:")
print(loaded_df.isnull().sum())

# ==========================
# END OF NOTEBOOK
# ==========================
