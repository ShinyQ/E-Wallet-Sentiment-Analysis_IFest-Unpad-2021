import streamlit as st
import pandas as pd


@st.cache
def raw_data():
    df_saku = pd.read_csv("./dataset/raw/sakuku.csv").head(10)
    df_ovo = pd.read_csv("./dataset/raw/ovo.csv").head(10)
    df_link = pd.read_csv("./dataset/raw/link.csv").head(10)
    df_dana = pd.read_csv("./dataset/raw/dana.csv").head(10)

    return df_dana, df_ovo, df_link, df_saku
