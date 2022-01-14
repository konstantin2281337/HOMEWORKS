#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import Series, DataFrame


# In[12]:


movies = pd.read_table('D:\pan\movies.dat.txt', sep = '::', names = ['MovieID', 'Title', 'Tag'],
                      engine = 'python')
movies


# In[13]:


users = pd.read_table('D:\\pan\\users.dat.txt', sep = '::', names = ['UserID', 'Gender', 'Age', 'Occepation', 'ZipCode'],
                     engine = 'python')
users


# In[14]:


ratings = pd.read_table('D:\\pan\\ratings.dat.txt', sep = '::', names = ['UserID', 'MovieID', 'Rating', 'Timestap'],
                       engine = 'python')
ratings


# In[18]:


data = pd.merge(ratings, users)
data


# In[19]:


data = pd.merge(data, movies)
data


# In[23]:


# Средний рейтинг у мужчин и женщин
mean_rating = data.pivot_table('Rating', index = 'Title', columns = 'Gender', aggfunc = 'mean')
mean_rating


# In[24]:


# Сортировка по рейтингу у женщин
mean_rating_F = mean_rating.sort_values(by = 'F', ascending = False)
mean_rating_F


# In[25]:


# Средний рейтинг по возрастам
mean_rating_age = data.pivot_table('Rating', index = 'Title', columns = 'Age', aggfunc = 'mean')
mean_rating_age


# In[27]:


# Сортировка по рейтингу у самой возрастной группы
mean_rating_old = mean_rating_age.sort_values(by = 56, ascending = False)
mean_rating_old


# In[28]:


# фильмы, получившие >= 250 оценок
a = data.groupby('Title').size()
a[a >= 250]


# In[29]:


# Женские - высокие, мужские - низкие 
mean_rating['diff'] = mean_rating['F'] - mean_rating['M']
mean_rating.sort_values(by = 'diff', ascending = False).head(15)


# In[32]:


# Мужские - высокие, женские - низкие
mean_rating['diff'] = mean_rating['M'] - mean_rating['F']
mean_rating.sort_values(by = 'diff', ascending = False).head(15)


# In[ ]:




