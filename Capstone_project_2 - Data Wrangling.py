#!/usr/bin/env python
# coding: utf-8

# ## Data Collection

# In[4]:


#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy


# In[46]:


#loading the zomato dataset and assigning to variable 'df'
df = pd.read_csv('zomato.csv',sep=',', encoding='latin-1')


# In[131]:


df.shape


# In[43]:


code = pd.read_excel('Country-Code.xlsx', sheet_name='Sheet1')


# In[44]:


code


# In[47]:


dfm = df.merge(code, on='Country Code', how='inner')


# In[10]:


dfm.head() #Calling the head method on merged datasets dfm to print the first several rows of the data


# In[58]:


dfm.info()


# In[59]:


dfm.columns


# In[60]:


dfm.shape


# In[63]:


ind_res = dfm[dfm['Country'] == 'India'] #Zomato Restaurants in India 
ind_res


# In[64]:


ind_res.columns


# In[65]:


ind_res.shape


# In[66]:


ind_res.info()


# In[67]:


ind_res.isnull().mean()*100 #Checking for null values


# In[68]:


ind_res.describe()


# In[70]:


vizag_res = ind_res[ind_res.City == 'Vizag']
vizag_res.shape


# In[71]:


vizag_res.head()


# In[73]:


plt.scatter(vizag_res['Votes'],vizag_res['Price range'], marker = '.')

