import tensorflow as tf
import streamlit as st
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from PIL import Image

def extract_features(img_path, model):
    img = Image.open(img_path)
    new_image = img.resize((224, 224))
    img_array = image.img_to_array(new_image)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / np.linalg.norm(flattened_features)
    return normalized_features

df1 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values1.csv', encoding='utf-8-sig', index_col=0)
df2 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values2.csv', encoding='utf-8-sig', index_col=0)
df3 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values3.csv', encoding='utf-8-sig', index_col=0)
df4 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values4.csv', encoding='utf-8-sig', index_col=0)
df5 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values5.csv', encoding='utf-8-sig', index_col=0)
df6 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values6.csv', encoding='utf-8-sig', index_col=0)
df7 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values7.csv', encoding='utf-8-sig', index_col=0)
df8 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values8.csv', encoding='utf-8-sig', index_col=0)
df9 = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/feature_values9.csv', encoding='utf-8-sig', index_col=0)

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9])
df.rename(columns={'name':'명칭'}, inplace=True)

address = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/tourapi_data.csv', encoding='utf-8-sig')

np_df = df.drop(columns='명칭')
np_df = np_df.values

model = VGG16(weights='imagenet', include_top=False)


st.write('Hello, *Welcome to Tour-Helper!* :sunglasses:')


d = st.date_input('Choose Your Trip Date', value=None , min_value=None , max_value=None , key=None )
st.write('You chose  :', d)



uploaded_file = st.file_uploader("Upload Your Trip-To-Be Image")

st.image(uploaded_file, caption = 'Uploaded Image')



user_features = extract_features(uploaded_file, model)

similarity = []
for i in range(0, len(df)):
  x = cosine_similarity([np_df[i]], [user_features])
  similarity.append(x)

similarity_list = []
for i in range(0, len(similarity)):
  similarity_list.append(similarity[i][0][0])

df['similar_score'] = similarity_list

simil_df = df.sort_values(by='similar_score', ascending=False)
simil_df = simil_df[['명칭', 'similar_score']].iloc[:20]

st.dataframe(simil_df)

result = pd.merge(simil_df, address, on = '명칭', how = 'inner')
st.dataframe(result)
