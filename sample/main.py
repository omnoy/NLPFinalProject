from court_scraper.CourtScraperToExcel import CourtScraperToExcel
from nlp.TfIdfKeywordExtractor import court_tfidf
from nlp.Word2VecKeywordExtractor import extract_text_keywords
from nlp.SentimentAnalyzer import sentiment_analyzer
from nlp.AutoencoderKeywordExtractor import KeyWord_Autoencoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sentiment_detection_model_training.sentiment_analysis_model import sentiment_analysis_model

docto = CourtScraperToExcel().get_df()

tfidf_subjects = []
word2vec_subjects = []
autoencoder_subjects = []

for verdict in docto.df['פסק-דין']:
    # get predicted subjects using tf_idf algorithm
    tf_idf_subject = court_tfidf(verdict).get_results()
    tfidf_subjects.append(",".join(tf_idf_subject))

    # get predicted subjects using word2vec
    word2vec_subject = extract_text_keywords(verdict)
    word2vec_subjects.append(",".join(word2vec_subject))

    # get subjects using an autoencoder
    # autoencoder = KeyWord_Autoencoder(texts=[verdict])
    # autoencoder.fit()
    # top_words = autoencoder.predict()
    # autoencoder_subjects.append(",".join(top_words[0]))
    # del autoencoder


docto.df['tfidf subjects'] = tfidf_subjects
docto.df['word2vec subjects'] = word2vec_subjects
#docto.df['autoencoder subjects'] = autoencoder_subjects

# Predict Sentiments
texts = [t for t in docto.df['פסק-דין']]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
max_length = max([len(seq) for seq in sequences])

padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

model = sentiment_analysis_model(tokenizer=tokenizer, max_length=max_length, path='C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\rnn_models\\sentiment_analysis_model_weights.h5')
result = model.predict(texts=texts, padded_sequences=padded_sequences)

sentiments = [sentiment_analysis_model.sentiment_text[value] for value in result.values()]
print(sentiments)
docto.save("CourtVerdicts")
