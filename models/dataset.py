import streamlit as st
import pandas as pd


@st.cache
def raw_data():
    df_saku = pd.read_csv("./dataset/raw/sakuku.csv")
    df_ovo = pd.read_csv("./dataset/raw/ovo.csv")
    df_link = pd.read_csv("./dataset/raw/link.csv")
    df_dana = pd.read_csv("./dataset/raw/dana.csv")

    return df_dana, df_ovo, df_link, df_saku
