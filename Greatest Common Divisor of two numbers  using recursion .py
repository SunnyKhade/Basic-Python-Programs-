#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gcd(a,b):
    if(b!=0):
        return gcd(b,a%b)
    else:
        return a

print('Enter two numbers : ')
a = int(input())
b = int(input())

gcd=gcd(a,b)
print('GCD is', gcd)


# In[ ]:




