import re
import numpy as np
from gensim.models import word2vec

def text_to_wordlist(text, stopword_list, remove_stopwords=True):
    # 2. Remove non-letters
    review_text = re.sub("\n", " ", text)
    review_text = re.sub("[^\u0590-\u05fe\']", " ", text)

    # 3. Convert words to lower case and split them, clean stopwords from model' vocabulary
    words = review_text.lower().split()
    meaningful_words = [w for w in words if not w in stopword_list]
    return (meaningful_words)


# Function to get feature vec of words
def get_feature_vec(words_list, model):
    # Index2word is a list that contains the names of the words in
    # the model's vocabulary. Convert it to a set, for speed
    clean_text = []
    # vocabulary, add its feature vector to the total
    for i, word in enumerate(words_list):
        if word in words_list:
            clean_text.append(model[i])

    return clean_text

def extract_text_keywords(text_review):
    with open("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\resources\\heb_stopwords.txt", encoding='utf8') as file:
        stopword_list = file.read().split("\n")

    with open("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\resources\\words_list_twitter.txt", encoding='utf8') as file:
        word_vec_names = file.read().split("\n")

    model = np.load("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\resources\\words_vectors_twitter.npy")
    # bag of word list without stopwords
    clean_train_text = (text_to_wordlist(text_review, stopword_list, remove_stopwords=True))

    # delete words which occur more than once
    clean_train = []
    for words in clean_train_text:
        if words in clean_train:
            words = 1
        else:
            clean_train.append(words)

    trainDataVecs = get_feature_vec(clean_train, model)
    trainData = np.asarray(trainDataVecs)

    # calculate cosine similarity matrix to use in pagerank algorithm for dense matrix, it is not
    # fast for sparse matrix
    # sim_matrix = 1-pairwise_distances(trainData, metric="cosine")

    # similarity matrix, it is 30 times faster for sparse matrix
    # replace this with A.dot(A.T).todense() for sparse representation
    similarity = np.dot(trainData, trainData.T)

    # squared magnitude of preference vectors (number of occurrences)
    square_mag = np.diag(similarity)

    # inverse squared magnitude
    inv_square_mag = 1 / square_mag

    # if it doesn't occur, set it's inverse magnitude to zero (instead of inf)
    inv_square_mag[np.isinf(inv_square_mag)] = 0

    # inverse of the magnitude
    inv_mag = np.sqrt(inv_square_mag)

    # cosine similarity (elementwise multiply by inverse magnitudes)
    cosine = similarity * inv_mag
    cosine = cosine.T * inv_mag


    # pagerank powermethod
    def powerMethod(A, x0, m, iter):
        n = A.shape[1]
        delta = m * (np.array([1] * n, dtype='float64') / n)
        for i in range(iter):
            x0 = np.dot((1 - m), np.dot(A, x0)) + delta
        return x0


    n = cosine.shape[1]  # A is n x n
    m = 0.15
    x0 = [1] * n

    pagerank_values = powerMethod(cosine, x0, m, 130)

    srt = np.argsort(-pagerank_values)
    a = srt[0:10]

    keywords_list = []

    for words in a:
        keywords_list.append(clean_train_text[words])

    return keywords_list