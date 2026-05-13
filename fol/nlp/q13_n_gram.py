# N-gram Text Generation using Bigram

import random

# Given text
text = "I love NLP and I love Python"

# Convert text into words
words = text.lower().split()

# Create bigrams
bigrams = {}

for i in range(len(words) - 1):

    current_word = words[i]
    next_word = words[i + 1]

    # Create list if word not present
    if current_word not in bigrams:
        bigrams[current_word] = []

    # Store next word
    bigrams[current_word].append(next_word)

# Display bigrams
print("Bigram Pairs:\n")

for key, value in bigrams.items():
    print(key, "->", value)

# Starting word
start = "i"

# Generate text
generated_text = start

for i in range(5):

    if start in bigrams:

        # Select random next word
        next_word = random.choice(bigrams[start])

        generated_text += " " + next_word

        start = next_word

    else:
        break

# Display generated text
print("\nGenerated Text:")
print(generated_text)