from pathlib import Path
from time import ctime
import shutil


Path(r"C:\Program Files\Tesseract-OCR")  # "r"用于防止转义
Path()
Path("Python\Learning\PythonStandardLibrary")
Path.home()
Path(r"Python\Learning")/"Python"
Path()/"Python/Learning"
# Search python3 pathlib
# https://docs.python.org/3/library/pathlib.html

path = Path("Moduleusing/__init__.py")
print(path.exists())  # False
path = Path(r"C:\Program Files\Tesseract-OCR")
print(path.exists())  # True

print(path.is_file())  # False
print(path.is_dir())  # True
print(path.name)  # Tesseract-OCR(文件名)
print(path.stem)  # Tesseract-OCR(无扩展名的文件名)
print(path.suffix)
print(path.parent)  # C:\Program Files

path = Path(
    r"D:\000_PersonalDocuments\1_StudyMaterials\Programming\Python\Learning\ModulesUsing\sales.py")
pathT = path.with_suffix(".txt")
print(pathT)
# D:\000_PersonalDocuments\1_StudyMaterials\Programming\Python\Learning\ModulesUsing\sales.txt
path = Path(
    r"Python\Learning\PythonStandardLibrary\PathlibTest")

# Making dealing millions of paths efficient, using generator object
iterPath = path.iterdir()
print(iterPath)  # <map object at 0x00000245196D1B70>
for i in iterPath:
    print(i)
# Files in path's folder
pyFiles = [p for p in path.glob("*")]
print(pyFiles)
# getfiles,*for all files.Other keywords a=can be used such as "*.py"

print(path.stat())  # os.stat_result(st_mode=16895, st_ino=562949953456531, st_dev=2619971258019858446, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1755492174, st_mtime=1755445583, st_ctime=1755445499)
print(ctime(path.stat().st_birthtime))  # Sun Aug 17 23:44:59 2025

path = Path("Python\Learning\ModulesUsing\ecommerce\__init__.py")
print(path.read_text())
# Return the content

target = Path(
    r"Python\Learning\PythonStandardLibrary\PathlibTest\Copyof__init.txt")
target.write_text(path.read_text())

# or:
shutil.copy(path, target)
