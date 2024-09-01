#  name = "Memoona"
# print(name)

# Data Types
            # 1. Premitive: it stores only single value i.e; int, float etc
            # 2.Non-Premitive: it stores multiple values at the same time i.e; list, tuple, dictionary etc
# String: str
# Integer: int
# Float: float
# Boolean: bool

name: str = "Memoona"
age: int = 21
height: float = 5.2
status: bool = True
# print("My name is", name)
# print("My age is", age)
# print("My height is", height)
# print("My status is", status)

# print("My name is", name, "\nMy age is", age, "\nMy height is", height, "\nMy status is", status)
print("Doctor's advice")
# title() function
# convert string or sentence into a title format(first letter of each word is always capital)
place= "artificial intelligence"
print(place.title())

# Formatting string Method
print(f"My name is {name} and my age is {age}")

# alternative method of formatting string
print("I am {0} years old".format(age))

first_name = "Memoona"
last_name = "Zahur"
full_name = print(f"My full name is {first_name} {last_name}")

#rstrip and lstrip
name = "Memoona   "
print(name)
print(name.rstrip(), '.')

language = "     Python"
print("Amazing", language.lstrip())