"Scratch module for working through lessons"


# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user['id'])


save_user(id=1, name="admin")
