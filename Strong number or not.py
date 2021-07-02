#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input('enter number'))
sum=0
temp=n
while(n):
    i=1
    fact=1
    rem=int(n%10)
    while(i<=rem):
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=int(n/10)
if(sum==temp):
    print('is a strong number')
else:
    print('not a strong number')


# In[ ]:




