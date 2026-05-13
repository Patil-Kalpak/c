# Rule-Based Chunking (Noun Phrase Detection)

# Given sentence
sentence = "The beautiful girl"

# Convert into words
words = sentence.lower().split()

# Grammar lists
determiners = ["a", "an", "the"]
adjectives = ["beautiful", "smart", "happy", "big"]
nouns = ["girl", "boy", "apple", "car"]

# Rule:
# NP = Determiner + Adjective + Noun

if len(words) == 3:

    det = words[0]
    adj = words[1]
    noun = words[2]

    if (det in determiners and
        adj in adjectives and
        noun in nouns):

        print("Noun Phrase (NP) Found")

    else:
        print("No Noun Phrase Found")

else:
    print("Invalid Pattern")