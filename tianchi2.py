#%%
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as plt
 
#%%
data_train1=data_train[0:400000]
data_train1=data_train1.groupby(by=['buyer_admin_id','item_id'])['irank'].count()
data_train1=pd.DataFrame(data_train1)
data_train1=data_train1.pivot_table(index='buyer_admin_id',columns='item_id',values='irank')
#%%
data_train2=data_train[400000:800000]
data_train2=data_train2.groupby(by=['buyer_admin_id','item_id'])['irank'].count()
data_train2=pd.DataFrame(data_train2)
data_train2=data_train2.pivot_table(index='buyer_admin_id',columns='item_id',values='irank')
#%%
data_train3=data_train[800000:]
data_train3=data_train3.groupby(by=['buyer_admin_id','item_id'])['irank'].count()
data_train3=pd.DataFrame(data_train3)
data_train3=data_train3.pivot_table(index='buyer_admin_id',columns='item_id',values='irank')
#%%
data_train=pd.concat([data_train1,data_train2,data_train3])
del data_train1
del data_train2
del data_train3
#%%
data_test=pd.read_csv(r'C:\Users\Administrator\Downloads\Antai_AE_round1_test_20190626.csv')
data_test.head(10)
data_test.drop(columns=['create_order_time','buyer_country_id'],inplace=True)
#%%
test_user=list(data_test['buyer_admin_id'].drop_duplicates())

#%%






#%%
