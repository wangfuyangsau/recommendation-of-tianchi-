#%%
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as plt
#%%
data_train=pd.read_csv(r'C:\Users\Administrator\Downloads\Antai_AE_round1_train_20190626\Antai_AE_round1_train_20190626.csv')
data_train.head(10)
#c=data_train.copy()
data_train.drop(columns=['create_order_time','buyer_country_id'],inplace=True)
#data_train=data_train.groupby(['item_id'])['buyer_admin_id'].count()


#%%
top30item=list(data_train.sort_values(by='buyer_admin_id',ascending=False).index)[0:30]

#%%
#对购买数少于1000的商品删除
down1000=list(data_train[data_train['buyer_admin_id']<500].index)


#%%
data_train=data_train[~data_train['item_id'].isin(down1000)]

#%%
ie=[2850195	,2370323,	394127,	12824199,	634028,	7163049,	11140901,	9722278	,12891086,	11912785,	6057436	,12928279,4016066	,7937154]
for i in ie:
    if i not in data_train['item_id']:
        print('1')

#%%
