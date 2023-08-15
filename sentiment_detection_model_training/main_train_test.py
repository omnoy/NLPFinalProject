import pyarrow.parquet as pq
import pandas as pd
from random import shuffle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sentiment_analysis_model import sentiment_analysis_model


# Read the Parquet file
df_train = pq.read_table('dataset/hebrew_sentiment-train.parquet')
df_train = df_train.to_pandas()

df_test = pq.read_table('dataset/hebrew_sentiment-test.parquet')
df_test = df_test.to_pandas()

train = [(label,text) for label,text in zip(df_train['label'],df_train['text'])]
shuffle(train)
validation = [(label,text) for label,text in zip(df_test['label'],df_test['text'])]
shuffle(validation)

print(f"DB Size: {len(train) + len(validation)}")
print(f"Train Size: {len(train)}")
print(f"Vali Size: {len(validation)}")

x_train = []
y_train =[]
x_validation = []
y_validation =[]

for inx,(ty,tx) in enumerate(train):
    y_train.append(ty)
    x_train.append(tx)

for inx,(ty,tx) in enumerate(validation):
    y_validation.append(ty)
    x_validation.append(tx)


tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train + x_validation)


sequences_train = tokenizer.texts_to_sequences(x_train)
sequences_validation = tokenizer.texts_to_sequences(x_validation)


max_length = max([len(seq) for seq in sequences_train + sequences_validation])

padded_sequences_train = pad_sequences(sequences_train, maxlen=max_length, padding='post')
padded_sequences_validation = pad_sequences(sequences_validation, maxlen=max_length, padding='post')

model = sentiment_analysis_model(tokenizer=tokenizer,
                               max_length=max_length,y_train=y_train)

model.fit(padded_sequences_train=padded_sequences_train)
model.test(validation=validation,padded_sequences_validation=padded_sequences_validation)