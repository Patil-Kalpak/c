# Simple CFG Parsing

# Given sentence
sentence = "Ram eats mango"

# Convert into words
words = sentence.lower().split()

# Grammar Rules
subjects = ["ram", "shyam", "boy", "girl"]
verbs = ["eat", "eats", "play", "plays", "like", "likes"]
objects = ["mango", "football", "apple", "music"]

# Check grammar
# S → Subject Verb Object

if len(words) == 3:

    subject = words[0]
    verb = words[1]
    obj = words[2]

    if (subject in subjects and
        verb in verbs and
        obj in objects):

        print("Valid Sentence")

    else:
        print("Invalid Sentence")

else:
    print("Invalid Sentence")