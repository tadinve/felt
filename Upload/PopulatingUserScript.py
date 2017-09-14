
# coding: utf-8

# In[10]:

import pandas as pd
import numpy as np


# In[11]:

df = pd.read_csv('FELTUsers.csv')


# In[12]:

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'mysql'+"@localhost/cleaned_db_Roche")
df.to_sql(con=engine, if_exists='append', name="roche_app_userauthentication",index=False)


# In[ ]:



