#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10


# In[2]:


type(a)


# In[3]:


b=10.56


# In[4]:


type(b)


# In[5]:


c="Shubham"


# In[6]:


type(c)


# ## 1 Python is dynamic programming language 

# In[7]:


a=123


# In[8]:


type(a)


# In[9]:


b=123.456


# In[10]:


type(b)


# In[11]:


c="I am learnin g machine learning"


# In[12]:


type(c)


# ## 2 Size of the data dynamically managed 

# In[13]:


a=200000000


# In[15]:


import sys
sys.getsizeof(a)


# In[ ]:


b=1234567890


# In[16]:


import sys
sys.getsizeof(b)


# In[ ]:


c=12345543216789098765


# In[17]:


import sys
sys.getsizeof(c)


# ## 3 data types are unbounded

# ## Bool

# In[18]:


True+False 


# In[19]:


True+True


# In[20]:


False+False


# In[23]:


x=1


# In[24]:


import sys
sys.getsizeof(x)


# ## String 
# 

# In[25]:


a="Shubham"


# In[26]:


type(a)


# In[27]:


a="Shubham"


# In[28]:


print(a)


# In[29]:


type(a)


# In[30]:


msg="Shubham's python classes"


# In[32]:


msg


# In[33]:


msg='Shubham"s python classes'


# In[34]:


msg


# In[35]:


type(msg)


# In[36]:


y="Let's learn python"


# In[37]:


print(y)


# In[39]:


y="""Let's learn "python" """


# In[40]:


type(y)


# In[41]:


print(y)


# In[42]:


y='let\'s learn "python" '


# In[43]:


type(y)


# In[44]:


print(y)


# In[45]:


my_string="My name is shubham"


# In[47]:


print(my_string)


# ## Type conversion 

# In[48]:


a=100


# In[49]:


type(a)


# In[50]:


b=float(a)


# In[51]:


print(b)


# ## Concatination 

# In[52]:


a='10'


# In[53]:


b='20'


# In[54]:


a+b


# In[55]:


x=int('10')


# In[56]:


type(x)


# In[58]:


y=int('20')


# In[59]:


type(y)


# In[60]:


x+y


# ## Input()

# ## You have to have two input from the user and you have to subtract it

# In[68]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=a-b
print(c)


# In[ ]:





# In[ ]:




