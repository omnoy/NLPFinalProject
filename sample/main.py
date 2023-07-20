from court_scraper.CourtScraperToExcel import CourtScraperToExcel
from nlp.tf_idf import court_tfidf


docto = CourtScraperToExcel().get_df()
subjects = []
for row in docto.df['פסק-דין']:
    subject = court_tfidf(row).get_results()
    subjects.append(",".join(subject))

#print(subjects)
docto.df['נושא'] = subjects
docto.save("CourtVerdicts")
