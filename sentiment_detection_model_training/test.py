import pandas as pd
from random import shuffle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sentiment_analysis_model import sentiment_analysis_model

# READ XLSX
df = pd.read_excel('CourtVerdicts.xlsx')


texts = [t for t in df['פסק-דין']]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)


sequences = tokenizer.texts_to_sequences(texts)


max_length = max([len(seq) for seq in sequences])

padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

model = sentiment_analysis_model(tokenizer=tokenizer, max_length=max_length, path='sentiment_analysis_model_weights.h5')

result = model.predict(texts=texts, padded_sequences=padded_sequences)

print(result)