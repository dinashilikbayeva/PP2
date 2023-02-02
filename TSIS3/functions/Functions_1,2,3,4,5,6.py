#!/usr/bin/env python
# coding: utf-8

# In[3]:


#exercise 1
def my_function():
  print("Hello from a function")


# In[4]:


#exercise 2
def my_function():
  print("Hello from a function")

my_function()


# In[18]:


#exercise 3
def my_function(fname, lname):
  print(fname)
fname = str(input())
lname = str(input())
my_function(fname, lname)


# In[16]:


#exercise 4
def my_function(x):
  return x + 5
x = int(input())
my_function(x)


# In[19]:


#exercise 5
def my_function(*kids):
  print("The youngest child is " + kids[2])

kids = ("Saltanat", "Ganiya", "Snezhana")
my_function(*kids)


# In[27]:


#exercise 6
def my_function(**kid):
  print("Her last name is " + kid["lname"])
my_function(fname = "Snezhana", lname = "Shukurova")







