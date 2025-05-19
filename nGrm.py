import re
import nltk
import matplotlib.pyplot as plt
from nltk import word_tokenize, FreqDist, bigrams

# Download necessary NLTK resources
nltk.download('punkt')

# File paths
input_file = 'downloaded_text/cleanCorpus.txt'
unigram_file = 'wordUnigramFreq.txt'
bigram_file = 'wordBigramFreq.txt'

# Read and preprocess the corpus
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read().lower()  # Convert to lowercase

# Tokenization: Capture both English and Telugu words
tokens = word_tokenize(text)

# Filter tokens to retain only Telugu and English words (ignoring special characters)
tokens = [token for token in tokens if re.match(r'[a-zA-Z\u0C00-\u0C7F]+', token)]

# Generate unigram frequencies
unigram_freq = FreqDist(tokens)

# Save unigram frequencies
with open(unigram_file, 'w', encoding='utf-8') as f:
    for word, freq in unigram_freq.items():
        f.write(f"{word}\t{freq}\n")

# Generate bigrams
bigrams_list = list(bigrams(tokens))
bigram_freq = FreqDist(bigrams_list)

# Save bigram frequencies
with open(bigram_file, 'w', encoding='utf-8') as f:
    for (w1, w2), freq in bigram_freq.items():
        f.write(f"{w1} {w2}\t{freq}\n")

# Plot top 20 unigrams
plt.figure(figsize=(10, 5))
unigram_freq.plot(20, title="Top 20 Unigram Frequencies")

# Plot top 20 bigrams
top_bigrams = bigram_freq.most_common(20)
bigram_labels = [f"{w1} {w2}" for (w1, w2), _ in top_bigrams]
bigram_counts = [count for _, count in top_bigrams]

plt.figure(figsize=(12, 6))
plt.bar(bigram_labels, bigram_counts, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Top 20 Bigram Frequencies")
plt.xlabel("Bigrams")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("✅ Word unigram and bigram frequencies saved successfully!")
#step 7
