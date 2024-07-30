from pathlib import Path
# pathlib - python docs
# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent) 
# path.with_name("file.txt")
# print(path.absolute())
# path.with_suffix(".txt")
# print(path)  

# path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
# print(path.iterdir())
# for p in path.iterdir():
#     print(p)
    
path = Path("ecommerce/__init__.py")
print(path.stat())