#!/usr/bin/env python
# coding: utf-8

# ### Task_1

# In[1]:


product_id = int(input("Enter Product ID: "))

product_name = input("Enter product Name: ")

price = float(input("Enter Price: "))

categories = input("Enter Categories (comma-separated): ").split(',')

available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

discount_percentage = float(input("Enter Discount Percentage: "))

features_input = input("Enter Product Features (comma-separated): ")
product_features = set(features_input.split(','))

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}


# ### Task_2

# 1. Using comma separation

# In[8]:


print("1. Using Comma Separation (sep=',')\n")
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")


# 2. Using %

# In[11]:


print("Product Discount: %.2f%%" % discount_percentage)


# Using f-strings

# In[12]:


print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")


# 4. Using .format()

# In[13]:


print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details["Name"],
    supplier_details["Contact"],
    supplier_details["Location"]
))


# In[ ]:




