# from ecommerce.shopping import sales
# print(dir(sales));

# from pathlib import Path

# # pathlib - python docs
# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
# print(path.iterdir())
# for p in path.iterdir():
#     print(p)

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

# py_files = [p for p in path.rglob("*.py")]
# print(py_files)

# from time import ctime

# path = Path("ecommerce/__init__.py")
# print(ctime(path.stat().st_ctime))

# # zip files
# from zipfile import ZipFile

# # with ZipFile("files.zip", "w") as zip:
# #     for path in Path("ecommerce").rglob("*.*"):
# #         zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")


# CSVs
# import csv

# # with open("data.csv", "w") as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["transaction_id", "product_id", "price"])
# #     writer.writerow([100, 1, 5])
# #     writer.writerow([100, 2, 15])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# JSON
# import json
# from pathlib import Path

# # movies = [
# #     {"id": 1, "title":"Terminator", "year": 1984 },
# #     {"id": 2, "title":"Kindergarten Cop", "year": 1993 }
# # ]

# # data = json.dumps(movies)
# # Path("movies.json").write_text(data)

# # to read json
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies[1]["title"])

# SQLlite

# import sqlite3
# import json
# from pathlib import Path

# # movies = json.loads(Path("movies.json").read_text())
# # print(movies)

# # with sqlite3.connect("db.sqlite3") as  conn:
# #     command = "INSERT INTO Movies VALUES(?,?,?)"
# #     for movie in movies:
# #         conn.execute(command, tuple(movie.values()))
# #     conn.commit()


# with sqlite3.connect("db.sqlite3") as  conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print(movies)


# time and datetime
# import time

# print(time.time())

# import random
# import string

# print(random.random())
# print(random.randint(1, 100))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# # random password
# # creates array of n of k, from string argument
# print(random.choices("abcdefghi", k=4))
# # .join to make into a random string
# print("".join(random.choices("abcdefghi", k=4)))
# #  string library
# print("".join(random.choices(string.ascii_letters + string.digits, k=21)))

# nums = [1, 2, 3, 4]
# random.shuffle(nums)
# print(nums)

# PIP
# import requests
# response = requests.get("http://google.com")
# print(response)

