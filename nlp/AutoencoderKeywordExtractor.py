import keras
import numpy as np
from keras.models import Model
from keras.layers import Input, Dense, LSTM, Embedding
from sklearn.preprocessing import normalize
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


class KeyWord_Autoencoder():


    SYMBOLS = ['[',']',"'",'"','0','1','2','3','4','5','6','7','8','9','(',')','.',',']

    SYMBOLS_TO_SPACE = ['-','\xa0','\0','\n','\r','\t','/',"\\",'  ']




    def __init__(self, texts, epochs=10, batch_size=1):

        self.texts = texts
        self.clean()

        self.epochs = epochs
        self.batch_size = batch_size

        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(self.texts)
        self.vocab_size = len(self.tokenizer.word_index) + 1

        self.X = self.tokenizer.texts_to_sequences(self.texts)
        self.X = pad_sequences(self.X)

        self.X = normalize(self.X, norm='l2')

        # Autoencoder architecture
        input_dim = self.X.shape[1]
        encoding_dim = 128  # Size of the LSTM encoding layer

        self.input_layer = Input(shape=(input_dim,))
        self.embedding = Embedding(input_dim=self.vocab_size, output_dim=128)(
            self.input_layer)  # Add an Embedding layer
        self.lstm_encoded = LSTM(encoding_dim)(self.embedding)
        self.decoded = Dense(input_dim, activation='sigmoid')(self.lstm_encoded)

        self.autoencoder = Model(inputs=self.input_layer, outputs=self.decoded)
        self.autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

    def clean(self):
        edit = []
        for t in self.texts:
            for s in self.SYMBOLS:
                t = t.replace(s, '')
            for st in self.SYMBOLS_TO_SPACE:
                t = t.replace(st, " ")
            txt = []
            for tx in t.split():
                if len(tx) > 0:
                    txt.append(tx)

            edit.append(" ".join(txt))
        self.texts = edit

    def fit(self):
        self.autoencoder.fit(self.X, self.X, epochs=self.epochs, batch_size=self.batch_size, verbose=False)

    def predict(self):
        encoded_words = []
        self.predict_encoder = Model(inputs=self.input_layer, outputs=self.lstm_encoded)
        encoded_texts = self.predict_encoder.predict(self.X)
        for values in encoded_texts:
            indexed_values = [(index, value) for index, value in enumerate(values)]
            sorted_values = sorted(indexed_values, key=lambda x: x[1], reverse=True)
            sorted_indices = [index for index, _ in sorted_values]
            res = []
            count = 0
            for inx in sorted_indices:
                if count == 5:
                    break
                try:
                    res.append(self.tokenizer.index_word[inx])
                    count += 1
                except:pass
            encoded_words.append(res)

        return encoded_words


    def save(self, name: str = "autoencoder.h5"):
        self.autoencoder.save(name)

    def load(self, path: str = None):
        if path:
            self.predict_encoder = keras.models.load_model(path)