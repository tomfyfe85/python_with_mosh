"Scratch module for working through lessons"


def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("fizzbuzz")
    if number % 5 == 0:
        print("buzz")
    if number % 3 == 0:
        print("fizz")

    print("not divisible by 3, 5 or both")


# if inout is divisble by 3 return fizz
# if it is divisible by 5 return buzz
# if it is divisble by 3 and 5 return fizzbuzz

fizz_buzz(31)
