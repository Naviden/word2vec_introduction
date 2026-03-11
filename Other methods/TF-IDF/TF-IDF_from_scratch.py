import math
import re
from collections import Counter


def tokenize(text):
    """
    Convert text to lowercase and split into words.
    Keeps only letters, numbers, and underscores.
    """
    return re.findall(r"\b\w+\b", text.lower())


def compute_tf(document):
    """
    Term Frequency (TF):
    number of times a word appears in a document
    divided by total number of words in that document
    """
    tokens = tokenize(document)
    total_terms = len(tokens)
    counts = Counter(tokens)

    tf = {}
    for term, count in counts.items():
        tf[term] = count / total_terms

    return tf


def compute_idf(documents):
    """
    Inverse Document Frequency (IDF):
    log(N / df)
    where:
    - N = number of documents
    - df = number of documents containing the term
    """
    N = len(documents)
    doc_freq = {}

    for document in documents:
        tokens = set(tokenize(document))  # unique terms only
        for term in tokens:
            doc_freq[term] = doc_freq.get(term, 0) + 1

    idf = {}
    for term, df in doc_freq.items():
        idf[term] = math.log(N / df)

    return idf


def compute_tfidf(documents):
    """
    Compute TF-IDF for each document.
    Returns a list of dictionaries, one per document.
    """
    idf = compute_idf(documents)
    tfidf_documents = []

    for document in documents:
        tf = compute_tf(document)
        tfidf = {}

        for term, tf_value in tf.items():
            tfidf[term] = tf_value * idf[term]

        tfidf_documents.append(tfidf)

    return tfidf_documents


# Example usage
documents = [
    "The cat sat on the mat",
    "The cat ate the mouse",
    "The dog sat on the log of the cat"
]

tfidf_result = compute_tfidf(documents)

for i, doc_vector in enumerate(tfidf_result, start=1):
    print(f"\nDocument {i}")
    for term, score in sorted(doc_vector.items()):
        print(f"{term}: {score:.4f}")