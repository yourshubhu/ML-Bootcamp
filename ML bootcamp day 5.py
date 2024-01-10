#!/usr/bin/env python
# coding: utf-8

# ## Class 5

# ## Conditional statement & Looping concept 

# In[1]:


print("Hello")


# In[2]:


name="Shubham"


# In[3]:


print("Hello",name)


# In[4]:


print("Hello %s" %(name))


# In[5]:


a=10


# In[6]:


print("Value of a is %d" %a)


# In[7]:


a=10


# In[8]:


print(a)


# ## Format specifier 

# In[10]:


name


# In[11]:


print("Hello %s" %(name))


# In[12]:


print("Hello %s How are you" %(name))


# In[13]:


name


# In[14]:


last_name='sali'


# In[15]:


print("Hello %s %s how are you" %(name,last_name))


# In[ ]:





# In[16]:


a=10


# In[17]:


print("value of a is %d" %(a))


# In[ ]:





# In[18]:


a=10
name="Shubham"
b=29.5


# ## Simple pythonic way 

# In[19]:


print("value of a is",a,"name is",name,"value of b is",b)


# In[ ]:





# ## With format specifier

# In[20]:


var=10
name="Shubham"


# In[21]:


a=100


# In[22]:


print(a)


# In[23]:


print("value of a",a)


# In[25]:


print("value of a is %d" %a)


# In[26]:


print("value of a is {}".format(a))


# In[27]:


b=200


# In[30]:


print("value of a is {} value of b is {}".format (a,b))


# In[31]:


name="Ganesh"
age=27


# In[32]:


print("name is {} age is {}".format(name,age))


# In[33]:


print("name is {name} age is {age}".format(name,age))


# In[35]:


print("name is {0} age is {1}".format(name,age))


# In[36]:


print("name is {n} age is {a}".format(n=name,a=age))


# In[ ]:





# ## Decision control statement 

# In[37]:


x=50


# In[38]:


if x>50:
    print("We are in first if")
if x==50:
    print("We are in second if")
if x<50:
    print("We are in third if")


# In[39]:


if x>50:
    print("We arev in")
if x<50:
    print("We are in second if")
else:
    print("We are out")


# In[40]:


if a>50:
    print("We are in first if")
elif a<50:
    print("We are in second if")
elif a==50:
    print("We are in third if")
else:
    print("We are out")


# In[ ]:


if x>50:
    print("We arev in")
if x<50:
    print("We are in second if")
else:
    print("We are out")


# ## Shubham
# 
# ## Second one is complete block of excecution

# ## Practice que
# 
# ## 1) Accept an integer from the user and check whether it is an evwn odd

# In[44]:


s = int(input("Enter number"))
if s%2 == 0:
    print('even')

else:
    print('odd')


# In[45]:


s = int(input("Enter number"))
if s%2 == 0:
    print('number is even')

else:
    print('number is not even')


# In[46]:


num=int(input("Enter a number: "))
if (num % 2)  == 0:
    print("{0} is even ".format(num))
else:
    print("{0} is odd".format(num))


# In[ ]:





# ## 2) Write a program to accept a character from the user and check whether it is a capital letter or small letter. Assume user will input only alphabets.

# In[48]:


ch=input("please enter the character")
if "A"<=ch[0]<="Z":
    print("this character will be a capital one")
else:
    print("this character will be a small one")


# In[ ]:





# In[52]:


a=input("Enter the character")
if a.isupper()==True :
    print("{} is a capital letter".format(a))
else:
    print("{} is a lower letter".format(a))
        


# In[ ]:





# ## * Nested If

# ## -- If inside if (We can write as many as if )

# In[53]:


a=100
b=200


# In[54]:


if a<110:
    print("We are in first if statement")
    if b<201:
        print("We are in second if statement")


# In[ ]:





# ## 3) Write a program 3 integers from the user and without using any logical operator and cascading of relational operators, find out the greatest number amongst them.

# X=100
# Y=500
# Z=200

# In[ ]:


x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
if x>y:
    if x>z:
        print("First will be greatest")
elif y>x:
    if y>z:
        print("Second will be greatest")
else:
    print("third is a greatest")


# In[ ]:





# ## While loop

# In[ ]:


x=10
i=1
while i<x:
    print("Shubham")
    print(i)
    i=i+1 ## Increament condition
    print("Loop End")


# In[ ]:





# ## 4) Print 50 Natural numbers with loop
# 
# ## 1 to 50

# In[ ]:





# ## 5) Write a program to accept # a string from the user and display it vertically but don't display the vowels in it.
# 
# ## Do it with while loop.

# In[ ]:


name=input("Enter your name")
i=0
while i<len(name):
    if n[a] != 'a' and n[a]!='e'and n[a]!='i' and n[a]!='o' and n[a]!='u':
        print(n[a])
        #if name[i] not in ["a","e","i","o","u"]:
        print(name[i])
        i=i+1
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




