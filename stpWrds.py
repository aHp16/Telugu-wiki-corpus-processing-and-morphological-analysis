import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stop words from NLTK (only once)
nltk.download('stopwords')
nltk.download('punkt')

# Define stop words for English & Telugu
english_stop_words = set(stopwords.words('english'))

# Custom Telugu stop words (expandable)
telugu_stop_words = {
    "ఇది", "అది", "నాకు", "మీ", "కాదు", "కాని", "ఈ", "అని", "లో", "వద్ద", "కూడా", "ఇలా", "ఎందుకు"
}

# Combine stop words
all_stop_words = english_stop_words.union(telugu_stop_words)

# File paths
input_file = "sentence-corpus.txt"
output_file = "cleaned-sentences.txt"

# Read the corpus
with open(input_file, 'r', encoding='utf-8') as f:
    sentences = f.readlines()

# Process sentences and remove stop words
cleaned_sentences = []
for sentence in sentences:
    # Tokenize words
    words = word_tokenize(sentence.lower())  # Convert to lowercase for uniformity

    # Remove stop words
    filtered_words = [word for word in words if word not in all_stop_words and re.match(r'[a-zA-Z\u0C00-\u0C7F]+', word)]

    # Reconstruct the sentence
    cleaned_sentence = ' '.join(filtered_words)
    cleaned_sentences.append(cleaned_sentence)

# Save the cleaned sentences
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(cleaned_sentences))

print(f"Stop words removed! Cleaned sentences saved to '{output_file}'.")
#step9
