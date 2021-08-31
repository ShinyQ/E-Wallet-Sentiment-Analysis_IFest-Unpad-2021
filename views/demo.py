import streamlit as st
from models import classifier, cleaning


def app():
    st.write("# **Demo Analisis Sentimen**")
    text = st.text_area(label="Masukkan Kalimat Untuk Analisis Sentimen")

    if text:
        st.write("### **Kalimat Awal**")
        st.write(text)

        col1, col2 = st.columns([3, 2])
        col3, col4 = st.columns(2)

        with col1:
            preprocessing = cleaning.CleanText(text)
            st.write("### **Hasil Preprocessing Kalimat**")
            st.write(
                """<div style="text-align:justify; margin-right:5%">"""
                + preprocessing +
                """</div>""",
                unsafe_allow_html=True)

        with col2:
            classify = classifier.TextClassifying(preprocessing)
            st.write("### **Jenis Klasifikasi Topik**")

            if len(classify) != 0:
                for key, cl in enumerate(classify):
                    st.write("""<div style="margin-bottom:2%">""" + str(key + 1) + ". " + cl.title() + """</div>""", unsafe_allow_html=True)
            else:
                st.write("Tidak Terdapat Topik Yang Cocok")
