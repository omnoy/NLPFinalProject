import pyarrow.parquet as pq
import pandas as pd
from random import shuffle
from tensorflow.keras.preprocessing.text import Tokenizer


class SentimentTokenizer:
    def __init__(self, train_path: str, validation_path: str, verdict_df_path: str):
        # Read the Parquet file
        df_train = pq.read_table(train_path)
        df_train = df_train.to_pandas()

        df_test = pq.read_table(validation_path)
        df_test = df_test.to_pandas()

        self.train = [(label, text) for label, text in zip(df_train['label'], df_train['text'])]
        shuffle(self.train)
        self.validation = [(label, text) for label, text in zip(df_test['label'], df_test['text'])]
        shuffle(self.validation)

        self.x_train = []
        self.y_train = []
        self.x_validation = []
        self.y_validation = []

        for inx, (ty, tx) in enumerate(self.train):
            self.y_train.append(ty)
            self.x_train.append(tx)

        for inx, (ty, tx) in enumerate(self.validation):
            self.y_validation.append(ty)
            self.x_validation.append(tx)


        verdicts_df = pd.read_excel(verdict_df_path)
        verdicts_text = list(verdicts_df['פסק-דין'])

        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(self.x_train + self.x_validation + verdicts_text)

