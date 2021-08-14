import streamlit as st
from views import home

st.set_page_config(
    page_title='Yasudahlah Team - IFest 2021 Unpad',
    page_icon='https://telkomuniversity.ac.id/wp-content/uploads/2019/07/cropped-favicon-2-32x32.png',
    layout='wide'
)

PAGES = {
    "🏠 Halaman Utama": home,
}

st.sidebar.subheader('Navigasi')

page = st.sidebar.selectbox("Pindah Halaman", list(PAGES.keys()))
page = PAGES[page]
page.app()
