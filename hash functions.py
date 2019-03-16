
# coding: utf-8

# In[3]:


n = int(input())


# In[4]:


m = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151]


# In[11]:


def hesh1(a):
    a1=0
    b = str(abs(a))
    for i in range(len(b)):
        a1=(a1+int(b[i]))*m[i]
    return a1


# In[12]:


hesh1(n)


# In[20]:


m2=m.copy()


# In[21]:


m2.reverse()


# In[22]:


m2


# In[24]:


def hesh2(a):
    a1=0
    b = str(abs(a))
    for i in range(len(b)):
        a1=(a1+int(b[i]))*m2[i]
    return a1


# In[25]:


hesh2(n)

