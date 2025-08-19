import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1991},
    {"id": 2, "title": "Kindergarten Cop", "year": 1997}
]

data = json.dumps(movies)
print(data)
Path("Python\Learning\PythonStandardLibrary\movies.json").write_text(data)
# D:\000_PersonalDocuments\1_StudyMaterials\Programming\Python\Learning\PythonStandardLibrary\movies.json
data = Path("Python\Learning\PythonStandardLibrary\movies.json").read_text(data)
movies = json.loads(data)
print(movies[0])
# get an array of dictionaries
