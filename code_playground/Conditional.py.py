#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = int(input("Input: "))
if num > 0:
    print("Positive number")


# In[3]:


num = int(input("Input: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# In[5]:


num = int(input("Input: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    print("Not divisible by 5")


# In[11]:


num = int(input("Input: "))
if num % 3 == 0 and num % 7 ==0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible")


# In[12]:


num = int(input("Year: "))
if num % 4 == 0:
    print("Leap Year")
else:
    print("Not a leap year")


# In[13]:


num = int(input("Marks: "))
if num >= 35:
    print("Pass")
else:
    print("Fail")


# In[1]:


num = int(input("Input: "))
if (100 <= num <= 999):
    print("3 digit number")
else:
    print("not a 3 digit number")


# In[2]:


vow = ["a","e","i","o","u"]
vowel = input("Input: ")
if vowel in vow:
    print("is a vowel")
else:
    print("Not a vowel")


# In[3]:


num1 = int(input(""))
num2 = int(input(""))
if num1 > num2:
    print(num1,"is greater")
else:
    print(num2, "is greater")


# In[5]:


num1 = int(input(""))
num2 = int(input(""))
if num1 == num2**2:
  print("num1 is sq.root of num2")
else:
  print("no")  


# In[7]:


one = input("enter a string: ")
two = input("enter another string: ")
if one == two:
    print("two strings are equal")


# In[12]:


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

num = int(input("Enter a number: "))
if is_prime(num):
    print("prime")
else:
    print("not prime")
    


# In[25]:


def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num)


# In[28]:


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("enter a num: "))
if is_prime(num):
    print("prime")
else:
    print("no")


# In[33]:


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num)
        


# In[37]:


character = input(" ")
if character.isupper():
    print("it's uppercase")
else:
    print("no")


# In[39]:


tem = int(input("Enter temperature: "))
if tem > 30:
    print("it's hot")
else:
    print("not hot")


# In[ ]:




