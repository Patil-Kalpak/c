# Tokenization Task

# Input paragraph as string
paragraph = "Natural Language Processing is very interesting. It is used in chatbots and translation systems."

# Split paragraph into sentences
sentences = paragraph.split(".")

print("Sentences:")
for s in sentences:
    
    # Remove extra spaces
    s = s.strip()
    
    # Ignore empty sentence
    if s != "":
        print(s)

# Split sentences into words
all_words = []

print("\nWords:")

for s in sentences:
    
    s = s.strip()
    
    if s != "":
        
        # Split sentence into words
        words = s.split()
        
        print(words)
        
        # Store words for token counting
        all_words.extend(words)

# Count total tokens
total_tokens = len(all_words)

print("\nTotal Tokens:", total_tokens)