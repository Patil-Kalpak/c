# Ambiguity Detection

sentence = input("Enter a sentence: ").lower()

# Words having multiple meanings
semantic_words = ["bank", "bat", "light", "crane", "match"]

# Check semantic ambiguity
semantic = False

for word in semantic_words:
    if word in sentence:
        semantic = True

# Check syntactic ambiguity
syntactic = False

if "with" in sentence or "while" in sentence:
    syntactic = True

# Display result
if syntactic:
    print("Syntactic Ambiguity")

elif semantic:
    print("Semantic Ambiguity")

else:
    print("No Ambiguity Detected")