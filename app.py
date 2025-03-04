import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Agregar un encabezado
st.header('Análisis de anuncios de venta de vehículos')

# Casilla de verificación para el histograma
show_histogram = st.checkbox('Mostrar histograma de odómetro')

# Si la casilla de verificación está marcada, mostrar el histograma
if show_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión (Precio vs Kilometraje)')

# Si la casilla de verificación está marcada, mostrar el gráfico de dispersión
if show_scatter:
    st.write('Creación de un gráfico de dispersión   (precio vs. kilometraje)')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig_scatter, use_container_width=True)