import streamlit as st
import pandas as pd
from streamlit_embedcode import github_gist

def app():
    st.markdown("# Proses Preprocessing")
    st.write("""
            <div style="text-align:justify;">
                Data Preparation atau bisa disebut juga dengan data preprocessing adalah suatu proses atau langkah 
                yang dilakukan untuk membuat data mentah menjadi data yang berkualitas untuk proses selanjutnya
                dalam data mining. Data Preprocessing merupakan sebuah langkah penting dalam Data Mining karena
                pada umumnya data mentah memiliki banyak noise, ukuran yang besar, dan merupakan campuran
                dari berbagai macam sumber. Data preprocessing membantu didalam memperbaiki presisi dan
                kinerja data mining dan mencegah kesalahan didalam proses data mining. Adapun proses preprocessing
                yang dilakukan dalam analisis sentimen ini yaitu case folding, tokenizing, filtering, dan stemming.
            </div>
        """, unsafe_allow_html=True)

    st.write("### **1. Case Folding**")
    st.write("""
        <div style="text-align:justify;">
            Case folding adalah salah satu bentuk text preprocessing yang memiliki tujuan 
            untuk mengubah semua huruf dalam dokumen menjadi huruf kecil. Hanya huruf ‘a’ sampai ‘z’ yang diterima. 
            Karakter selain huruf dihilangkan dan dianggap delimiter (pembatas kata). Adapun case folding 
            dilakukan menggunakan function python yaitu lower().
        </div>
    """, unsafe_allow_html=True)

    st.write("### **2. Tokenizing**")
    st.write("""
        <div style="text-align:justify;">
            Tokenizing adalah metode untuk melakukan pemisahan kata dalam suatu kalimat dengan tujuan untuk proses analisis 
            teks lebih lanjut. Sebelum melakukan tokenizing biasanya melakukan proses case folding yang didalamnya 
            mencakup proses menghapus angka dan tanda baca yang tidak perlu, dan whitespace. Adapun dalam proses
            tokenizing analisis sentimen ini menggunakan beberapa aturan, diantaranya yaitu.
        </div>
        <li> Menghapus Link Dengan Pattern http/https dan </li>
        <li> Menghapus Karakter HTML </li>
        <li> Menghapus Tanda Baca (.,;:'"()?!%) </li>
        <li> Menghapus Karakter Selain Huruf a-z dan A-Z </li>
        <li> Mengganti Baris Baru Dengan Spasi </li>
        <li> Menghapus Karakter Berulang (Contoh: Horeeee!!!! menjadi Hore!) </li>
        <li> Menghapus 1 Karakter Terpisah </li>
        <li> Menghapus Spasi Yang Lebih Dari Satu </li>

        <br>Adapun kode yang dibuat untuk proses tokenizing adalah sebagai berikut.<br>
    """, unsafe_allow_html=True)

    github_gist("https://gist.github.com/ShinyQ/c62b36ecae197bca6ae1b42883ad76b4", height=450, width=900)

    st.write("### **3. Filtering**")
    st.write("""
        <div style="text-align:justify;">
            Filtering adalah tahap mengambil kata-kata penting dari hasil token dengan menggunakan algoritma 
            stoplist (membuang kata kurang penting) atau wordlist (menyimpan kata penting). Stopword adalah 
            kata umum yang biasanya muncul dalam jumlah besar dan dianggap tidak memiliki makna. 
            Contoh stopword dalam bahasa Indonesia adalah “yang”, “dan”, “di”, “dari”, dll. Untuk filtering pada 
            analisis sentimen projek ini digunakan beberapa jenis filtering yaitu.
        </div>    
        
        <li> 
            Menghapus kata pada kamus alay pada dataset 
            <a target="_blank" href="https://raw.githubusercontent.com/fendiirfan/Kamus-Alay/main/Kamu-Alay.csv">Kamus Alay</a> 
            dan <a target="_blank" href="https://raw.githubusercontent.com/nasalsabila/kamus-alay/master/colloquial-indonesian-lexicon.csv">colloquial-indonesian-lexicon</a> 
        </li>
        <li>
            Menghapus stopword Bahasa Indonesia menggunakan dataset 
            <a target="_blank" href="https://raw.githubusercontent.com/datascienceid/stopwords-bahasa-indonesia/master/stopwords_id_satya.txt">stopwords-id-satya</a> 
        </li>
        
        <br>Adapun kode yang dibuat untuk proses filtering adalah sebagai berikut.<br>
    """, unsafe_allow_html=True)

    github_gist("https://gist.github.com/ShinyQ/bb0e4264604c6a852694fbdab4539508", height=450, width=900)

    st.write("### **4. Stemming**")
    st.write("""
            <div style="text-align:justify;">
                Stemming adalah proses menghilangkan infleksi kata ke bentuk dasarnya (tidak terdapat imbuhan pada kata). 
                Misalnya kata “mendengarkan”, “dengarkan”, “didengarkan” akan ditransformasi menjadi kata “dengar”.
                Pada analisis sentimen ini kami menggunakan library <a target="_blank" href="https://github.com/har07/PySastrawi">Python Sastrawi</a> 
                untuk melakukan proses stemming setiap kata.
            </div>    

            <br>Adapun kode yang dibuat untuk proses filtering adalah sebagai berikut.<br>
    """, unsafe_allow_html=True)

    github_gist("https://gist.github.com/ShinyQ/67b2f82d77afe4ad106654c7679c8eca", height=220, width=900)

    st.write("### **Keseluruhan Kode Data Preprocessing**")
    github_gist("https://gist.github.com/ShinyQ/a859db53010c886745bd290ba91e1e1b", height=450, width=900)

    st.write("### **Contoh Hasil Proses Pre Processing**")
    data = pd.read_csv("./dataset/processed/ovo.csv").sample(8)
    st.table(data)