import sqlite3
import json
from pathlib import Path

movies = json.loads(
    Path("Python\Learning\PythonStandardLibrary\movies.json").read_text())

print(movies)

# Learn SQLite first!
