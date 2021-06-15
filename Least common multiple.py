#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Enter two numbers : ')
a = int(input())
b = int(input())
lcm=1
if(a>b):
    lcm=a
else:
    lcm=b
while(1):
    if(lcm%a==0 and lcm%b==0):
        print('lcm is',lcm)
        break
    lcm=lcm+1


# In[ ]:




