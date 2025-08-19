from zipfile import ZipFile
from pathlib import Path


with ZipFile("files.zip") as zip:
    print(zip.namelist())
    ['Python/Learning/PythonStandardLibrary/PathlibTest/1.txt', 'Python/Learning/PythonStandardLibrary/PathlibTest/2.txt', 'Python/Learning/PythonStandardLibrary/PathlibTest/3.txt', 'Python/Learning/PythonStandardLibrary/PathlibTest/4.txt',
        'Python/Learning/PythonStandardLibrary/PathlibTest/5.txt', 'Python/Learning/PythonStandardLibrary/PathlibTest/6.txt', 'Python/Learning/PythonStandardLibrary/PathlibTest/Copyof__init.txt', 'Python/Learning/PythonStandardLibrary/PathlibTest/AA/q.txt']
    # Donot use '/' here
    info = zip.getinfo(
        "Python/Learning/PythonStandardLibrary/PathlibTest/Copyof__init.txt")
    print(info.file_size)  # 90
    print(info.compress_size)  # 90
    zip.extractall("extract")
