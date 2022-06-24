import requests

def call(data):
    local = 'http://127.0.0.1:8000/recommend'
    products = requests.post(local, json = data)
    return products.text
