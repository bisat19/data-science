import streamlit as st
import numpy as np
import joblib
import os

# Tentukan jalur folder artifacts
# ARTIFACTS_PATH = os.path.join(os.getcwd(), "artifacts")

# # Load model dari folder artifacts
# scaler_path = os.path.join(ARTIFACTS_PATH, 'scaler.pkl')
# pca_path = os.path.join(ARTIFACTS_PATH, 'pca.pkl')
# kmeans_path = os.path.join(ARTIFACTS_PATH, 'kmeans.pkl')

scaler = joblib.load(open('applications/artifacts/scaler.pkl','rb'))
pca = joblib.load(open('applications/artifacts/pca.pkl','rb'))
kmeans = joblib.load(open('applications/artifacts/kmeans.pkl','rb'))

# Header aplikasi
st.title("Prediksi Cluster Produk")

# Input pengguna
st.subheader("Masukkan data nutrisi produk:")
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
    pca_data = pca.transform(scaled_data)
    
    # Prediksi cluster
    cluster = kmeans.predict(pca_data)[0]
    section = ["Produk Organic","Produk Dairy","Produk Olahan"]
    cluster_index = cluster
    # Tampilkan hasil prediksi
    st.success(f"Produk termasuk dalam Section {section[cluster_index]}")