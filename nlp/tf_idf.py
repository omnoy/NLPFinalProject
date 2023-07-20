import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class court_tfidf:

    def __init__(self, judgment: str):
        self.judgment = judgment.replace("\xa0", "").replace("\n", " ").replace("  ", " ")

        self.sentences = self.judgment.split(".")

        #self.sentences = self.sentences[:-5]  # Remove 2 last cell from list

        self.count = CountVectorizer()
        word_count = self.count.fit_transform(self.sentences)

        tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
        tfidf_transformer.fit(word_count)
        self.df_idf = pd.DataFrame(tfidf_transformer.idf_, index=self.count.get_feature_names_out(),
                                   columns=["idf_weights"])

        self.df_idf.sort_values(by=['idf_weights'], ascending=False, inplace=True)

    def get_results(self):
        result = []
        for word in self.df_idf.index.values:
            if len(result) == 5:
                break
            if not word.isdigit():
                result.append(word)
        return result
