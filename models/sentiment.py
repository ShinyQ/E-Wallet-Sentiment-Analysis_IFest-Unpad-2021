import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def processed_data():
    df_saku = pd.read_csv("./dataset/sentiment/sakuku.csv")
    df_ovo = pd.read_csv("./dataset/sentiment/ovo.csv")
    df_link = pd.read_csv("./dataset/sentiment/link.csv")
    df_dana = pd.read_csv("./dataset/sentiment/dana.csv")

    return df_dana, df_ovo, df_link, df_saku


def percentage(df, name, seq):
    data = list(df.predict.value_counts())

    fig = px.pie(
        values=data, names=['Negatif', 'Positif'],
        color_discrete_sequence=seq,
    )

    fig.layout.showlegend = False
    fig.update_traces(textposition='inside', textinfo='percent+label+value')
    fig.update_layout(
        height=420,
        width=450,
        hovermode=False,
        margin=dict(l=0, r=0, t=100, b=0),
    )

    st.plotly_chart(fig)


def topic_percentage(name, seq):
    val = []
    feature = ['akun', 'cs', 'pengaksesan', 'performa', 'transaksi']

    for feat in feature:
        df = pd.read_csv('./dataset/sentiment_topic/' + name.lower() + '_' + feat + '.csv')
        val.append(len(df))

    names = ['Akun', 'Pelayanan', 'Pengaksesan', 'Performa', 'Transaksi']

    fig = px.bar(y=val, x=names, color=names, text=val, orientation='v', color_discrete_sequence=seq,)
    fig.update_layout(
        showlegend=False,
        height=450,
        width=550,
        hovermode=False,
        xaxis=dict(
            title="Jenis Topik"
        ),
        yaxis=dict(
            title="Nilai"
        )
    )
    st.plotly_chart(fig)
