# Bag of Words Implementation

sentences = [
    "I love NLP",
    "NLP is interesting",
    "I love programming"
]

# Create vocabulary
vocab = []

for sentence in sentences:
    words = sentence.lower().split()

    for word in words:
        if word not in vocab:
            vocab.append(word)

print("Vocabulary:", vocab)

# Display header
print("\nBag of Words Matrix:\n")

print("Sentence\t", end="")

for word in vocab:
    print(word, end="\t")

print()

# Create matrix
for sentence in sentences:

    words = sentence.lower().split()

    print(sentence, end="\t")

    for word in vocab:
        print(words.count(word), end="\t")

    print()