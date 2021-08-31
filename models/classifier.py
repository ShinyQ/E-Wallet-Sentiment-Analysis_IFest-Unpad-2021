import numpy as np
import pandas as pd

topics = {
    "pengaksesan": ['login', 'register', 'kode', 'otp', 'pin'],
    "transaksi": [
        'transfer', 'pembelian', 'pembayaran', 'saldo', 'pulsa', 'topup',
        'top', 'up', 'beli', 'listrik', 'transaksi', 'biaya', 'potongan',
        'uang', 'beli'
    ],
    "akun": ['upgrade', 'verifikasi', 'ktp', 'premium', 'akun'],
    "cs": ['email', 'wa', 'whatsapp', 'telpon', 'cs', 'telfon', 'respon', 'customer service'],
    "performa": ['lambat', 'lag', 'cepat', 'performa']
}


def DataFrameClassifier(data_frame, text_column: str):
    data_frame = pd.read_csv(data_frame)
    df = data_frame.copy()
    final_dict = {
        'text': []
    }

    for topic in topics.keys():
        final_dict[topic] = np.zeros(shape=(len(df),))

    for i in range(len(df)):
        text = df.loc[i][text_column]
        final_dict['text'].append(text)
        classification = TextClassifying(text)
        for topic in classification:
            final_dict[topic][i] = 1

    final_df = pd.DataFrame(final_dict)

    for i in range(len(final_df)):
        jum = 0
        for topic in topics.keys():
            jum += final_df.loc[i][topic]

        if jum == 0:
            final_df = final_df.drop(i)

    final_df = final_df.reset_index(drop=True)

    return final_df


def TextClassifying(text):
    final_class = []
    text_split = text.split(' ')

    for i in range(len(text_split)):
        kata = text_split[i]
        for topic in topics.keys():
            if kata in topics[topic]:
                final_class.append(topic)

    return list(set(final_class))
