#1

def mult(list):
    result = 1
    for i in list:
        result = result * i
    
    return result

list = [int(input()) for i in range(int(input()))]

print(mult(list))

#2

str = str(input())

count1 = 0
count2 = 0

for i in str:
    if i.isupper():
        count1 += 1
    if i.islower():
        count2 += 1

print(count1, " ", count2)

#3
str = str(input())
str2=reversed(str)

if list(str)==list(str2):
    print("Palindrome")
else:
    print('Not palindrome')

#4
from time import sleep  
import math

number = int(input())
milliseconds = int(input())

sleep(milliseconds/1000)

print("Square root of {n} after {m} miliseconds is {sq}".format(n = number, m = milliseconds, sq = math.sqrt(number)))

#5
def true(tuple):
    for i in tuple:
        if not i:
            return False
    return True

tuple = (True, True)

print(true(tuple))