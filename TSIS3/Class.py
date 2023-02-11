#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1

class stri():
     def __init__(self):
         self.string=""

     def getString(self):
         self.string=input()
    
     def printstring(self):
         print(self.string.upper())

 a = stri()
 a.getString()
 a.printstring()


# In[ ]:


# 2

 class shape():
     def area(self):
         print(0)

 class square(shape):
     def __init__(self, lenght):
         super().__init__()
         self.lenght = lenght
     def area(self):
         print(self.lenght**2)

 class rectangle(shape):
     def __init__(self, width, lenght):
         super().__init__()
         self.width = width
         self.lenght = lenght

     def area(self):
         print(self.width*self.lenght)

 square = square(7)
 square.area()

 rectangle = rectangle(7,9)
 rectangle.area()


# In[ ]:


# 4

 import math
 class point():
     def __init__(self, x, y):
         self.x=x
         self.y=y
    
     def show(self):
         print(self.x, ";", self.y, sep="")

     def move(self,x,y):
         self.x=x
         self.y=y

     def dist(self, p2):
         print(math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2))


 a=point(1,1)
 a.show()
 a.move(2,2)
 a.show()
 b=point(2,2)
 a.dist(b)


# In[ ]:


# 5

 class account():
     def __init__(self,owner,balance):
         self.owner=owner
         self.balance=balance
    
     def deposit(self, amount):
         self.balance += amount

     def withdraw(self, sum):
         if(sum>self.balance):
             print("Withdraw is exceed the available balance.\n The available balance = ", self.balance)
         else:
             self.balance -= sum
             print("Withdrawal completed successfully!.")
             print("Remaining balance = ", self.balance)

 first=account("Dina", 1000000000)

 first.deposit(980000)

 first.withdraw(999999)


# In[ ]:


# 6

 def filter(list):
     result = []
     for i in list:
         count=0
         for j in range(1, i+1):
             if(i%j==0):
                 count += 1

         if(count==2):
             result.append(i)

     return result
                
 a=[1,2,4,7,8]

 print(filter(a))

