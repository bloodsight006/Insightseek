from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SearchEngine:

    def __init__(self, documents):

        self.vectorizer = TfidfVectorizer(stop_words="english")

        self.tfidf_matrix = self.vectorizer.fit_transform(documents)

    def search(self, query):

        query_vector = self.vectorizer.transform([query])

        similarity = cosine_similarity(query_vector, self.tfidf_matrix)

        return similarity.flatten()
    