#1
import math

degree = int(input())
radian = math.radians(degree)
print(radian)

#2
height = int(input())
a = int(input())
b = int(input())

print((a+b) * height / 2)

#3
sides = float(input())
lenght = float(input())

apothem = lenght / 2 * math.tan(math.pi/sides)

S = apothem * sides*lenght / 2
print(math.ceil(S))

#4
length = float(input())
height = float(input())

print(length*height)