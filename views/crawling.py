import streamlit as st
from streamlit_embedcode import github_gist
from models import dataset


def app():
    st.markdown("# **Proses Data Crawling**")
    df_dana, df_ovo, df_link, df_saku = dataset.raw_data()
    st.write("""
         Pada tahap crawling data dilakukan proses pengambilan data review melalui playstore. 
         Adapun review data sentimen e-wallet yang akan diambil adalah review aplikasi e-wallet 
         pada perusahaan besar seperti aplikasi e-wallet OVO, Dana, LinkAja dan Sakuku.
    """)

    st.write("""
        Dalam melakukan crawling, kami menggunakan library
        [google-play-scraper](https://github.com/JoMingyu/google-play-scraper) untuk pengambilan review
        pada aplikasi e-wallet teratas di playstore. Adapun contoh implementasinya adalah sebagai berikut:
    """)

    github_gist("https://gist.github.com/ShinyQ/723dfa46bb648a01a7ebd41a1269bfb6", height=265, width=900)

    st.write("""
            Dari keseluruhan hasil crawling, didapatkan total 3978 dataset review untuk masing-masing 
            aplikasi e-wallet. Adapun dataset yang didapatkan ditampilkan seperti pada tabel berikut:
    """)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.markdown("### **Hasil Dataset Dana**")
        st.write(df_dana)

    with col2:
        st.markdown("### **Hasil Dataset OVO**")
        st.write(df_ovo)

    with col3:
        st.markdown("### **Hasil Dataset LinkAja**")
        st.write(df_link)

    with col4:
        st.markdown("### **Hasil Dataset Sakuku**")
        st.write(df_saku)
