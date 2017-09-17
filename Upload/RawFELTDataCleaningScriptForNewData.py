
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

df = pd.read_csv('RawData2.csv')


# In[3]:

df.info()


# In[4]:

df['process_order_creation_date'] = pd.to_datetime(df['process_order_creation_date'],errors='coerce',dayfirst=True)
df['process_order_release_date'] = pd.to_datetime(df['process_order_release_date'],errors='coerce',dayfirst=True)
df['packaging_line_start_date'] = pd.to_datetime(df['packaging_line_start_date'],errors='coerce',dayfirst=True)
df['packaging_line_finish_date'] = pd.to_datetime(df['packaging_line_finish_date'],errors='coerce',dayfirst=True)
df['packaging_final_check_date'] = pd.to_datetime(df['packaging_final_check_date'],errors='coerce',dayfirst=True)
df['brr_start_date'] = pd.to_datetime(df['brr_start_date'],errors='coerce',dayfirst=True)
df['brr_end_date'] = pd.to_datetime(df['brr_end_date'],errors='coerce',dayfirst=True)
df['qa_release_date'] = pd.to_datetime(df['qa_release_date'],errors='coerce',dayfirst=True)


# In[5]:

df1 = df.dropna()
df1.info()


# In[6]:

df1.info()


# In[7]:

df2 = pd.DataFrame()


# In[8]:

df2['process_order_number'] = (df1['process_order_number']).astype(int)


# In[9]:

df2['order_type_packaging_or_repackaging_field'] = (df1['order_type'])


# In[10]:

df2['material_number'] = (df1['material_number'])
df2['product'] = (df1['product_family'])
df2['product_name'] = (df1['product_name'])


# In[11]:

df2['process_order_creation_date'] = (df1['process_order_creation_date'])


# In[12]:

df2['batch_number'] = (df1['batch_number'])


# In[13]:

df2['batch_number'] = (df1['batch_number'])
df2['process_order_release_date'] = (df1['process_order_release_date'])
df2['packaging_line_start'] = (df1['packaging_line_start_date'])
df2['packaging_line_finish'] = (df1['packaging_line_finish_date'])
df2['packaging_final_check_date'] = (df1['packaging_final_check_date'])
df2['brr_start_date'] = (df1['brr_start_date'])
df2['brr_end_date'] = (df1['brr_end_date'])
df2['qa_release_date'] = (df1['qa_release_date'])


# In[14]:

df2.info()


# In[15]:

df3 = pd.DataFrame()
df3 = df2.dropna()
df3.info()
df4 = pd.DataFrame()


# In[16]:

df4['po_create_to_po_release']= ((df3['process_order_release_date']) - (df3['process_order_creation_date']))/ np.timedelta64(1, 'D')
df4['po_release_to_pkg_start']= ((df3['packaging_line_start']) - (df3['process_order_release_date']))/ np.timedelta64(1, 'D')
df4['pkg_start_to_pkg_finish']= ((df3['packaging_line_finish']) - (df3['packaging_line_start']))/ np.timedelta64(1, 'D')
df4['pkg_finish_to_pkg_final_check']= ((df3['packaging_final_check_date']) - (df3['packaging_line_finish']))/ np.timedelta64(1, 'D')
df4['pkg_final_check_to_brr_begin']= ((df3['brr_start_date']) - (df3['packaging_final_check_date']))/ np.timedelta64(1, 'D')
df4['brr_begin_to_brr_finish']= ((df3['brr_end_date']) - (df3['brr_start_date']))/ np.timedelta64(1, 'D')
df4['brr_finish_to_qp_release']= ((df3['qa_release_date']) - (df3['brr_end_date']))/ np.timedelta64(1, 'D')


# In[17]:

df5 = df3.join(df4)


# In[18]:

df5.info()


# In[20]:

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'mysql'+"@localhost/cleaned_db_Roche")
df5.to_sql(con=engine, if_exists='replace', name="roche_app_rochenewmodel",index=False)


# In[ ]:



