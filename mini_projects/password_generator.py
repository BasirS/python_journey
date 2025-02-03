#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string

def gen_pwd(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special
        
    pwd = ""
    criteria = False
    pwd_number = False
    pwd_special = False
    
    while not criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            pwd_number = True
        elif new_char in special:
            pwd_special = True
        
        criteria = True
        if numbers:
            criteria = pwd_number
        if special_char:
            criteria = criteria and pwd_special

    return pwd
            
min_length = int(input("Enter the minimum length: "))
required_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
required_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

pwd = gen_pwd(min_length, required_number, required_special)
print("The generated password is:", pwd)