# 1. Simple Message

name: str = "My name is Memoona Zahur."
print(name)

# 2. Simple Messages

introduction: str = "My name is Memoona Zahur."
print(introduction)

introduction = "I am a student of BSCS"
print(introduction)

# 3. Personal Message

person_name: str = "Mona"
print(f"Hello {person_name}, would you like to learn some Python today?")

# 4. Name Cases

name = "meMOONa zaHuR"
print(name.lower())
print(name.upper())
print(name.title())

# 5. Famous Quote

quote = "The only way to do great work is to love what you do."
author = "Steve Jobs"

print(f'{author} once said, "{quote}"')

# 6. Famous Quote 2

famous_person = "Ayn Rand"
message = f'{famous_person} once said, "A creative man is motivated by the desire to achieve, not by the desire to beat others."'
print(message)

# 7. Stripping Names

name = "     \n\tMemoona Zahur     \t\n"
print(name)
print("The name after lstrip():", name.lstrip())
print("The name after rstrip():", name.rstrip())
print("The name after strip():", name.strip())

# 8. Variable Sum

x: int = 5
y: int = 10
z: int = 15
sum = x+y+z
print(f"The sum of {x}, {y} and {z} is: {sum}")

# 9. Variable Swap

a: int = 5
b: int = 7
print(f"""Before Swapping:
      The value of a is: {a}
      The value of b is: {b}""")
a, b = b, a
print(f"""After Swapping:
      The value of a is: {a}
      The value of b is: {b}""")

# 10. Favorite Color

favorite_color: str = "Black"
print(f"My favorite color is: {favorite_color}")
color = favorite_color
print(f"I like {color} color.")

# 11. Changing Pet Name

pet_name = "Buddy"
pet_name = "Max"
print(f"My pet's new name is: {pet_name}")

# 12. Observing Name Error

weather = "Sunshine"
print(weather)
# print(sunshine)   # This will cause a Name Error

# 13. Reassigning Score

score = 100
print(f"The initial score is: {score}")
score = 500
print(f"The new score is: {score}")

# 14. City Name

city: str = "Lahore"
print(f"My favorite city is: {city}")

# 15. Title Case Text

text = "python programming"
print(f"In title case: {text.title()}")

# 16. Lowercase Conversion

language: str = "PYthOn pROGraMmING"
print(f"In lower case: {language.lower()}")

# 17. Uppercase Conversion

language = "PyThon progRaMMing"
print(f"In upper case: {text.upper()}")

# 18. Current Temperature

temperature = 25
print(f"The current temperature is {temperature} degrees.")

# 19. Printing a Poem

poem = """Let me but do my work from day to day,
In field or forest, at the desk or loom,
In roaring market-place or tranquil room;
Let me but find it in my heart to say,
When vagrant wishes beckon me astray,
"This is my work; my blessing, not my doom;
Of all who live, I am the one by whom
This work can best be done in the right way."
"""

print(poem)