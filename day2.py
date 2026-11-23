"""
DATA TYPES
WHAT ARE DATA TYPES IN PYTHON?
A DATA TYPES DEFINES:
     - WHAT KIND OF VALUE IS STORED
     - HOW THE MEMORY IS ALLOCATED
     - WHETHER THE VALUE CAN BE MODIFIED OR NOT
     - HOW PYTHON INTERNALLY MANAGES THE DATA

TYPES OF DATA TYPES IN PYTHON:
1. NUMERIC DATA TYPES
   - INTEGER [INT] [EXAMPLE: 1, 2, 3]
   - FLOAT [FLOAT] [EXAMPLE: 1.5, 2.7]
   - COMPLEX [COMPLEX] [EXAMPLE: 1+2j]

2. SEQUENCE DATA TYPES they accept duplicate values
   - STRING [STR] [EXAMPLE: "Hello", 'World']
   - LIST [LIST] [EXAMPLE: [1, 2, 3], ['a', 'b', 'c']]
   - TUPLE [TUPLE] [EXAMPLE: (1, 2, 3), ('x', 'y', 'z')]
   
   
- SET [SET] [EXAMPLE: {1, 2, 3}, {'a', 'b', 'c'}]
- DICTIONARY [DICT] [EXAMPLE: {'key1': 'value1', 'key2': 'value2'}]
- BOOLEAN [BOOL] [EXAMPLE: 0, 1, True, False]
- NONE [NONE] [EXAMPLE: NULL]
    """

# numeric datatypes
a = 2
b = 3.10
c = 5+4j
print(type(a))
print(type(b))
print(type(c))

#questions
#q1
age = int(input())
print(age)
print(type())

#q2
height = float(input())
print(height)
print(type(height))

#q3
a = int(input())
b = int(input())
sum = int(input())
difference = int(input())
production = int(input())
division = float(input())

#q4
salary = float(input())
print(salary)
print(type(salary))
print(12*salary)

#q5
a = int(input())
b = float(input())
c = complex(input())
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#sequence datatypes
a = "world5"
b = [1,4,5,67,5]
c = (1,2,3)
print(type(a))
print(type(b))
print(type(c))

#questions
#q6
movie_name = input()
print(movie_name)
print(len(movie_name))
print(type(movie_name))

#q7
fruits = list(input())
print(fruits)
print(len(fruits))
print(type(fruits))

#q8
city = tuple(input())
print(city)
print(len(city))
print(type(city))

#q9
name = input()
age = int(input())
city = input()
print(age)
print(name)
print(city)

#q10
list = list(input())
tuple = tuple(input())
print(list)
print(tuple)

#set
a = {1,5,7,7,8,9}
print(type(a))
print(a)

#dict
b = {(1,2),(2,45),(9,54)}
print(type(b))

#boolean
a = True
b = False
print(type(a))
print(type(b))

#none
a = None
print(type(a))
 