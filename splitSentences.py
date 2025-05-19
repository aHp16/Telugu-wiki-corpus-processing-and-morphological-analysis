import re

input_file = 'downloaded_text/corpus.txt'
output_file = 'downloaded_text/sentence-corpus.txt'

decimal_pattern = re.compile(r'\d+\.\d+')
telugu_abbreviations = {'డా.', 'శ్రీ.', 'కుం.', 'ప్రొ.', 'జే.ఎన్.', 'ఇ.స.'}

def preprocess_text(text):
    return re.sub(r'\s+', ' ', text.strip())

def tokenize_sentences(text):
    text = decimal_pattern.sub(lambda m: m.group().replace('.', '@DOT@'), text)
    for abbr in telugu_abbreviations:
        text = text.replace(abbr, abbr.replace('.', '@ABBR@'))
    
    sentences = re.split(r'(?<=[.!?।॥])\s+', text)
    
    return [s.replace('@DOT@', '.').replace('@ABBR@', '.').strip() for s in sentences]

with open(input_file, 'r', encoding='utf-8') as infile:
    raw_text = infile.read()

cleaned_text = preprocess_text(raw_text)
sentences = tokenize_sentences(cleaned_text)

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("\n".join(sentences) + "\n")

print("Sentence tokenization complete! Saved as 'sentence-corpus.txt'.")
#step4




"""import re

# Input and output file paths
input_file = "downloaded_text/corpus.txt"
output_file = "downloaded_text/sentence-corpus.txt"

def split_into_sentences(text):
    #Splits text into sentences, removes standalone numbers, and cleans up empty lines
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split at sentence-ending punctuation
    clean_sentences = []
    
    for s in sentences:
        s = s.strip()
        if s and not re.match(r'^\d+$', s):  # Remove blank lines & standalone numbers
            clean_sentences.append(s)

    return clean_sentences

def process_corpus(input_path, output_path):
    #Reads corpus, splits into sentences, and writes to a new file.
    with open(input_path, "r", encoding="utf-8") as infile:
        text = infile.read()

    sentences = split_into_sentences(text)

    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(sentences))

    print(f"✅ Processed corpus saved as: {output_path}")

# Run the function
process_corpus(input_file, output_file) """


