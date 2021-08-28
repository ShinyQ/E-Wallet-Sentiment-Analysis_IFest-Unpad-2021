import streamlit as st
from views import crawling


def app():
    st.markdown("# Halaman Utama")
    st.image('image/dac.jpg')
    st.write("""
        <div style="text-align:justify;">
            Data Analysis Competition merupakan cabang kompetisi IT Competition IFest 2021 berskala nasional. 
            Kompetisi Analisis Data adalah kompetisi untuk menganalisis data untuk mendapatkan solusi dari suatu masalah. 
            Tujuan dari kompetisi ini adalah untuk mendorong generasi milenial agar memiliki kemampuan analisa yang baik 
            sehingga dapat menyelesaikan berbagai permasalahan yang ada di era digital. Kompetisi Analisis Data mengangkat 
            tema <b>"Memanfaatkan Kekuatan Analisis Sentimen Terhadap Kemajuan Industri dan Bisnis Digital"</b>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## **Abstrak**")
    st.write("""
        <div style="text-align:justify; margin-bottom: 1%">
            Data Analysis Competition merupakan cabang kompetisi IT Competition IFest 2021 berskala nasional. 
            Kompetisi Analisis Data adalah kompetisi untuk menganalisis data untuk mendapatkan solusi dari suatu masalah. 
            Tujuan dari kompetisi ini adalah untuk mendorong generasi milenial agar memiliki kemampuan analisa yang baik 
            sehingga dapat menyelesaikan berbagai permasalahan yang ada di era digital. Kompetisi Analisis Data mengangkat 
            tema <b>"Memanfaatkan Kekuatan Analisis Sentimen Terhadap Kemajuan Industri dan Bisnis Digital"</b>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## **Alur Pemrosesan Analisis Sentimen**")
    st.write("""
        Dalam proses melakukan analisis sentimen terdapat beberapa macam langkah-langkah
        yang harus dilakukan untuk menghasilkan analisis sentimen yang diinginkan. Adapun alur
        pemrosesan tersebut disederhanakan melalui gambaran flowchart sebagai berikut.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.image('image/alur.png', width=450)

    with col2:
        st.write("""
            **1. Data Crawling**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Proses pengambilan data review pada google play store untuk mendapatkan
                ulasan pengguna e-wallet pada aplikasi ovo, dana, sakuku, dan linkaja.
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            **2. Data Preprocessing**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Data preprocessing adalah teknik penambangan data yang digunakan untuk mengubah data raw menjadi 
                data dengan format yang berguna dan efisien. Pada kasus analisis sentimen ini akan dilakukan 4 jenis
                pemrosesan yaitu casefolding, filtering, tokenizing, dan stemming.
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            **3. Topic Classification**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Proses pengambilan data review pada google play store untuk mendapatkan
                ulasan pengguna e-wallet pada aplikasi ovo, dana, sakuku, dan linkaja.
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            **4. Sentiment Analysis Modelling**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Proses pengambilan data review pada google play store untuk mendapatkan
                ulasan pengguna e-wallet pada aplikasi ovo, dana, sakuku, dan linkaja.
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            **5. Sentiment Analysis Result**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Proses pengambilan data review pada google play store untuk mendapatkan
                ulasan pengguna e-wallet pada aplikasi ovo, dana, sakuku, dan linkaja.
            </div>
        """, unsafe_allow_html=True)

