from get_data import all_model_data
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import contractions
import string

def recommender(category : str, curr_reviews : dict):
    
    df, users, df_cols, mapping = all_model_data(category)
    
    processed_dict = {}
    punc = list(string.punctuation)
    for key in curr_reviews:
        review = curr_reviews[key][1]
        review = review.lower()
        review = contractions.fix(review)
        for mark in punc:
            review = review.replace(mark, '')
        polarity = TextBlob(review).sentiment.polarity
        value = curr_reviews[key][0] * polarity
        processed_dict[key] = value

    arr = np.zeros([1, len(df_cols)], dtype = 'float64')
    ls = list(processed_dict.keys()) 
    ind = 0
    for col in df_cols:
        if col in ls:
            arr[0][ind] = processed_dict[col]
        ind += 1

    similarity_arr = cosine_similarity(arr, df.iloc[ : , 1 : ])

    sim_users = []
    for i, user in enumerate(users):
        curr_sim = [user]
        curr_sim.append(similarity_arr[0, i])
        sim_users.append(curr_sim)
        
    for i in range(0, len(sim_users) - 1):
        for j in range(0, len(sim_users) - i - 1):
            if(sim_users[j][1] < sim_users[j+1][1]):
                temp = sim_users[j]
                sim_users[j] = sim_users[j+1]
                sim_users[j+1] = temp
                
    products_reviewed = { }
    for user in sim_users[0:5]:
        if(user[1] > 0):
            curr_user = df[df.isin([user[0]]).any(axis=1)].values[0][1:].reshape(1,-1)
            pos_rev_ind = np.where(curr_user >= 2.5)[1]
            products_reviewed = set(products_reviewed).union(set(pos_rev_ind))
            
    output_prods = []
    for i in products_reviewed:
        if i not in ls: 
            output_id = df_cols[i] 
            output_prods.append(mapping[output_id])
        
    return output_prods

