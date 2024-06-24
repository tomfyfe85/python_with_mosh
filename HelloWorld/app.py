"Notes"


# list comprehension

# items = [
#     ("Product 1", 10),
#     ("Product 2", 800),
#     ("Product 3", 8),
# ]

# prices: list = []

# x = list(filter(lambda item: item[1] >= 10, items))
# print(x)

# y = [item for item in items if item[1] >= 10]


# zip function

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip("abc", list1, list2)))


# Stacks - LIFO last in first out - take from the back

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.pop()
# if not browsing_session:
#     print(browsing_session[-1])


# Queues - FIFO first in, first out - take from the front
# from collections import deque
# queue: deque[int] = deque([])
# # queue.append(1)
# # queue.append(2)
# # queue.append(3)
# # queue.popleft()
# print(queue)

# if not queue:
#     print('empty')

# tuples - read only list
# use tuples to prevent accidental errors

# swapping variables

# x = 10
# y = 11

# z = x
# x = y
# y = z

# in python
# x, y = y, x
# # y, x is a tuple
# print(x, y)

# arrays
# for large data types  - 10,000 or more numbers
# from array import array
# # https://docs.python.org/3/library/array.html - look up for type codes
# numbers = array("i", [1,2,3])
# every element must be of the type specified ie "i"

# Sets
# unordered collection of items, they are un-indexed
# list with no duplicates - removes dupes --> {1,2,3,4,5}
# numbers = [1, 1, 2, 3, 4, 5]
# first = set(numbers)
# second = {1, 2, 4, 8, 9}
# # print(first)
# # print(first | second)
# # # --> {1, 2, 3, 4, 5, 8, 9}
# # print(first & second)
# # --> intersection of the two sets
# # {1, 2, 3, 4, 5, 8, 9}
# # {1, 2, 4}

# # difference between two sets
# print(first - second)
# # --> {3, 5}

# # returns elements which are not in both sets
# print(first ^ second)
# # {3, 5, 8, 9}

# Sets are not indexed - to get index put the set in a list


# dictionaries
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# # same output
# print(point.get("x"), 0)
# # --> 1
# # 0 here is an example of a default return IE if "x" doesn't exist return 0
# point["z"] = 20
# del point["x"]
# print(point)
# # --> {'y': 2, 'z': 20}

# # looping over dictionaries
# for key in point:
#     print(key, point[key])

# # or use .items()

# for key, value in point.items():
#     print(key, value)

# # -->
# # y 2
# # z 20

# dictionary comprehensions
# values = {x: x*2 for x in range(5)}
# print(values)
# --> {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# generator expressions
# these generate a new value per iteration, rather than store all the values like a list
# looks like a list comp but with () instead of []
# use this this save memory/increase efficiency


# unpacking operator
# nums = [1,2,3]
# print(*nums)
# # same as ... in JS

# vals = [*range(5), *"hi marge"]
# #  can unpack any iterables
# print(vals)
# # [0, 1, 2, 3, 4, 'h', 'i', ' ', 'm', 'a', 'r', 'g', 'e']

# # combine lis ts
# first = [1,2]
# second = [3,4]

# values = [*first, *second]
# print(values)
# # --> [1, 2, 3, 4]

# # # unpacking dictionaries
# # **

# one = dict(x=1)
# two = dict(x=10, y=2)
# combined = {**one, **two, "z":4}
# print(combined)
# # if two keys are the same it takes the last key

# EXERCISE

# get the most repeated char in this text


# from pprint import pprint

# sentence = "This is a common interview question"

# # print(striped)
# char_frequency: dict = {}

# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
50
# # print(char_frequency)

# newSort = char_frequency.items()

# char_freq = sorted(char_frequency.items(),
#                     key=lambda kv: kv[1],
#                     reverse=True)
# print(char_freq[0])
# # print('Most repeated character:',newTups[-1][1], f'\nRepeated {newTups[-1][0]} times')

# pprint(char_frequency, width=1)


# EXCEPTIONS

#  - Handle exceptions:
# Basic structure
# try:
#     age = int(input("age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age")
#     # ex is type of error
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions werer thrown")


# Handling different exceptions
# try:
#     age = int(input("age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("No exceptions were thrown")

# cleaning up

# try:
#     file = open("app.py")
#     age = int(input("age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()

# The With Statement
# try:
#     with open("app.py") as file:
#         print("file opened")
#     age = int(input("age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("No exceptions were thrown")

# Raising exceptions - not the most efficient way
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less")
#     return 10/age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# cost of raising exceptions
# from timeit import timeit

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less")
#     return 10/age
#     try:
#         calculate_xfactor(-1)
#     except ValueError as error:
#         pass
# """

# code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     return 10 / age

# xfactor = calculate_xfactor(-1)
# if xfactor == None:
#     pass
# """

# print("first code:", timeit(code1, number=10000))
# print("second code:", timeit(code2, number=10000))
# These prints so the program's runtime

# raising exceptions should be done with caution as they can increase run time
#  Think twice when using them