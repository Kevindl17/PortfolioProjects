#!/usr/bin/env python
# coding: utf-8

# In[66]:


import json

file = open("employee.json")

data = json.load(file)
empi = input("Which employee number do you want to see (1-5), 6 for all: ")

if int(empi) <= 5:
    empo = "Emp0"+empi
    print("#"+empo, "is:", data[empo])
if int(empi) == 6:
    for i in range(1,6,1):
        empo = "Emp0"+str(i)
        print("#"+empo,"is:", data[empo])

file.close()


# In[ ]:




