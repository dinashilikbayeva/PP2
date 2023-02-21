
#1
n = int(input())
list=[i**2 for i in range(1, n+1)]

print(list)

#2
def generator(n):   
    for i in range (0, n+1):
        if i%2==0:
            yield i   

for i in generator(int(input())):
     print(i, end = ",")

#3
def generator(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i

for i in generator(int(input())):
    print(i, end = " ")

#4
a = int(input())
b = int(input())

def squares(a, b):
    for i in range(a, b+1):
        yield i**2

for i in squares(a, b):
    print(i, end = " ")

#5
def generator(n):
    for i in range(n, -1, -1):
        yield i

for i in generator(int(input())):
    print(i, end = " ")