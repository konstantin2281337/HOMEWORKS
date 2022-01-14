#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input())
def f(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * f(num - 1)
print(f(num))


# In[ ]:




