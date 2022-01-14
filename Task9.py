#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Airplane():
    def __init__(self, name, plane_type, cargo_capacity, max_speed, fuel_capacity):
        self.name = name
        self.plane_type = plane_type
        self.cargo_capacity = cargo_capacity
        self.max_speed = max_speed
        self.fuel = 0 
        self.fuel_capacity = fuel_capacity
        self.status = 'work'
        
        
        
    def fill_plane(self):
        self.fuel = self.fuel_capacity
        print('%s is full now' %self.name)
        
    def flight(self):
        if(self.fuel > 0 or self.status == 'work'):
            print('%s ready fly' %self.name)
        else:
            print('please fuel %s or fix the %s' %self.name)
            
    def breake_plane(self):
        self.status = 'broke'
        print('%s the crashes' %self.name)
        
    def fix_plane(self):
        self.status = 'work'
        print('the %s is fully fixed and ready to fly' %self.name)
        
    def transportation(self):
        if(self.cargo_capacity > 100000 and self.fuel > 0 and self.status == 'work'):
            print('%s can carry out transportation' %self.name)
        else:
            print('%s cannot carry out transportation, choose another plane or fuel the plane or fix the %s' %self.name)
            
    def war(self):
        if(self.plane_type == 'Military' and self.fuel > 0 and self.status == 'work'):
            print('%s in full combat readiness' %self.name)
        else:
            print('%s does not fit choose another plane or fuel the Ty-160 or fix the Ty-160' %self.name)
            
    def transportation_passengers(self):
        if(self.name == 'Boeing737' and self.status == 'work'):
            print('%s ready to fly' %self.name)
        else:
            print('Choose another the plane or fix the Boeing737')
            
    def transportation_fast(self):
        if(self.max_speed > 1000 and self.status == 'work'):
            print('the selected %s is suitable for a fast flight' %self.name)
        else:
            print('Choose another the plane or fix the %s' %self.name)
    
    
        


# In[17]:


plane1 = Airplane('Boeing737', 'Passenger', 53000, 1020, 500)
plane2 = Airplane('Boeing747-400', 'Cargo', 400000, 918, 1500)
plane3 = Airplane('Ty-160', 'Military', 40000, 2000, 1000)


# In[18]:


plane1.breake_plane()


# In[19]:


plane1.transportation_passengers()


# In[20]:


plane1.fix_plane()


# In[23]:


plane1.transportation_passengers()


# In[24]:


plane2.war()


# In[25]:


plane3.war()


# In[26]:


plane3.fill_plane()


# In[27]:


plane3.war()


# In[ ]:




