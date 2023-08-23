from court_scraper.CourtScraperToExcel import CourtScraperToExcel
from nlp.TfIdfKeywordExtractor import court_tfidf
from nlp.Word2VecKeywordExtractor import extract_text_keywords
from nlp.AutoencoderKeywordExtractor import KeyWord_Autoencoder
from sentiment_detection_model_training.sentiment_analysis_model import sentiment_analysis_model
from sentiment_detection_model_training.sentiment_tokenizer import SentimentTokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tqdm import tqdm

docto = CourtScraperToExcel(year=2005,limit=50).get_df()

tfidf_subjects = []
word2vec_subjects = []
autoencoder_subjects = []
verdict_sentiments = []

for verdict in tqdm(docto.df['פסק-דין']):
    # get predicted subjects using tf_idf algorithm
    tf_idf_subject = court_tfidf(verdict).get_results()
    tfidf_subjects.append(",".join(tf_idf_subject))

    # get predicted subjects using word2vec
    word2vec_subject = extract_text_keywords(verdict)
    word2vec_subjects.append(",".join(word2vec_subject))

    # get subjects using an autoencoder
    autoencoder = KeyWord_Autoencoder(texts=[verdict])
    autoencoder.fit()
    top_words = autoencoder.predict()
    autoencoder_subjects.append(",".join(top_words[0]))
    del autoencoder


docto.df['tfidf subjects'] = tfidf_subjects
docto.df['word2vec subjects'] = word2vec_subjects
docto.df['autoencoder subjects'] = autoencoder_subjects

# Create sentiment analyzer and add to file
verdict_texts = [t for t in docto.df['פסק-דין']]

tokenizer = SentimentTokenizer(train_path='C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sentiment_detection_model_training\\dataset\\hebrew_sentiment-train.parquet',
                               validation_path='C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sentiment_detection_model_training\\dataset\\hebrew_sentiment-test.parquet',
                               verdict_df_path='CourtVerdicts.xlsx').tokenizer

sequences = tokenizer.texts_to_sequences(verdict_texts)

max_length = 909

padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

model = sentiment_analysis_model(tokenizer=tokenizer, max_length=max_length, path='C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sentiment_detection_model_training\\sentiment_analysis_model_weights.h5')

results = model.predict(texts=verdict_texts, padded_sequences=padded_sequences)

docto.df['sentiment'] = [sentiment_analysis_model.sentiment_text[result['sentiment']] for result in results]

docto.save("CourtVerdicts")
