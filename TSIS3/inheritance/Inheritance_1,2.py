#!/usr/bin/env python
# coding: utf-8

# In[8]:


#exercise 1
class Student(Person)


# In[9]:


#exercise 2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

