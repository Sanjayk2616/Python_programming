"""
   comparision operators :- comparision operators are used for the comparision and returns true or false
   ==   checks if both values are equal
   !=   checks if values are not equal
   >    checks if the first value is greater
   <    checks if  the first value is smaller    
   >=   checks if the first value is greater or equal
   <=   checks if the first value is smaller or equal

   logical operators :- logiacal operators are used to perform on logic verification result is always true or false
   and :- returns true if both the conditions are true or else returns false
    T T -> T
    T F -> F
    F T -> F
    F F -> F

   or :-  returns true if any of the conditions are true or else returns false
    T T -> T
    T F -> T
    F T -> T
    F F -> F

   not  returns vice versa of the result

   assignment operators :- these are used to assign or update value of a  variable
   = -> assign
   += -> add & assign
   -= -> subtract & assign
   *= -> multiply & assign
   **= -> exponentiate & assign
   /= -> divide & assign
   //= -> floor divide & assign
   %= -> modulus & assign

   membership operators
   it checks if a value exists within a sequence (like a list , string , tuple)
   in - returns true if the value exists in the sequence
   not in - returns true if the value doesn't exists in the sequence 

   identity operators :- are used to check whether two variables refer to the same object in memory
   is - returns true if both refer to the same object
   is not - returns true if theyrefer to different objects




"""
#take two inputs as a,b is 20,30 perform all comparision operators
a = 20
b = 30
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#take the inputs as weights of three persons and check all are same or not
#check weight2 is less than or equal to weight3
wp1 = 30
wp2 = 30
wp3 = 40
print(wp1 == wp2 == wp3)
print(wp2 <= wp3)
print(wp1 >= wp3)

#questions 1 to 3
x = 10
y = 20
print(x == y)
print(x >= y)
print(x <= y)

#q4
x = int(input())
print(x >= 40)

#q5
age = int(input())
print(age < 18)

#q6
a = int(input())
a += 10
print(a)

#q7
b = int(input())
b += 5
print(b)

#q8
c = int(input())
c += 5
print(c)

#q9
age = int(input())
print(age > 18 and age < 60)

#q10
a = int(input())
b = int(input())
print(a > 10 and b >10)

#q11
a = int(input())
print(a < 0 or a > 100)

#q12
age = int(input())
print(age >= 18 and age < 60) 

#q13
age = 22
exp = 3
print(age > 18 and exp >2)

#q14
a = 45
b = 60
print(a < b and (a+b) > 100)

#q15
s1 = 78
s2 = 85
s3 = 62
print((a > 70 and b > 70) or c > 80) # ((a and b) > 70 or c > 80)

#q16
temp = 32
hum = 65
print((temp>25 and temp<40) and (hum < 70))

#q17
age = 17
print(age < 18 or age > 60)

#q18
num1 = 25
num2 = 40
print(num1 != num2)
print(num2 > 30)

#assignment operators
#q
x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x **= 3
print(x)
x //= 3
print(x)
x %= 3
print(x)

#membership operators
l = [5,6,7,8,9]
print(5 in l)
print(10 in l)
print(20 not in l)
print(5 not in l)

name = "Sanjay"
print ( 'x' in name)
print( 'a' not in name)
print('S' in name)

#identity operators
a = [1,2,3]
b = 1
c = a #reassigning
d = [1,2,3]
print(a is b)
print(a == d)
print(a is c)
print(a is  d)
print(a is not c)
print (a is not d)


#questions
#q1
s = "Python"
print('a' in s)

#q2
list = [1,3,5,7,9]
print(5 in list)

#q3
course = ["python","c","c++"]
print('java' in course)

#q4
tuple = (5,10,15,20)
print(10 in tuple)

#q5
colors = ["blue","green","yellow"]
print("red" in colors)

#q6
a = 5
b = 5
print(a is b)

#q7
a = [1,2,3]
b = 1
print(a is b)

#q8
a = [1,2]
b = [1,2]
print(a is b)

#q9
a = int(input())
print(a > 10 and a < 50)

#q10
age = int(input())
print(age >= 18 and age < 60)
