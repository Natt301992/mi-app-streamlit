# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:11:10 2025

@author: pc
"""



import os
print("Directorio actual:", os.getcwd())



import streamlit as st
import joblib
import numpy as np 

model_filename = 'arnes.pkl'
# Cargamos el modelo desde el archivo
loaded_model = joblib.load(model_filename)

print("Hemos cargado el modelo")

# Preparar los datos de entrada para el modelo
#inputs = np.array(60).reshape(-1, 1)

# Usamos el modelo para hacer predicciones
#predicted_boot_size = loaded_model.predict(inputs)[0]

#st.write("El modelo estima un tamaño de bota",round(predicted_boot_size))

arnes = 0

arnes = st.text_input(label='Tamaño del arnés:',value=0)

arnes = int(arnes)

inputs = np.array(arnes).reshape(-1, 1)

#Usamos el modelo para hacer predicciones
predicted_boot_size = loaded_model.predict(inputs)[0]


st.write("El modelo estima un tamaño de bota: ",round(predicted_boot_size))

texto = "El modelo estima un tamaño de bota: " + str(round(predicted_boot_size))

st.info(texto)