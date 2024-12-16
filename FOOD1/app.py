import streamlit as st
import numpy as np
import joblib
import os

scaler = joblib.load(open('artifacts/scaler1.pkl','rb'))
kmeans = joblib.load(open('artifacts/kmeans1.pkl','rb'))

# Header aplikasi
st.title("Cari Produk Keto-mu")

# Input pengguna
st.subheader("Masukkan data nutrisi produk yang anda cari:")
energy = st.number_input('Energy (100g)', min_value=0.0, step=0.1)
fat = st.number_input('Fat (100g)', min_value=0.0, step=0.1)
saturated_fat = st.number_input('Saturated Fat (100g)', min_value=0.0, step=0.1)
carbohydrates = st.number_input('Carbohydrates (100g)', min_value=0.0, step=0.1)
sugars = st.number_input('Sugars (100g)', min_value=0.0, step=0.1)
proteins = st.number_input('Proteins (100g)', min_value=0.0, step=0.1)

# Tombol untuk prediksi
if st.button("Prediksi Cluster"):
    # Preprocessing input
    input_data = np.array([[energy, fat, saturated_fat, carbohydrates, sugars, proteins]])
    scaled_data = scaler.transform(input_data)
    
    # Prediksi cluster
    cluster = kmeans.predict(scaled_data)[0]
    section = ["Produk Organic","Produk Dairy","Produk Olahan"]
    cluster_index = cluster
    # Tampilkan hasil prediksi
    st.success(f"Produk anda termasuk dalam Section {section[cluster_index]}")