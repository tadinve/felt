
# coding: utf-8

# In[11]:

import pandas as pd
import numpy as np


# In[12]:

df = pd.read_csv('BrrPriorityReport2.csv')


# In[13]:

df


# In[14]:

df1 = df.dropna()


# In[15]:

df1.to_csv("BrrPriorityReportCleaned.csv", sep=',', encoding='utf-8')


# In[ ]:




# In[ ]:



