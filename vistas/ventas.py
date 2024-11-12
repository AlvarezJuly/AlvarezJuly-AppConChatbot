import streamlit as  st
import pandas as pd
import plotly.express as px

import datetime 

dfDatos = pd.read_csv('https://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')
#pip install plotly installar para la conexión de los datos

st.header("Filtrado y Captura de Datos")
st.write("EL procesamiento de datos a través de ciencia de datos usando Streamlit de Python.")

st.metric("Registros Totales", len (dfDatos))
st.dataframe(dfDatos, use_container_width=True)