from court_scraper.CourtScraperToExcel import CourtScraperToExcel
from nlp.tf_idf import court_tfidf
from nlp.ExtractKeywords import extract_text_keywords
from nlp.SentimentAnalyzer import sentiment_analyzer
docto = CourtScraperToExcel().get_df()

tfidf_subjects = []
word2vec_subjects = []
verdict_sentiments = []
sent_analyzer = sentiment_analyzer()
for verdict in docto.df['פסק-דין']:
    #get predicted subjects using tf_idf algorithm
    tf_idf_subject = court_tfidf(verdict).get_results()
    tfidf_subjects.append(",".join(tf_idf_subject))

    #get predicted subjects using word2vec
    word2vec_subject = extract_text_keywords(verdict)
    word2vec_subjects.append(",".join(word2vec_subject))

    #get predicted sentiment
    verdict_sentiments.append(sent_analyzer.get_analysis(verdict))

docto.df['tfidf subjects'] = tfidf_subjects
docto.df['word2vec subjects'] = word2vec_subjects
docto.df['sentiment'] = verdict_sentiments
docto.save("CourtVerdicts")
