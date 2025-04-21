#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check_product_availability(quantity):
    if quantity > 10:
        return "Product is available."
    elif 1 <= quantity <= 10:
        return "Product is in limited quantity."
    else:
        return "Product is out of stock."


quantity = int(input("Enter the quantity of the product: "))


status = check_product_availability(quantity)
print(status)


# In[2]:


def check_product_availability(quantity, is_prime_member, has_discount_coupon):
    if quantity > 10:
        stock_status = "Product is available."
    elif 1 <= quantity <= 10:
        stock_status = "Product is in limited quantity."
    else:
        stock_status = "Product is out of stock."

    if is_prime_member and has_discount_coupon:
        discount_status = "You have a discount coupon and are a Prime member! Enjoy your perks."
    elif is_prime_member:
        discount_status = "You are a Prime member. No discount coupon applied."
    elif has_discount_coupon:
        discount_status = "You have a discount coupon. No Prime membership benefits."
    else:
        discount_status = "No discounts available."

    return stock_status, discount_status


quantity = int(input("Enter the quantity of the product: "))
is_prime_member = input("Are you a Prime member? (yes/no): ").lower() == 'yes'
has_discount_coupon = input("Do you have a discount coupon? (yes/no): ").lower() == 'yes'


stock_status, discount_status = check_product_availability(quantity, is_prime_member, has_discount_coupon)


print(stock_status)
print(discount_status)


# In[3]:


def check_number(number):
    if number > 0:
        return "The number is positive"
    elif number < 0:
        return "The number is neg"
    else:
        return "The number is zero."


number = float(input("Enter a number: "))


result = check_number(number)
print(result)


# In[4]:


#................................FORLOOP..............
for var in range(0,101,2):
    print(var)


# In[5]:


for var in range(10,0,-1):
    print(var)


# In[6]:


for var in range(1,11):
    print(f' 3*{var} = {3*var}')


# In[7]:


l = [1,2,3,4]
for var in l:
    print(var)


# In[8]:


l = 'vasuki'
for var in range(0, len(l)):
    print(var, l[var])


# In[9]:


l = {1:2,3:4,5:6}
for ind,kv in enumerate(l):
    print(kv, l[kv] ,'is at index:', ind)


# ### WHILE LOOP
# 

# In[10]:


max_attempts = 5
cur_attempts = 0

d_pwd = 'python123'

while cur_attempts < max_attempts:
    pwd = input("enter the password: ")
    if d_pwd == pwd:
        print("Login Successful")
        break
    else:
        print("Try Again")

