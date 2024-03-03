# Variables and datatypes

from datetime import date

a = "Abir Sarkar"


def func(string):
    print("Hello", string)


# func(a)

b = 123
c = "Abir Sarkar"

# print(b + b)

# print(type(a), type(b), type(c))


list1 = [8, 8.2, [-4, 5], ["Banana", "Apple"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dist1 = {"name": "Abir Sarkar", "age": 26, "canVote": True}
print(dist1)

# The bellow part is just for fun and experiment purpose only
today = date.today()

print("Today is :", today)
print(today.strftime("%d/%m/%Y"))
