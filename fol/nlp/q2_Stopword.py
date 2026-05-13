# Stopword Removal using Manual List

# Given sentence
sentence = "This is a simple example of stopword removal in NLP"

# Predefined stopwords list
stopwords = ["is", "a", "of", "in", "this"]

# Convert sentence into words
words = sentence.lower().split()

# Store cleaned words
cleaned_words = []

# Remove stopwords manually
for word in words:
    
    if word not in stopwords:
        cleaned_words.append(word)

# Join words into cleaned sentence
cleaned_text = " ".join(cleaned_words)

# Display output
print("Original Sentence:")
print(sentence)

print("\nCleaned Text:")
print(cleaned_text)