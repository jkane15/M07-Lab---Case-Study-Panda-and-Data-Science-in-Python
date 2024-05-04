#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install pandas


# In[9]:


import pandas as pd


# In[15]:


pd.


# 1.1 Create from a csv

# In[14]:


df = pd.read_csv('telco_churn.csv')


# 1.2 Create from a dictionary 

# In[23]:


temptdict = {'coll':[1,2,3], 'col2':[4,5,6],'col3':[7,8,9]}


# In[24]:


dictdf = pd.DataFrame.from_dict(temptdict)


# 2.1 Show top 5 and bottom rows 

# In[17]:


df.head(5)


# In[25]:


dictdf.head()


# In[27]:


df.tail(10)


# 2.2 Show Columns and Data types

# In[28]:


df.columns


# In[29]:


df.dtypes


# Summary Statistics 

# In[30]:


df.describe()


# In[31]:


df.describe(include='object')


# 2.4 Filtering Columns

# In[32]:


df.State


# In[33]:


df['International plan']


# In[34]:


df[['State','International plan']]


# In[36]:


df.Churn.unique()


# 2.5 Filtering on Rows 

# In[37]:


df.head()


# In[38]:


df[df['International plan']=='No']


# In[39]:


df[(df['International plan']=='No') & (df['Churn']==False)]


# In[40]:


df[(df['International plan']=='No') & (df['Churn']==True)]


# 2.6 Indexing with iloc

# In[41]:


df.iloc[14]


# In[42]:


df.iloc[14,0]


# In[43]:


df.iloc[22:33]


# 2.7 Indexing with loc

# In[44]:


state = df.copy()
state.set_index('State', inplace=True)


# In[45]:


state.head()


# In[46]:


state.loc['OH']


# 3.1 Dropping Rows

# In[47]:


df.isnull().sum()


# In[48]:


df.dropna(inplace=True)


# In[49]:


df.isnull().sum()


# 3.2 Dropping Columns

# In[50]:


df.drop('Area code', axis=1)


# 3.3 Creating Calculated Columns

# In[53]:


df['New Column'] = df['Total night minutes'] + df['Total intl minutes']


# In[54]:


df.head()


# 3.4 Updating entire column

# In[56]:


df['New Column'] = 100


# In[57]:


df.head()


# 3.5 Updating a Single Value 

# In[58]:


df.iloc[0,-1] = 10


# In[59]:


df.head()


# 3.6 Condition based updating using apply 

# In[61]:


df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)


# In[63]:


df[df['Churn']==True].head()


# 4.1 Output to CSV

# In[64]:


df.to_csv('output.csv')


# In[65]:


df.to_json()


# In[66]:


df.to_html()


# In[ ]:




