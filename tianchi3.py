#%%
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib as plt
#%%
user_item={}
for i in test_user:
    user_item.update({i:data_test[data_test['buyer_admin_id']==i].item_id.values})

#%%
user_corrma={}
for key,item in user_item.items():
    a=list(item)
    b=list(item)
    for i in a:
        if i in data_train.columns:
            continue
        else:
            b.remove(i)
    if len(b):
        res=[]
        for j in b:
             corr_user=data_train.corrwith(data_train[j])#返回Series
             res.append(corr_user.dropna())
        user_corrma.update({key:res})
    else:
        user_corrma.update({key:[]})
#%%
user1_re={}
res1_none=[]
for key,item in user_corrma.items():
     if len(item)==0:
         res1_none.append(key)#获取无法推荐的用户
         continue
    
     elif len(item)==1:
          a=item[0].sort_values(ascending=False)
          if len(a)>=30:
              user1_re.update({key:list(a.index)[:30]})
          else:
              user1_re.update({key:list(a.index)})
     else:
           b=(pd.concat(item).sort_values(ascending=False).index).drop_duplicates()
           if len(b)>=30:
                user1_re.update({key:list(b)[:30]})
           else:
                user1_re.update({key:list(b)})
#%%
item_30=top30item

#%%
norecom_user_item={}
for i in res1_none:
      re_item=list(data_test[data_test['buyer_admin_id']==i]['item_id'].drop_duplicates().values)
      np.random.shuffle(item_30)
      if len(re_item)<30:
          re_item+=item_30[:30-len(re_item)]
      else:
          re_item=re_item[:30]
      norecom_user_item.update({i:re_item})

#%%

user_re={}
for i,item in user1_re.items():
   
    if len(item)<30:
        np.random.shuffle(item_30)
        item+=item_30[:30-len(item)]
    user_re.update({i:item})

#%%
#结果验证
for i,ii,in user_re.items():
    if len(ii)!=30:
        print(i)
for i,ii in norecom_user_item.items():
    if len(ii)!=30:
        print(i)

#%%
#合并结果
result=pd.DataFrame(user1_re)
result=result.T
result1=pd.DataFrame(norecom_user_item)
result1=result1.T
end_result=pd.concat([result,result1])
#%%
#输出结果
end_result.to_csv(r'C:\Users\Administrator\Desktop\submit_result1.csv')

#%%
#结果验证
for i in test_user:
    if i not  in list(end_result.index):
        print(i)


#%%
