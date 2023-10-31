import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('estimasi_harga_rumah.sav', 'rb'))

st.title('Estimasi harga rumah')

area = st.number_input('Luas total rumah dalam kaki persegi')
bedrooms = st.number_input('Jumlah kamar tidur di dalam rumah.')
bathrooms = st.number_input('Jumlah kamar mandi di dalam rumah.')
stories = st.number_input('Jumlah lantai di dalam rumah')
mainroad = st.selectbox('Apakah rumah tersebut terhubung dengan jalan utama', ['Yes','No'])
guestroom = st.selectbox('Apakah rumah tersebut memiliki ruang tamu', ['Yes','No'])
basement = st.selectbox('Apakah rumah memiliki ruang bawah tanah', ['Yes','No'])
hotwaterheating = st.selectbox('Apakah rumah memiliki sistem pemanas air panas', ['Yes','No'])
airconditioning = st.selectbox('Apakah rumah memiliki sistem pendingin udara', ['Yes','No'])
parking = st.number_input('Jumlah tempat parkir yang tersedia di dalam rumah')
prefarea = st.selectbox('Apakah rumah tersebut terletak di area yang disukai', ['Yes','No'])
furnishingstatus = st.selectbox('Status perabotan rumah', ["Fully Furnished", "Semi Furnished", "Unfurnished"])


# Define LabelEncoders for categorical variables
label_encoder_mainroad = LabelEncoder()
label_encoder_guestroom = LabelEncoder()
label_encoder_basement = LabelEncoder()
label_encoder_hotwaterheating = LabelEncoder()
label_encoder_airconditioning = LabelEncoder()
label_encoder_prefarea = LabelEncoder()
label_encoder_furnishingstatus = LabelEncoder()

# Anda perlu melakukan fit pada objek LabelEncoder sebelum melakukan transform
label_encoder_mainroad.fit(['Yes','No'])
label_encoder_guestroom.fit(['Yes', 'No'])
label_encoder_basement.fit(['Yes','No'])
label_encoder_hotwaterheating.fit(['Yes','No'])
label_encoder_airconditioning.fit(['Yes','No'])
label_encoder_prefarea.fit(['Yes','No'])
label_encoder_furnishingstatus.fit(["Fully Furnished", "Semi Furnished", "Unfurnished"])

mainroad_encoded = label_encoder_mainroad.transform([mainroad])[0]
guestroom_encoded = label_encoder_guestroom.transform([guestroom])[0]
basement_encoded = label_encoder_basement.transform([basement])[0]
hotwaterheating_encoded = label_encoder_hotwaterheating.transform([hotwaterheating])[0]
airconditioning_encoded = label_encoder_airconditioning.transform([airconditioning])[0]
prefarea_encoded = label_encoder_prefarea.transform([prefarea])[0]
furnishingstatus_encoded = label_encoder_furnishingstatus.transform([furnishingstatus])[0]

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[area,bedrooms, bathrooms,stories,mainroad_encoded,guestroom_encoded,basement_encoded,
           hotwaterheating_encoded,airconditioning_encoded,parking,prefarea_encoded,furnishingstatus_encoded]]
    )
    st.write('Estimasi Harga Rumah:', predict)
