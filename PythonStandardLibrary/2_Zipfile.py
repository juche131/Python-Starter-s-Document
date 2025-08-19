from zipfile import ZipFile
from pathlib import Path

zip = ZipFile("files.zip", "w")
for path in Path("Python\Learning\PythonStandardLibrary\PathlibTest").rglob("*.*"):
    zip.write(path)
zip.close()
# Don't forget to close
# Or using this:
with ZipFile("files.zip", "w") as zip:
    for path in Path("Python\Learning\PythonStandardLibrary\PathlibTest").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("Python\Learning\PythonStandardLibrary\PathlibTest")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("")