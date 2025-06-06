import pandas as pd
import re
import string

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

kamus_alay1 = pd.read_csv('./dataset/processed/Kamu-Alay.csv')
kamus_alay1 = kamus_alay1.set_index('kataAlay')

kamus_alay2 = pd.read_csv('./dataset/processed/colloquial-indonesian-lexicon.csv')
kamus_alay2 = kamus_alay2.filter(['slang', 'formal'], axis=1)

kamus_alay2 = kamus_alay2.drop_duplicates(subset=['slang'], keep='first')
kamus_alay2 = kamus_alay2.set_index('slang')

stopword1 = list(pd.read_csv('./dataset/processed/stopwords_id_satya.txt', header=None)[0])
custom_word = ['nya', 'tolong', 'iya', 'guna', 'kasih', 'buka', 'hari', 'sih', 'mohon', 'baru']


def CleanText(text):
    temp_text_split = []

    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'(@\w+|#\w+)', '', text)
    text = re.sub('<.*?>', '', text)
    text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub("\n", " ", text)
    text = text.lower()
    text = re.sub(r"(username|user|url|rt|xf|fx|xe|xa)\s|\s(user|url|rt|xf|fx|xe|xa)", "", text)
    text = re.sub(r'(\w)(\1{2,})', r"\1", text)
    text = re.sub(r"\b[a-zA-Z]\b", "", text)
    text = re.sub('(s{2,})', ' ', text)
    text = ' '.join(text.split())

    text_split = text.split(' ')

    for i in range(len(text_split)):
        if text_split[i] in kamus_alay1.index:
            text_split[i] = kamus_alay1.loc[text_split[i]]['kataBaik']
        elif text_split[i] in kamus_alay2.index:
            text_split[i] = kamus_alay2.loc[text_split[i]]['formal']

    stemmer.stem(text)

    for i in range(len(text_split)):
        if (text_split[i] not in stopword1) and (text_split[i] not in custom_word):
            temp_text_split.append(text_split[i])

    final_text = ' '.join(temp_text_split)

    return final_text

