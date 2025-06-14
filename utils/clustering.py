from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_keywords(keywords, n_clusters=5):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(keywords)
    model = KMeans(n_clusters=n_clusters)
    model.fit(X)
    labels = model.labels_
    clusters = {}
    for label, kw in zip(labels, keywords):
        clusters.setdefault(f"Cluster {label+1}", []).append(kw)
    return clusters
