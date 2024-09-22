# print("Hello World")
# print('0----')
# print(' ||||')
# print('*' * 10)
#-----------------
#
# price = 10
# name = 'Ashish'
# state = True
# rating = 4.9
# print(price , name , state, rating )
#-----------------
from multiprocessing.managers import convert_to_error

# myName = input('What is your name? ')
# myAge = input('What is your age? ')
# print ('Hi '+ myName + ' your age is ' +myAge)
#-----------------

# birth_year = input('birth year? ')
# print(type(birth_year))
# age = 2024 - int(birth_year)
# print(age)
#-----------------
#Task 1

# weight = input('What is your weight in pounds? ')
# weight = float(weight) / 2.205
# print('Your weight in Kg is ' , int(weight))

#-----------------

# course = "python's course for beginners"
# print(course)
# email = '''Hey,
#
# This is to inform that the assignment is completed successfully
#
# Thank you,
# Ashish'''
#
# print(email)
#-----------------

# course = 'Python for beginners'
#
# print(course[0:3])
# print(course[:3])
# print(course[0:])
# print(course[1:-1])
#-----------------

# first= 'Ashish'
# last = 'Kumar'
# # message = f'{first} [{last}] is a coder'
# print(f'{first} [{last}] is a coder')

#-----------------

# course = 'python for beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course)
# print(course.find('o'))
# print(course.replace('beginners', 'newbie'))
# print('python' in course)

#-----------------

# print(10//3) #// for absolute value
# x = 10
# x+=3
# print(x)
#print(round(2.9))
#-----------------

# import math
#
# print(math.ceil(2.9))

#-----------------

# is_hot = False
# is_cold = True
# if is_hot:
#     print('Drink plenty of water')
#     print("because it's a hot day")
# elif is_cold:
#     print("its cold day")
# else:
#     print('not today')
# print("Ok buddy")

#-----------------

# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"down_payment: ${down_payment}")

#-----------------

# has_high_income = True
# has_good_credit = False
#
# if has_high_income or has_good_credit:
#     print("Eligible for loan.")

#-----------------

# temperature = 35
#
# if temperature>35:
#     print("Hot day")
# else:
#     print("Cold day")

#-----------------

# i = 1
# while i<=5:
#     print('*' * i)
#     i = i+1
# print("Done")

#-----------------

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count<guess_limit:
#     guess = int(input('Guess: '))
#     guess_count +=1
#     if guess ==secret_number:
#         print('you won!')
#         break
# else:
#         print("You failed")

#-----------------

# for i in range(5,11,2):
#     print(i)

# prices = [10,20,30]
# total = 0
# for i in prices:
#     total +=i
# print(f"Total: {total}")
#
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

#------------------
#
# names = ['ashish', 'rohan', 'pranav']
# print(names[1])

#------------------

# myList = [1,2,3,4,5,6,7]
# max = myList[0]
# for i in myList:
#     if i>max:
#         largest_num = i
#     else:
#         continue
# print(largest_num)

#------------------

# appNum = [5,7,3,2,8]
# appNum.index(7)
# appNum.pop() #last item remove
# appNum.remove(5)
# # appNum.clear()
# print(appNum.count(5))
# appNum.sort()
# ap = appNum.copy()
# appNum.insert(3,6)
# print(appNum)

#------------------
# numbers = [2,2,4,6,3,4,6,1]
# uniques = []
# for i in numbers:
#     if i not in uniques:
#         uniques.append(i)
#
# print(uniques)

#------------------
#tuples immutable unlike list , cannot be changed
#or append, insert, remove, clear, pop. count and index is only available
#
# numbers = (1,2,3)
# coordinates = (1,2,3)
# x,y,z = coordinates #unpacking, can be done on list as well
# print(x,y,z)

#------------------
#Dictionary, each key should be unique

# customer = {
#     "name": "Ashish",
#     "age": 23,
#     "is_verified": True
#
# }
# print(customer["age"])

#function----------


# def greet_user():
#     print("Hello")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user()
# print("finish")

# def addition(a,b):
#     print(a+b)
#
# addition(3,5)

# def greet_user(name,surname):
#     print(f"Hello {name} {surname}")
#     print("Welcome")
#
# greet_user("John", "smith")

#
# def square(number):
#     return number * number
#
# print(square(25))

#Exception---------
# try:
#     age = int(input("Age: ")) #if we write string here then error
#     print(age)
# except ValueError: #ZeroDivisionError error also,
#     print("Write only numbers")

#classes-----------

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10,20)
# # point1.draw()
# # point1.move()
# # point1.x = 1
# # point1.y = 20
# # print(point1.x)
# # print(point1.y)
# print(point1.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}.")
#
# john = Person("John Smith")
# john.talk()

#inheritence-------

# class Mammal:
#     def walk(self):
#         print("Walk")
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#
# class Cat(Mammal):
#     pass
#
# dog1 = Dog()
# dog1.bark()

#modules-----------

# import converters
# from converters import lbs_to_kg
# ans = converters.kg_to_lbs(23)
# print(lbs_to_kg(25))
#
# from ecommerce.shipping import calc_shipping
# calc_shipping()

# import random
#
# for i in range(3):
#     print(random.randint(10,20))
#
# from pathlib import Path
#
# path = Path("ecommerce")
# print(path.exists())

