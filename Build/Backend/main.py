from fastapi import FastAPI
from pydantic import BaseModel
from get_data import coldstart
from model import recommender

app = FastAPI()

class Data(BaseModel):
    coldstart : bool = True
    category : str
    curr_reviews : dict
    
@app.post('/recommend')
async def recommend(user_input : Data):
    
    if user_input.coldstart == True:
        products = coldstart(user_input.category)
        return products
    
    # model integration
    products = recommender(user_input.category, user_input.curr_reviews)
    
    return products

