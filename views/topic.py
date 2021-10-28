import pandas as pd
import streamlit as st
from streamlit_embedcode import github_gist
import plotly.graph_objects as go
from models import classifier


def app():
    st.markdown("## **Proses Pengklasifikasian Topik**")

    st.write("""
            <div style="text-align:justify;">
                Topik Klasifikasi merupakan adalah teknik penentuan untuk menentukan suatu topik dari sebuah teks. 
                Pada penelitian ini, untuk melakukan klasifikasi pada data yang telah di preprocessing digunakan 
                metode Word Cloud dan Pengurutan Kata Terbanyak dari keseluruhan dataset yang digabungkan.
            </div>    
    """, unsafe_allow_html=True)

    st.markdown("### **1. WordCloud**")
    st.write("""
         <div style="text-align:justify;">
            Word cloud (disebut juga text cloud atau tag cloud) merupakan salah satu metode untuk menampilkan data teks secara visual. 
            Grafik ini populer dalam text mining karena mudah dipahami. 
            Dengan menggunakan word cloud, gambaran frekuensi kata-kata dapat ditampilkan dalam bentuk yang menarik namun tetap informatif. 
        </div>    
    """, unsafe_allow_html=True)

    github_gist("https://gist.github.com/ShinyQ/359a063d0feb3d0be01afca1edafa5fd", height=360, width=900)

    st.write("Berikut merupakan hasil dari wordcloud yang telah diolah.")

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

    st.write("### **2. Pengurutan Kata Terbanyak**")
    st.write("""
         <div style="text-align:justify;">
            Dalam penentuan pemilihan topik klasifikasi, kami menggunakan kata dengan jumlah kemunculan 
            terbanyak dari hasil crawling data dan hasil kata dari wordcloud. Adapun hasil dari penggabungan.
            keseluruhan dataset tersebut ditampilkan tabel dibawah. Kemudian, berdasarkan hasil 
            pengolahan seluruh kata untuk setiap dataset didapatkan beberapa topik klasifikasi dan sub topik yang 
            dijabarkan pada tabel sebagai berikut. <br><br>
        </div>    
    """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:
        st.write("#### **Tabel Pengurutan Kata Terbanyak**")
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

        fig.update_layout(margin=dict(l=0, r=240, t=0, b=0))
        st.plotly_chart(fig)

    with col6:
        st.write("#### **Hasil Pengklasifikasian Topik Dan Sub-Topik**")
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['Topik', 'Sub Topik'],
                align='center',
                font_size=13,
                height=30,

            ),
            cells=dict(
                values=[
                    ['Pengaksesan', 'Transaksi', 'Akun', 'Pelayanan', 'Performa'],
                    [
                        'Login, Register, OTP, Kode, Pin',
                        'Transfer, Pembelian, Pembayaran, Saldo, Topup, Top, Up, Beli, Listrik, Transaksi, Biaya, Potongan, Uang, Beli',
                        'Upgrade, Verifikasi, KTP, Premium, Akun',
                        'Email, WA, Whatsapp, Telpon, CS, Telfon, Respon, Customer Service',
                        'Lambat, Lag, Cepat, Performa'
                    ]
                ],
                align='center',
                font_size=13,
                height=50
            )
        )])

        fig.update_layout(margin=dict(l=0, r=240, t=0, b=0))
        st.plotly_chart(fig)

    st.markdown("### **4. Contoh Hasil Pembagian Klasifikasi Topik**")
    st.write("""
         <div style="text-align:justify;">
            Setelah melakukan proses penentuan topik dan sub-topik untuk pengklasifikasian setiap macam masalah maka
             langkah selanjutnya yang dilakukan adalah mengklasifikasikan setiap dataset kedalam topik yang telah ditentukan. 
        </div>    
    """, unsafe_allow_html=True)

    github_gist("https://gist.github.com/ShinyQ/67063ba772f91ad21ea88f4b85d282ac", height=360, width=900)
    st.write("Adapun beberapa contoh hasil dari pengklasifikasi topik dan sub topik dijabarkan sebagai berikut.")
    data = classifier.DataFrameClassifier('dataset/raw/ovo.csv', "comments").sample(8)
    st.table(data)
