#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = [1, 2, 3, 4, 5, 6, 7]

s.insert(0, s[len(s) - 1])
s.insert(len(s), s[1])
s.pop(len(s) - 2)
s.pop(1)

print("".join(map(str, s)))


# In[ ]:




