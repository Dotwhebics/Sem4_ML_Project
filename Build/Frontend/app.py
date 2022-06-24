import streamlit as st
import json

from ui_functions import display_coldstart
from ui_functions import existing_user

st.title('Amazon Product Recommender')

coldstart = st.selectbox('Coldstart?', ['True', 'False'])

category_list = ['Arts', 'Watches', 'Musical_Instruments', 'Cell_Phones_&_Accessories', 'Jewelry']

if coldstart == 'True':
    st.write('Looks like you are new here!!')
    category = st.selectbox('Select you category', category_list)
    if st.button('Recommend'):
        products = display_coldstart(category)
        products = products.split('"')[1:-1]
        for product in products:
            if product == ',':
                continue
            st.write(product)

else:
    st.write('Recommending based on your previous reviews!!')
    category = st.selectbox('Select you category', category_list)
    curr_reviews = st.text_area('Previous Reviews', height = 275)
    if st.button('Recommend'):
        curr_reviews = json.loads(curr_reviews)
        products = existing_user(category, curr_reviews)
        products = products.split('"')[1:-1]
        for product in products:
            if product == ',':
                continue
            st.write(product)

