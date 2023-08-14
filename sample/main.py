from court_scraper.CourtScraperToExcel import CourtScraperToExcel
from nlp.tf_idf import court_tfidf
from nlp.ExtractKeywords import extract_text_keywords

docto = CourtScraperToExcel().get_df()

tfidf_subjects = []
for verdict in docto.df['פסק-דין']:
    subject = court_tfidf(verdict).get_results()
    tfidf_subjects.append(",".join(subject))

word2vec_subjects = []
for verdict in docto.df['פסק-דין']:
    subject = extract_text_keywords(verdict)
    word2vec_subjects.append(",".join(subject))

#print(subjects)
docto.df['tfidf subjects'] = tfidf_subjects
docto.df['word2vec subjects'] = word2vec_subjects
docto.save("CourtVerdicts")
