from tensorflow.keras.preprocessing.sequence import pad_sequences
from sentiment_analysis_model import sentiment_analysis_model
from sentiment_detection_model_training.sentiment_tokenizer import SentimentTokenizer

sentiment_tokenizer = SentimentTokenizer(train_path='dataset/hebrew_sentiment-train.parquet',
                               validation_path='dataset/hebrew_sentiment-test.parquet',
                               verdict_df_path='CourtVerdicts.xlsx')

tokenizer = sentiment_tokenizer.tokenizer

x_train = sentiment_tokenizer.x_train
y_train = sentiment_tokenizer.y_train
x_validation = sentiment_tokenizer.x_validation
y_validation = sentiment_tokenizer.y_validation


sequences_train = tokenizer.texts_to_sequences(x_train)
sequences_validation = tokenizer.texts_to_sequences(x_validation)


max_length = max([len(seq) for seq in sequences_train + sequences_validation])

padded_sequences_train = pad_sequences(sequences_train, maxlen=max_length, padding='post')
padded_sequences_validation = pad_sequences(sequences_validation, maxlen=max_length, padding='post')

model = sentiment_analysis_model(tokenizer=tokenizer, max_length=max_length,y_train=y_train)

model.fit(padded_sequences_train=padded_sequences_train)
model.test(validation=sentiment_tokenizer.validation,padded_sequences_validation=padded_sequences_validation)