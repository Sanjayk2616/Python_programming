'''
 dynamic inputs
 list
 l = list(int,input().split())

 tuple
 t = tuple(int,input().split())
'''
l = list(input().split())
print(l)
l1 = list(map(int,input().split()))
print(l1)

t = tuple(input().split())
t1 = tuple(map(int,input().split()))
print(t)

s = set(map(int,input().split()))
print(s)

#questions
#q1
a , b = 10 , 20
print(a & b)
print(a | b)
print(a ^ b)

#q2
a = int(input())
print(bin(a))
print(a << 2)



