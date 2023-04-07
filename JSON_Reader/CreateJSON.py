#!/usr/bin/env python
# coding: utf-8

# In[23]:


import json

Employee = {
    "Cindy": {"team": "marketing", "role": "graphic designer", "salary": "$50.000"},
    "Jacob": {"team": "sales", "role": "sales manager", "salary": "$90.000"},
    "Bert": {"team": "marketing", "role": "social media marketer", "salary": "$70.000"},
    "Gerald": {"team": "people", "role": "president", "salary": "$120.000"},
    "Billy": {"team": "people", "role": "human resource", "salary": "$80.000"},
    "Gerard": {"team": "sales", "role": "sales intern", "salary": "$40.000"}}

test_ist = {"Emp01", "Emp02", "Emp03", "Emp04", "Emp05", "Emp06"}

x = json.dumps(Employee)
    
res = {}
for key, ele in zip(test_ist, Employee.items()):
    res[key] = dict([ele])

print(res)

