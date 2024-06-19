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
nums = [1,2,3]
print(*nums)
# same as ... in JS

vals = [*range(5), *"hi marge"]
#  can unpack any iterables
print(vals)
# [0, 1, 2, 3, 4, 'h', 'i', ' ', 'm', 'a', 'r', 'g', 'e']

# combine lists
first = [1,2]
second = [3,4]

values = [*first, *second]
print(values)
# --> [1, 2, 3, 4]

# # unpacking dictionaries
# **

one = dict(x=1)
two = dict(x=10, y=2)
combined = {**one, **two, "z":4}
print(combined)
# if two keys are the same it takes the last key