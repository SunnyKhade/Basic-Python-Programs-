#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input('enter Nth number'))
a=0
b=1
sum=0
print('finonacci series upto',n,':')
while(sum<=n):
    print(sum,end=' ')
    a=b
    b=sum
    sum=a+b

