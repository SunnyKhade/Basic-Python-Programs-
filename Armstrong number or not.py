#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math 
number=int(input('Enter a number'))
result=0
n=0
temp=number

while(temp!=0):
    temp=int(temp/10)
    n=n+1

temp=number
while(temp!=0):
    remainder=temp%10
    result=result+math.pow(remainder,n)
    temp=int(temp/10)
    
if(result==number):
    print('is an Armstrong number')
else:
    print('not an Armstrong number')


# In[ ]:




