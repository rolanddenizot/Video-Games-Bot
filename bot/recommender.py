import pandas as pd
import io
import numpy as np
from scipy import spatial

def cosine_similarity(usr,mov):
  return 1 - spatial.distance.cosine(usr,mov)



def getRecommendation(message):
  jv = pd.read_csv('./videogames.csv', sep=',')
  jv = jv[['Rank', 'Name', 'Genre']]
  jv.rename(columns={'Rank': 'jvId'}, inplace=True)
  all_genres = set(jv.Genre)
  all_genres = list(all_genres)
  print(all_genres)
  
  encodings = []
  
  for index, row in jv.iterrows():
      genres = row['Genre']
      encod = [
          1 if all_genres[i] == genres else 0 for i in range(len(all_genres))
      ]
      encodings.append(encod)
    
  for j in range(len(encodings[0])):
    first_col = [encodings[i][j] for i in range(len(encodings))]
    jv[all_genres[j]] = first_col
    
  jv_genres = jv[all_genres]
  jv_new = jv_genres.div(jv_genres.sum(axis=1), axis=0)
  jv_new['jvId']=jv['jvId']
  
  ratings = pd.read_csv('./ratings.csv', sep=',')
  user_ids = set(ratings.userId)
  ids_toenum = {v:k for k,v in enumerate(user_ids)}
  print(ids_toenum)
  
  def utility_matrix():
    max_user = len(set(ratings.userId))
    max_jv = ratings.jvId.max()
    utility_matrix = np.zeros(shape=(max_user+1,max_jv+1))
  
    for index,row in ratings.iterrows():
      u_id = int(ids_toenum[row['userId']])
      m_id = int(row['jvId'])
      ranking = int(row['rating'])
      utility_matrix[u_id,m_id] = ranking
  
    return utility_matrix
  
  utility_matrix = utility_matrix()
  
  ratings['jvId']= ratings['jvId'].astype(int)
  
  result = pd.merge(ratings,jv_new[jv_new.columns],on='jvId')
  
  user_matrix=[]
  for id in np.unique(result.userId):
    usr1 = result.loc[result['userId']==id].reset_index()
    scores_genres = []
    ratings_usr = usr1.rating
    array_genres = [usr1[genre] for genre in all_genres]
    for j in range(len(all_genres)):
      scores_genre = [array_genres[j][i]*ratings_usr[i] for i in range(len(ratings_usr))]
      scores_genres.append(np.sum(scores_genre))
    user_matrix.append(scores_genres)
  
  user_df = pd.DataFrame(user_matrix,columns=all_genres)
  similarities = {i:cosine_similarity(user_df.iloc[0],jv_new.iloc[i,:len(user_df.iloc[0])])for i in range(jv_new.shape[0])}
  similarities = {k: v for k, v in sorted(similarities.items(),reverse=True, key=lambda item: item[1])}
  already_played = len(ratings.loc[ratings["userId"] == f'{message.author}'].index)
  similarities_jv_idx = [list(similarities.keys())[i] for i in range(already_played,already_played+3)]
  game_names = [jv.iloc[idx]['Name'] for idx in similarities_jv_idx]
  
  return ','.join(game_names)