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
