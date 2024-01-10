#!/usr/bin/env python
# coding: utf-8

# ## For_ Loop & Range functions

# In[1]:


word="Shubham"


# In[2]:


for s in word:
    print(s)


# In[3]:


x=[1,2,3,"a"]


# In[4]:


type(x)


# In[5]:


for y in x:
    print(y)


# In[6]:


fruits =["apple","orange","mango",2,True]


# In[11]:


for i in fruits:
    print(i)


# In[13]:


fruits=["apple","orange","mango","papaya","grapes"]
is_grapes=False

for i in fruits:
    if i =="grapes":
        is_grapes= True 
        print("Grapes found in the fruits list")
        break
        
if is_grapes == False:
    print("No grapes found in the list")


# In[1]:


my_list =[14,10,12,17]
low_bound=10
upp_bound=20
for i in my_list1:
    if i <low bound or i> upp bound:
        print("all elements are not in the limit")
        break
else:
    print("all the elements are in the list are in the list")


# ## Range Function 

# In[ ]:


## Inbuilt function in pythoy
range() function in python which return range object
## this function is useful to generate sequence of numbers in form list


# In[6]:


a=range(20)


# In[7]:


print(a)


# In[8]:


list(a)


# range(start,stop,step)
# 
# #range(20)
# #range(1,20)
# #range(1,20,2)

# In[11]:


b=range(4)


# In[12]:


print(b)


# In[13]:


list(b)


# In[15]:


for i in b:
    print(i)


# In[17]:


c=range(15)
d=list(c)


# In[18]:


for i in c:
    print(i)


# In[19]:


x=range(7)


# In[22]:


for i in x:
    print(i)


# range(start,stop,step)

# In[25]:


y=range(6)


# In[26]:


for i in y:
    print(i)


# In[28]:


y=range(1,6)


# In[29]:


for i in y:
    print(i)


# In[30]:


y=range(1,6,2)


# In[31]:


for i in y:
    print(i)


# In[32]:


x=range(-10)


# In[33]:


list(x)


# In[40]:


m=range(1)


# 1=list(m)

# In[41]:


1=list(m)


# In[42]:


print(m)


# In[43]:


a=range(10,1)


# In[44]:


print(a)


# In[45]:


a=range(-10,3)


# In[46]:


list(a)


# In[47]:


a=range(1,10,2)


# In[48]:


list(a)


# In[3]:


numbers = [1,2,3]
alpha = ['a','b','c']

for n in numbers:
    print(n)
    for ch in alpha:
        print(ch)


# In[2]:


for i in range(3):
    for j in range(3):
        print('*',end='')  
        print()


# In[1]:


for i in range(4):
    for j in range(i+1):
        print("*",end = " ")  
        print("")


# In[63]:


## Write a program to accept the integer from user and display all numbers from 1 to to that number. Reapet the proccess
## Until the user enter 0


# In[ ]:


d=1
while d!=0:
    d=int(input("enter number"))
for i in range(1,d+1):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




