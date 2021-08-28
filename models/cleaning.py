import pandas as pd
import re
import string
import streamlit as st
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

kamus_alay = pd.read_csv('./dataset/processed/Kamu-Alay.csv')
kamus_alay = kamus_alay.set_index('kataAlay')
kamusAlay = pd.read_csv('./dataset/processed/colloquial-indonesian-lexicon.csv')
stopWord = list(pd.read_csv('./dataset/processed/stopwords_id_satya.txt', header = None)[0])

def DataCleaning(text):
    text_temp = CleanText(text)
    st.write(text_temp)
    text_temp = ApplyKamusAlayStopTranslate(text_temp)
    st.write(text_temp)
    text_temp = Stemming(text_temp)
    st.write(text_temp)

def CleanText(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub('(@\w+|#\w+)','',text)
    text = re.sub('<.*?>', '', text)
    text = text.translate(str.maketrans(' ',' ',string.punctuation))
    text = re.sub('[^a-zA-Z]',' ',text)
    text = re.sub("\n"," ",text)
    text = text.lower()
    text = re.sub("(username|user|url|rt|xf|fx|xe|xa)\s|\s(user|url|rt|xf|fx|xe|xa)","",text)
    text = re.sub(r'(\w)(\1{2,})', r"\1", text)
    text = re.sub(r"\b[a-zA-Z]\b","",text)
    text = re.sub('(s{2,})',' ',text)
    text = ' '.join(text.split())

    return text

def ApplyKamusAlayStopTranslate(text):
    text = text.split(' ')
    temp = []

    for i in range(len(text)):
        try:
            text[i] = kamus[text[i]]
        except:
            pass

        try:
            index = kamusAlay.index[kamusAlay['slang'] == text[i]][0]
            text[i] = kamusAlay['formal'][index]
        except:
            pass

        try:
            text[i] = kamus_alay.loc[text[i]]['kataBaik']
        except:
            pass

        try:
            if (text[i] in stopWord):
                text.remove(text[i])
        except:
            pass

    text = ' '.join(text)
    return text

def Stemming(text):
    return stemmer.stem(text)