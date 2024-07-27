from pathlib import Path
# pathlib - python docs
path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent) 
path.with_name("file.txt")
print(path.absolute())
path.with_suffix(".txt")
print(path)  