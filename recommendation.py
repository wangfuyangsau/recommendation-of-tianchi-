#%%
import pandas as  pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
#%%
df = pd.read_csv(r'C:\Users\Administrator\Downloads\ml-latest-small\ratings.csv'\
        , sep=',')

#%%
movie_name=pd.read_csv(r'C:\Users\Administrator\Downloads\ml-latest-small\movies.csv'\
    ,sep=',')

#%%
movie_name.head()

#%%
df=pd.merge(df,movie_name,on='movieId')
df.head()

#%%
df.drop(columns='genres')

#%%
df.info()


#%%
df.describe()

#%%
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()

#%%
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
ratings.head()

#%%
men_movie=df.groupby(['userId','title']).mean()
men_movie
#%%
ratings['rating'].hist(bins=50)

#%%
ratings['number_of_ratings'].hist(bins=1000)

#%%

sns.jointplot(x='rating', y='number_of_ratings', data=ratings)

#%%
movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
movie_matrix.head()

#%%
ratings.sort_values('number_of_ratings', ascending=False).head(10)

#%%
AFO_user_rating = movie_matrix['Air Force One (1997)']
contact_user_rating = movie_matrix['Contact (1997)']


#%%
AFO_user_rating.head()
contact_user_rating.head()


#%%
similar_to_air_force_one=movie_matrix.corrwith(AFO_user_rating)

#%%
print(similar_to_air_force_one)

#%%
similar_to_contact = movie_matrix.corrwith(contact_user_rating)

#%%
similar_to_contact.head()

#%%
corr_contact = pd.DataFrame(similar_to_contact, columns=['Correlation'])
corr_contact.dropna(inplace=True)
corr_contact.head()
corr_AFO = pd.DataFrame(similar_to_air_force_one, columns=['correlation'])
corr_AFO.dropna(inplace=True)
corr_AFO.head()

#%%
corr_AFO = corr_AFO.join(ratings['number_of_ratings'])
corr_contact = corr_contact.join(ratings['number_of_ratings'])
corr_AFO .head()
corr_contact.head()

#%%
corr_AFO[corr_AFO['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10)

#%%
corr_contact[corr_contact['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(10)

#%%


#%%


#%%
