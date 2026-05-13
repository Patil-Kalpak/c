# Simple Rule-Based POS Tagging

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:

    # Convert to lowercase for checking
    w = word.lower()

    # Rule-based tagging
    if w.endswith("ly"):
        tag = "Adverb"

    elif w.endswith("ing") or w.endswith("ed"):
        tag = "Verb"
    

    elif w in ["is", "am", "are", "was", "were", "eat", "eats", "go", "goes", "play", "plays"]:
        tag = "Verb"

    elif w in ["he", "she", "i", "we", "they", "you"]:
        tag = "Pronoun"

    elif word[0].isupper():
        tag = "Proper Noun"

    elif w in ["and", "or", "but"]:
        pos = "Conjunction"
    else:
        tag = "Noun"

    print(word, "->", tag)