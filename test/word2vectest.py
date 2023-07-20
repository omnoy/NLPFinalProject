import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
# using the count vectorizer
import re
from gensim.models import Word2Vec

data = pd.read_excel('test.xlsx')

text = data['פסק-דין'][0].replace("\xa0", "").replace("\n", " ").replace("  ", " ")
text = text.split(".")