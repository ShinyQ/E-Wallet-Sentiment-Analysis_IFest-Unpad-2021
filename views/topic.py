import pandas as pd
import streamlit as st
from streamlit_embedcode import github_gist
import plotly.graph_objects as go
from models import classifier


def app():
    st.markdown("## **Proses Pengklasifikasian Topik**")

    st.markdown("### **1. WordCloud**")
    github_gist("https://gist.github.com/ShinyQ/359a063d0feb3d0be01afca1edafa5fd", height=360, width=900)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.write("### **Wordcloud Dana**")
        st.image('image/classification/dana.png', width=450)

    with col2:
        st.write("### **Wordcloud OVO**")
        st.image('image/classification/ovo.png', width=450)

    with col3:
        st.write("### **Wordcloud LinkAja**")
        st.image('image/classification/linkaja.png', width=450)

    with col4:
        st.write("### **Wordcloud Sakuku**")
        st.image('image/classification/sakuku.png', width=450)

    st.write("### **Wordcloud Gabungan Seluruh Dataset**")

    col5, col6 = st.columns(2)

    with col5:
        word_count = pd.read_csv("dataset/topic/wordcount.csv")

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=list(word_count.columns),
                align='center',
                font_size=13,
                height=30,

            ),
            cells=dict(
                values=[word_count.Kata, word_count['Jumlah Kata']],
                align='center',
                font_size=13,
                height=30
            )
        )])

        fig.update_layout(margin=dict(l=0, r=240, t=0, b=210))
        st.plotly_chart(fig)

    with col6:
        st.image('image/classification/all.png', width=450)

    st.markdown("### **2. Pembagian Klasifikasi Topik**")
    github_gist("https://gist.github.com/ShinyQ/67063ba772f91ad21ea88f4b85d282ac", height=360, width=900)

    st.write(classifier.DataFrameClassifier('dataset/raw/ovo.csv', "comments"))