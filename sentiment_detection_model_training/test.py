import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sentiment_analysis_model import sentiment_analysis_model
from sentiment_detection_model_training.sentiment_tokenizer import SentimentTokenizer

# READ XLSX
df = pd.read_excel('CourtVerdicts.xlsx')


texts = [t for t in df['פסק-דין']]

tokenizer = SentimentTokenizer(train_path='dataset/hebrew_sentiment-train.parquet',
                               validation_path='dataset/hebrew_sentiment-test.parquet',
                               verdict_df_path='CourtVerdicts.xlsx').tokenizer

sequences = tokenizer.texts_to_sequences(texts)

max_length = 909

padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

model = sentiment_analysis_model(tokenizer=tokenizer, max_length=max_length, path='sentiment_analysis_model_weights.h5')

results = model.predict(texts=texts, padded_sequences=padded_sequences)

print([sentiment_analysis_model.sentiment_text[result['sentiment']] for result in results])
