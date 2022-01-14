#!/usr/bin/env python
# coding: utf-8

# In[3]:


from random import randint


# In[6]:


def f(I, Friend):
    Iw = 'Ты выиграл'
    Fw = 'Ты проиграл'
    if I == Friend:
        return('Ничья')
    elif(I == 0 and Friend == 1) or (I == 1 and Friend == 2) or (I == 2 and Friend == 0):
        return(Iw)
    else:
        return(Fw)
    
s = ['Камень', 'Ножницы', 'Бумага']
I_word = str(input('Камень, Ножницы, Бумага? \n'))
I_move = s.index(I_word)

F_move = randint(0, 2)
F_word = s[F_move]

print('Friend move - ', F_word, '\n', f(I_move, F_move))
    


# In[ ]:




