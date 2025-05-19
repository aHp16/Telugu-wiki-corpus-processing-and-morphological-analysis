import os

input_file = 'downloaded_text/sentence-corpus.txt'
output_file = 'downloaded_text/sentence-stats.txt'

def calculate_statistics(sentences):
    stats = []
    total_words = 0

    for i, sentence in enumerate(sentences, start=1):
        word_count = len(sentence.split())
        char_count = len(sentence)
        total_words += word_count
        stats.append((i, word_count, char_count))
    
    avg_words = total_words / len(sentences) if sentences else 0
    
    return stats, avg_words

if os.path.exists(input_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        sentences = [line.strip() for line in infile if line.strip()]

    stats, avg_words = calculate_statistics(sentences)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("Sentence ID | Total Words | Total Characters\n")
        outfile.write("-" * 40 + "\n")
        for sid, words, chars in stats:
            outfile.write(f"{sid:<11} | {words:<12} | {chars}\n")
        outfile.write(f"\nAverage words per sentence: {avg_words:.2f}\n")

    print(f"Statistics saved to '{output_file}'.")

else:
    print(f"Error: '{input_file}' not found.")
#step5

"""# Load sentences from file
with open('sentence-corpus.txt', 'r', encoding='utf-8') as f:
    sentences = [line.strip() for line in f if line.strip()]

total_sentences = len(sentences)
total_words_all = 0

# Collect stats per sentence
stats = []

for idx, sentence in enumerate(sentences, start=1):
    word_count = len(sentence.split())
    char_count = len(sentence)
    total_words_all += word_count
    stats.append((idx, sentence, word_count, char_count))

# Calculate overall average words per sentence
average_words = total_words_all / total_sentences if total_sentences else 0

# Display result table
print(f"{'Sentence ID':<12} | {'Sentence':<60} | {'Words':<5} | {'Avg Words/Sent':<18} | {'Chars':<6}")
print("-" * 120)

for stat in stats:
    sentence_id, sentence, word_count, char_count = stat
    # Trim sentence to first 55 chars for clean tabular output
    trimmed_sentence = sentence if len(sentence) <= 55 else sentence[:52] + "..."
    print(f"{sentence_id:<12} | {trimmed_sentence:<60} | {word_count:<5} | {average_words:<18.2f} | {char_count:<6}")  """

