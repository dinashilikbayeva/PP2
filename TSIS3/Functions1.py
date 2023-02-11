#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1
 def ounces(grams):
     return 28.3495231 * grams


 grams=float(input())
 print(ounces(grams))


# In[ ]:


# 2

 def centigrade(F):
     return (5 / 9) * (F - 32)

 F=int(input())
 print(centigrade(F))


# In[ ]:


# 3

 def puzzle(heads, legs):

     rabbits = int((legs-70)/2)
     chickens = int(heads - rabbits)

     return rabbits, chickens

 heads = int(input())
 legs=int(input())

 print(puzzle(heads, legs))


# In[ ]:


# 4

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


# In[ ]:


# 5

 from itertools import permutations
 def permut(string):
     p=permutations(string)
     print(list(p))

 a=str(input())
 permut(a)


# In[ ]:


# 6

 def reverse(string):
     reverse_list=string.split(" ")
     reverse_list.reverse()
     for i in reverse_list:
         print (i, end=" ")
    

 string = str(input())
 reverse(string)


# In[ ]:


# 7

 def has_33(nums):
     for i in nums:
         if(i+1<len(nums) and nums[i]==3 and nums[i+1]==3):
             return True
     return False

 print(has_33([3, 1, 3]))


# In[ ]:


# 8

 def spy_game(nums):

     count=0

     for i in nums:
         if(count==0 and i == 0):
             count+=1
         elif(count==1 and i==0):
             count+=1
         elif(count==2 and i==7):
             count+=1


     if(count==3):
         return True
     else:
         return False


 print(spy_game([1,2,4,0,0,7,5])) 
 print(spy_game([1,0,2,4,0,5,7])) 
 print(spy_game([1,7,2,0,4,5,0]))


# In[ ]:


# 9

 r=int(input())
 vol = lambda rad: (4/3) * 3.14 * pow(rad, 3)
 print(vol(r))


# In[ ]:


# 10

 def unique(list):
     uniqueList = []
     for i in list:
         if i not in  uniqueList:
             uniqueList.append(i)
     return uniqueList

 list=[11, 1, 3, 2, 1, 3, 4]
 print(unique(list))


# In[ ]:


# 11

 def palindron(string):
     if(string==string[::-1]):
         return True
     else:
         return False


 string=str(input())
 print(palindron(string))


# In[ ]:


# 12

 def histogram(list):
     for i in list:
         print("*"*i)

 histogram([4, 9, 7])


# In[ ]:


# 13
 import random
 print("Hello! What is your name?")
 name=input()

 attempts=0

 num = random.randint(1, 20)
 print("Well, KBTU, I am thinking of a number between 1 and 20.")
 print("Take a guess")

 tr = 0
 while(tr!=num):
     tr=int(input())
     if(tr<num):
         print("Your guess is too low.")
         print("Take a guess")
         attempts+=1

     elif(tr>num):
         print("Your guess is too high.")
         print("Take a guess")
         attempts+=1

     else:
         attempts+=1
         print("Good job, {fname}! You guessed my number in {fattempt} guesses!".format(fname = name, fattempt = attempts))
         break

