import re
import nltk
from collections import Counter
from nltk.util import ngrams

nltk.download('punkt')

# Load a large Telugu dictionary (pre-existing dataset)
telugu_dictionary_file = "telugu_words.txt"

# Read dictionary words (considering them as valid root words)
with open(telugu_dictionary_file, 'r', encoding='utf-8') as f:
    telugu_roots = set(f.read().splitlines())

# Common prefixes and suffixes in Telugu
telugu_prefixes = ["అ", "ఉ", "ప్ర", "సు", "ప"]
telugu_suffixes = ["ము", "లు", "వారు", "తో", "కి", "గా", "ని", "లో", "తా", "గా", "మూ", "చు"]

# Input corpus file
input_file = "sentence-corpus.txt"

# Read the corpus
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read().strip()

# Tokenize words (handles code-mixed language)
words = nltk.word_tokenize(text)

# Function to find root words
def stem_word(word):
    # If word is already in dictionary, return as root
    if word in telugu_roots:
        return word

    # Remove suffixes
    for suffix in telugu_suffixes:
        if word.endswith(suffix):
            stem = word[:-len(suffix)]
            if stem in telugu_roots:
                return stem

    # Remove prefixes
    for prefix in telugu_prefixes:
        if word.startswith(prefix):
            stem = word[len(prefix):]
            if stem in telugu_roots:
                return stem

    # Return original word if no root is found
    return word

# Perform stemming on all words
stemmed_words = [stem_word(word) for word in words]

# Generate bigrams for analysis
bigrams = list(ngrams(stemmed_words, 2))
bigram_freq = Counter(bigrams)

# Save results
with open("stemmed_words.txt", 'w', encoding='utf-8') as f:
    f.write("\n".join(stemmed_words))

with open("bigram_analysis.txt", 'w', encoding='utf-8') as f:
    for pair, freq in bigram_freq.items():
        f.write(f"{pair[0]} {pair[1]}\t{freq}\n")

print("✅ Morphological analysis complete! Results saved in 'stemmed_words.txt'.")
#step8
