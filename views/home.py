import streamlit as st


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
            Kombinasi pendekatan deep learning dan pemrosesan bahasa alami diterapkan untuk menganalisis sentimen dari 
            teks untuk kalimat tertentu. Era digital membuat banyak hal untuk beradaptasi karena cepat dan mudahnya 
            informasi untuk didapatkan serta disebarluaskan. 
            Proses transaksi keuangan merupakan hal yang sangat sering dijumpai, Bahkan saat ini transaksi 
            keuangan sudah banyak dilakukan dengan teknologi yang sering disebut dengan dompet digital. 
            Teknologi dompet digital juga didukung oleh budaya orang yang mulai menyukai pembayaran cashless 
            sehingga banyak perusahaan yang menyediakan jasa tersebut seperti DANA, OVO, Link Aja dan Sakuku. 
            Kualitas dari perusahaan dompet digital dinilai dari ulasan konsumen dan orang lain ingin mengerti 
            dari ulasan satu orang. Pendapat konsumen ini diatur dengan cara yang terstruktur dan untuk memahami 
            persepsi ulasan dan reaksi konsumen. Data ulasan konsumen kami dapatkan melalui review yang ada pada 
            google play store. Kemudian membuat kumpulan data yang telah kami crawling dan melakukan pengolahan 
            data terelebih dahulu. Dengan menggunakan, arsitektur CNN LSTM gabungan digunakan dalam dataset 
            kami dan mendapatkan akurasi training sebesar 88% dan akurasi validasi sebesar 83%
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
            **3. Aspect Classification**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Menganalisis aspek-aspek penting pada sentimen untuk diklasifikasikan. Adapun beberapa
                hal yang dilakukan untuk mendapatkan beberapa klasifikasi adalah dengan mengobservasi pada
                kata terbanyak serta dengan membuat wordcloud. 
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            **4. Sentiment Analysis Modelling**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                 Melakukan pemodelan untuk proses analisis sentimen yang akan dibuat menggunakan model CNN-LSTM dengan 
                 menggunakan library Ternsorflow.
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            **5. Sentiment Analysis Result**
            <div style="text-align:justify; margin-top:-2%; margin-bottom:5%">
                Mengklasifikasikan seluruh hasil sentimen dan memvisualisasikannya untuk mendapatkan insight 
                pada setiap jenis e-wallet yang ditentukan dalam penelitian ini.
            </div>
        """, unsafe_allow_html=True)
