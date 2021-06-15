#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Enter number')
n=int(input())
flag=False
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            flag=True
        break

if flag:
    print('Not prime')
else:
    print('Prime')
        


# In[ ]:




