
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# In[50]:

df = pd.read_csv('NewFreshFELTdata1.csv')


# In[51]:

df.info()


# In[52]:

df['process_order_creation_date'] = pd.to_datetime(df['process_order_creation_date'],errors='coerce',dayfirst=True)
df['process_order_release_date'] = pd.to_datetime(df['process_order_release_date'],errors='coerce',dayfirst=True)
df['packaging_line_start_date'] = pd.to_datetime(df['packaging_line_start_date'],errors='coerce',dayfirst=True)
df['packaging_line_finish_date'] = pd.to_datetime(df['packaging_line_finish_date'],errors='coerce',dayfirst=True)
df['packaging_final_check_date'] = pd.to_datetime(df['packaging_final_check_date'],errors='coerce',dayfirst=True)
df['brr_start_date'] = pd.to_datetime(df['brr_start_date'],errors='coerce',dayfirst=True)
df['brr_end_date'] = pd.to_datetime(df['brr_end_date'],errors='coerce',dayfirst=True)
df['qa_release_date'] = pd.to_datetime(df['qa_release_date'],errors='coerce',dayfirst=True)


# In[53]:

df1 = df.dropna()
df1.info()


# In[54]:

df1.info()


# In[55]:

df2 = pd.DataFrame()


# In[56]:

df2['process_order_number'] = (df1['process_order_number']).astype(int)


# In[57]:

df2['order_type_packaging_or_repackaging_field'] = (df1['order_type'])


# In[58]:

df2['material_number'] = (df1['material_number'])
df2['product'] = (df1['product_family'])
df2['product_name'] = (df1['product_name'])


# In[59]:

df2['process_order_creation_date'] = (df1['process_order_creation_date'])


# In[60]:

df2['batch_number'] = (df1['batch_number'])


# In[61]:

df2['batch_number'] = (df1['batch_number'])
df2['process_order_release_date'] = (df1['process_order_release_date'])
df2['packaging_line_start'] = (df1['packaging_line_start_date'])
df2['packaging_line_finish'] = (df1['packaging_line_finish_date'])
df2['packaging_final_check_date'] = (df1['packaging_final_check_date'])
df2['brr_start_date'] = (df1['brr_start_date'])
df2['brr_end_date'] = (df1['brr_end_date'])
df2['qa_release_date'] = (df1['qa_release_date'])


# In[62]:

df2.info()


# In[63]:

df3 = pd.DataFrame()
df3 = df2.dropna()
df3.info()
df4 = pd.DataFrame()


# In[64]:

df4['po_create_to_po_release']= ((df3['process_order_release_date']) - (df3['process_order_creation_date']))/ np.timedelta64(1, 'D')
df4['po_release_to_pkg_start']= ((df3['packaging_line_start']) - (df3['process_order_release_date']))/ np.timedelta64(1, 'D')
df4['pkg_start_to_pkg_finish']= ((df3['packaging_line_finish']) - (df3['packaging_line_start']))/ np.timedelta64(1, 'D')
df4['pkg_finish_to_pkg_final_check']= ((df3['packaging_final_check_date']) - (df3['packaging_line_finish']))/ np.timedelta64(1, 'D')
df4['pkg_final_check_to_brr_begin']= ((df3['brr_start_date']) - (df3['packaging_final_check_date']))/ np.timedelta64(1, 'D')
df4['brr_begin_to_brr_finish']= ((df3['brr_end_date']) - (df3['brr_start_date']))/ np.timedelta64(1, 'D')
df4['brr_finish_to_qp_release']= ((df3['qa_release_date']) - (df3['brr_end_date']))/ np.timedelta64(1, 'D')


# In[65]:

df5 = df3.join(df4)


# In[66]:

df5


# In[67]:

df5.to_csv("RocheDataNew.csv", sep=',', encoding='utf-8')


# In[68]:

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'mysql'+"@localhost/cleaned_db_Roche")
df5.to_sql(con=engine, if_exists='replace', name="roche_app_rochenewmodel2",index=False)


# In[69]:

df6 = pd.DataFrame()


# In[70]:

df6 = df5


# In[71]:

df6['PL'] = (df6['packaging_line_start'] - df6['process_order_creation_date'])/ np.timedelta64(1, 'D')
df6['PA'] = (df6['packaging_final_check_date'] - df6['packaging_line_start'])/ np.timedelta64(1, 'D')
df6['QA'] = (df6['qa_release_date'] - df6['packaging_final_check_date'])/ np.timedelta64(1, 'D')


# In[72]:

df6


# In[45]:

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'mysql'+"@localhost/cleaned_db_Roche")
df6.to_sql(con=engine, if_exists='replace', name="roche_app_rochenewmodel2",index=False)


# In[73]:

df6['product'].unique()


# In[74]:

j = 1
for i in df6['product'].unique():
    df6['product'].replace(i, 'Product_' + str(j),inplace=True)
    j = j + 1


# In[94]:

df7 = pd.DataFrame()
df7 = df6


# In[105]:

for i in df6['product_name'].unique():
    j = df7.loc[df['product_name'] == i, 'product']
    back = i.split(' ')[1:]
    backjoin = ' '.join([x for x in back])
    main = j + '_' + backjoin
    df7['product_name'].replace(i,main, inplace=True)


# In[106]:

df7


# In[102]:

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'mysql'+"@localhost/cleaned_db_Roche")
df7.to_sql(con=engine, if_exists='replace', name="roche_app_rochenewmodel",index=False)


# In[57]:

df8 = pd.read_csv('Modified Yield Data - Data.csv')


# In[58]:

df9 = df8.dropna()
df9.info()
df9


# In[59]:

df9['Actual finish'] = pd.to_datetime(df9['Actual finish'],errors='coerce',dayfirst=False)


# In[60]:

df9.info()


# In[66]:

df9.columns = [c.replace(' ', '_') for c in df9.columns]
df9.columns = [c.replace('-', '_') for c in df9.columns]
df9.replace('#DIV/0!', 0,inplace=True)
df10 =df9[df9.columns[1:29]].join(df9[df9.columns[29:33]].replace('[\$,]', '', regex=True).astype(float))


# In[62]:

df10


# In[68]:

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+'mysql'+"@localhost/cleaned_db_Roche")
df10.to_sql(con=engine, if_exists='replace', name="YieldDB",index=False)


# In[ ]:



