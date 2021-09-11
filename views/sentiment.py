import streamlit as st
import pandas as pd
from models import sentiment
import plotly.express as px


def app():
    st.markdown("## **Hasil Proses Analisis Sentiment**")
    df_dana, df_ovo, df_link, df_saku = sentiment.processed_data()

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)

    # st.table(get_sentiment(df_ovo, 1))
    with col2:
        sentiment.percentage(df_dana, 'Dana', px.colors.sequential.Agsunset)
    with col1:
        st.write("### **Hasil Analisis Sentimen Aplikasi Dana**")
        sentiment.topic_percentage('Dana', px.colors.sequential.Agsunset)

    with col4:
        sentiment.percentage(df_ovo, 'OVO', px.colors.sequential.Agsunset)
    with col3:
        st.write("### **Hasil Analisis Sentimen Aplikasi OVO**")
        sentiment.topic_percentage('OVO', px.colors.sequential.Agsunset)

    with col6:
        sentiment.percentage(df_link, 'LinkAja', px.colors.sequential.Agsunset)
    with col5:
        st.write("### **Hasil Analisis Sentimen Aplikasi LinkAja**")
        sentiment.topic_percentage('Link', px.colors.sequential.Agsunset)

    with col8:
        sentiment.percentage(df_saku, 'Sakuku', px.colors.sequential.Agsunset)
    with col7:
        st.write("### **Hasil Analisis Sentimen Aplikasi Sakuku**")
        sentiment.topic_percentage('Sakuku', px.colors.sequential.Agsunset)
