import pickle
import pandas as pd

def coldstart(category : str):
    data = open('pickled_files/coldstart_dict.pkl', 'rb')
    dictionary = pickle.load(data)
    data.close()
    return dictionary[category]



def all_model_data(category : str):
    
    path = 'crosstab_datasets/' + category + '.csv'
    df = pd.read_csv(path)
    
    users = df['review/profileName'].to_numpy()
    
    df_cols = list(df.columns)[1 : ]
    
    data = open('pickled_files/mappings_dict.pkl', 'rb')
    dictionary = pickle.load(data)
    data.close()
    mapping = dictionary[category]
    
    return df, users, df_cols, mapping
