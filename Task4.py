#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[4]:


a = int(input())
b = int(input())

m = [[randint(0, 101) for i in range(a)] for j in range(b)]
print(m)


# In[ ]:




