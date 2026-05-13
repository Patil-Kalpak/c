# TF-IDF Calculation

documents = [
    "NLP is interesting",
    "NLP is useful",
    "Machine learning is interesting"
]

# Convert documents into word lists
doc_words = []

for doc in documents:

    words = doc.lower().split()

    doc_words.append(words)

# Create vocabulary
vocab = []

for words in doc_words:

    for word in words:

        if word not in vocab:
            vocab.append(word)

# Total number of documents
N = len(documents)

print("Word\tTF\tIDF\tTF-IDF\n")

# Use first document for TF-IDF calculation
words = doc_words[0]

total_words = len(words)

for word in vocab:

    # Term Frequency
    tf = words.count(word) / total_words

    # Document Frequency
    df = 0

    for doc in doc_words:

        if word in doc:
            df += 1

    # Inverse Document Frequency
    import math

    idf = math.log(N / df)

    # TF-IDF
    tf_idf = tf * idf

    print(word, "\t", round(tf,2), "\t", round(idf,2), "\t", round(tf_idf,2))