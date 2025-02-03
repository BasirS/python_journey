#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.executable)

get_ipython().system('pip install playsound')


# In[2]:


import time
from playsound import playsound
from IPython.display import clear_output

def alarm(hours):
    time_elapsed = 0
    
    while time_elapsed < hours:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = hours - time_elapsed
        days_left = time_left // 24
        hours_left = time_left % 24
        
        clear_output(wait=True)
        print(f"{days_left:02d}:{hours_left:02d}")
        
    playsound("wawawa.wav")

days = int(input("How many days to wait: "))
hours = int(input("How many hours to wait: "))
total_hours = days * 24 + hours
alarm(10)