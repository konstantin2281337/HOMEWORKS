#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import random


# In[15]:


#Создание матрицы заполненной 1 и -1 в случайном порядке

x = int(input('размерность матрицы: '))
k = [1, -1]
matrix = np.zeros((x, x))
for i in range(x):
    for j in range(x):
        matrix[i, j] = random.choice(k)
print(matrix)


# In[16]:


Sum = 0
for a in range(x):
    for b in range(x):
        Sum += matrix[a][b]*matrix[a][b-1]+matrix[a-1][b]*matrix[a][b]
print(Sum)

