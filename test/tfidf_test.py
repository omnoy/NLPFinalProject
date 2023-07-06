import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
#using the count vectorizer
import re

data = pd.read_excel('test.xlsx')

text = data['פסק-דין'][0].replace("\xa0","").replace("\n"," ").replace("  "," ")
print(text.split("."))
'''
count = CountVectorizer()
word_count=count.fit_transform(text)
print(word_count.toarray())

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count)
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count.get_feature_names_out(),columns=["idf_weights"])

df_idf.sort_values(by=['idf_weights'],ascending=False,inplace=True)

print(df_idf)

'''