import tensorflow as tf
import streamlit as st
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from PIL import Image
from IPython.display import HTML, display
import base64
import requests
import folium
from haversine import haversine

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

# saving ram by removing dfs
df1 = None
df2 = None
df3 = None
df4 = None
df5 = None
df6 = None
df7 = None
df8 = None
df9 = None

address = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/tourapi_add.csv', encoding='utf-8-sig', index_col=0)

np_df = df.drop(columns='명칭')
np_df = np_df.values

model = VGG16(weights='imagenet', include_top=False)

# webpage head
st.write('Hello, *Welcome to Tour-Helper!* :sunglasses:')


#date selection
d = st.date_input('Choose Your Trip Date', value=None , min_value=None , max_value=None , key=None )
if d:
    st.write('You chose  :', d)
    month = d.month
    day = d.day


# image upload
uploaded_file = st.file_uploader("Upload Your Trip-To-Be Image")

if uploaded_file is not None:
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
    
    trip = pd.merge(simil_df, address, on = '명칭', how = 'inner')
    df.clear()

    # 관광객 수 데이터 조정 및 위경도 관련 데이터 불러오기
    people = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/tourist_prediction_2324.csv', encoding='utf-8-sig', index_col=0)
    result_people = people.reset_index(drop=True)
    result_people['월'] = result_people['ds'].apply(lambda x : x.split('-')[1])
    result_people['일'] = result_people['ds'].apply(lambda x : x.split('-')[2])
    result_people['월'] = result_people['월'].astype('int')
    result_people['일'] = result_people['일'].astype('int')
    people = None
    
    result_list = list(trip['명칭'])
    result_temp = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/temp_test.csv')
    lat_lon_peo = pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/lat_lon_peo.csv')
    lat_lon_tem= pd.read_csv('https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/lat_lon_tem.csv')



# github 파일 이용한 folium 띄우기


def local_find(frame, frame2):
    for i in range(len(frame)):
        start = frame.loc[i, '위도'], frame.loc[i, '경도'] 
        goal = frame2.loc[0, '위도'], frame2.loc[0, '경도'] 
        frame.loc[i,'거리'] = haversine(start, goal, unit='mi')

    frame.sort_values(by='거리', inplace=True)
    frame.reset_index(drop=True,inplace=True)
    return frame.loc[0, '지역']

def result_output(result_list, user_month, user_day):
    m =folium.Map(location=[36, 127], zoom_start=7.5, tiles='openStreetMap')
    tooltip = 'Info'
    # result = []
    for i in result_list:
        data = trip[trip['명칭'] == i].reset_index(drop=True)
        # if data['주소'][0].split(' ')[0] == '경기도':
        #     address = data['주소'][0].split(' ')[1][:-1]
        # else:
        #     address = data['주소'][0].split(' ')[0][:2]

        address = local_find(lat_lon_tem , data)
        address1 = local_find(lat_lon_peo , data)

        pre_people = result_people[(result_people['si'] == address1) & (result_people['월'] == user_month) & (result_people['일'] == user_day)].reset_index(drop=True)
        # result.append([address, address1])
        temp = result_temp[(result_temp['si'] == address) & (result_temp['월'] == user_month) & (result_temp['일'] == user_day)].reset_index(drop=True)
        
        # Assuming 'data["사진"].values[0]' contains the image file's raw content URL from GitHub
        image_url = f'https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/images/{data["사진"].values[0]}'
        response = requests.get(image_url)

        # Fetch the image content
        if response.status_code == 200:
          image_content = requests.get(image_url).content
        else:
          image_url = f'https://raw.githubusercontent.com/KulangK/Zerobase_Tutorials/main/Final_Project/images2/{data["사진"].values[0]}'
          image_content = requests.get(image_url).content

        # Encode the image in base64 format
        encoded_image = base64.b64encode(image_content).decode()

        # Create the popup content
        popup_content = f'<div style="width:250px; text-align:center;">'\
                        f'<strong>{data["명칭"].values[0]}</strong><br><br>'\
                        f'<img width="250px" src="data:image/jpeg;base64,{encoded_image}"><br><br>'\
                        f'주소: {data["주소"].values[0]}<br>'\
                        f'예상 방문객: {round(pre_people["yhat"].values[0])} 명<br>'\
                        f'예상 온도: {round(temp["yhat"].values[0])} (°C)<br></div>'

        # Create the folium.Marker
        folium.Marker(
            [data['위도'], data['경도']],
            popup=popup_content,
            tooltip=tooltip,
            icon=folium.Icon(icon='info-sign')
        ).add_to(m)

    m.save('result.html')
    return m

if uploaded_file is not None:
    st.write(result_output(result_list, month, day))
