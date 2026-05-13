# Regex-based Text Cleaning

import re

# Input text
text = input("Enter text: ")

# Convert to lowercase
text = text.lower()

# Remove numbers
text = re.sub(r'[0-9]', '', text)

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Display cleaned text
print("\nCleaned Text:")
print(text)