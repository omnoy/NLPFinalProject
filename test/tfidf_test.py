import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
# using the count vectorizer
import re


class court_tfidf:

    def __init__(self, judgment: str):
        self.judgment = judgment.replace("\xa0", "").replace("\n", " ").replace("  ", " ")

        self.sentences = self.judgment.split(".")

        self.sentences = self.sentences[:-2]  # Remove 2 last cell from list

        self.count = CountVectorizer()
        word_count = self.count.fit_transform(text)

        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        tfidf_transformer.fit(word_count)
        self.df_idf = pd.DataFrame(tfidf_transformer.idf_, index=self.count.get_feature_names_out(),
                                   columns=["idf_weights"])

        self.df_idf.sort_values(by=['idf_weights'], ascending=False, inplace=True)

    def get_results(self, ):
        first_5_values = self.df_idf.head(5)
        return first_5_values['idf_weights']


data = pd.read_excel('test.xlsx')

text = data['פסק-דין'][0].replace("\xa0", "").replace("\n", " ").replace("  ", " ")
text = text.split(".")[:-2]

count = CountVectorizer()
word_count = count.fit_transform(text)

tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(word_count)
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count.get_feature_names_out(), columns=["idf_weights"])

df_idf.sort_values(by=['idf_weights'], ascending=False, inplace=True)

print(df_idf)
