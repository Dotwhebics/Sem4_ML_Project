from api_caller import call

def display_coldstart(category):
    data = {
        "coldstart" : True,
        "category" : category,
        "curr_reviews" : {} 
    }
    products = call(data)
    return products

def existing_user(category, curr_reviews):
    data = {
        "coldstart" : False,
        "category" : category,
        "curr_reviews" : curr_reviews
    }
    products = call(data)
    return products
