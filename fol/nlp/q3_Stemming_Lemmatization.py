# Simple Rule-Based Stemmer

def stem_word(word):
    suffixes = ["ing", "ed", "ly", "es", "s"]

    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]

    return word


# Input from user
word = input("Enter a word: ")

stemmed = stem_word(word)

print("Original Word :", word)
print("Stemmed Word  :", stemmed)