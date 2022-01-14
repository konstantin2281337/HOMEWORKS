#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


cols = [ 'name', 'gender', 'birth' ]
years = range(1880, 2010 + 1)
pieces = []
for i in years:
    df  = pd.read_table('C:\\Users\\Delta\\Desktop\\Work\\Prog\\babynames\\yob%d.txt'%i, sep = ',', engine = 'python', names = cols)
    df['year'] = i
    pieces.append(df)
    data = pd.concat(pieces, ignore_index = True)
countb = data.pivot_table('birth', index = 'gender', aggfunc = 'sum')
countb      # Общее число младенцев


# In[6]:


data    # Таблица


# In[9]:


import matplotlib.pyplot as plt


# In[12]:


gender1 = data.pivot_table('birth', index = 'year', columns = 'gender', aggfunc = 'sum')
gender1
a, b = gender1['M'], gender1['F']
c = years
plt.plot(c, a, label = 'Male', color = 'purple', lw = 2)
plt.plot(c, b, label = 'Female', color = 'gold', lw = 2)
plt.legend()
plt.show()
# График родившихся младенцев по полу


# In[17]:


data['proportion'] = data['birth']/sum(data['birth'])
data   
# Доля младенцев получивших данное имя, относительно числа родившихся


# In[26]:


import pylab

nameb = data.pivot_table('birth', index = 'year', columns = 'name', aggfunc = 'sum')
pylab.subplot(2, 2, 1)
pylab.plot(c, nameb['Johnny'], color = 'purple')
pylab.title('Johnny')
pylab.subplot(2, 2, 2)
pylab.plot(c, nameb['Natalie'], color = 'gold')
pylab.title('Natalie')
pylab.subplot(2, 2, 3)
pylab.plot(c, nameb['Bob'], color = 'green')
pylab.title('Bob')
pylab.subplot(2, 2, 4)
pylab.plot(c, nameb['Konstantin'], color = 'red')
pylab.title('Konstantin')
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)   # Нашёл в интернете, как увелить расстояние между графиками

# графики общего кол-ва младенцев получавших следующие имена


# In[28]:


nameb = data.pivot_table('proportion', index = 'year', columns = 'name', aggfunc = 'sum')
pylab.subplot(2, 2, 1)
pylab.plot(c, nameb['Johnny'], color = 'purple')
pylab.title('Johnny')
pylab.subplot(2, 2, 2)
pylab.plot(c, nameb['Natalie'], color = 'gold')
pylab.title('Natalie')
pylab.subplot(2, 2, 3)
pylab.plot(c, nameb['Bob'], color = 'green')
pylab.title('Bob')
pylab.subplot(2, 2, 4)
pylab.plot(c, nameb['Konstantin'], color = 'red')
pylab.title('Konstantin')
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)

# графики относительной доли младенцев получавших данные имена


# In[29]:


a = []
for i in range(1880, 2010 + 1):
    b = data[data['year'] == i]
    b.sort_values('birth', ascending = False)
    a.append(b.head(1))
c = pd.concat(a, ignore_index = True)
del c['proportion']
del c['gender']
c
 # Самые популярный в каждом году имена


# In[ ]:




