# Information Extraction using Named Entity Recognition (NER)

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download required packages
nltk.download('punkt')
nltk.download('punkt_tab')

nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')

nltk.download('words')

# Given sentence
text = "Barack Obama visited India and met Narendra Modi in Delhi"

# Tokenization
words = word_tokenize(text)

# POS Tagging
pos = pos_tag(words)

# Named Entity Recognition
ner = ne_chunk(pos)

# Display entities
print("\nNamed Entities:\n")

for subtree in ner:

    # Check named entities
    if hasattr(subtree, 'label'):

        entity_name = ""

        for leaf in subtree.leaves():
            entity_name += leaf[0] + " "

        print(entity_name.strip(), "->", subtree.label())