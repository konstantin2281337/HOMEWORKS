#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def f(x):
    a = []
    for i in range(x):
        a.append(random.choice([1, -1]))
    a.append(0)
    return a

y, x = input('y x = ').split()
y = int(y)
x = int(x)

b = []
a = 0

for j in range(y):
    b.append(f(x))
b.append([0] * (x + 1))

for j in range(y + 1):
    b[j][x]  = b[j][0]
for k in range(x + 1):
    b[y][k] = b[0][k]
for j in range(y + 1):
    print(b[j])
for j in range(y):
    for k in range(x):
        a += b[j][k] * b[j + 1][k]
        a += b[j][k] * b[j][k + 1]
print(a)


# In[ ]:




