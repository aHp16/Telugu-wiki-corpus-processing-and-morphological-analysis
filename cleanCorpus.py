import re

input_file = "downloaded_text/sentence-corpus.txt"
output_file = "downloaded_text/cleanCorpus.txt"

allowed_punctuation = {".", "!", "?", "।", "॥"}

def clean_text(text):
    return "".join(char if char.isalnum() or char.isspace() or char in allowed_punctuation else "" for char in text)

with open(input_file, "r", encoding="utf-8") as infile:
    sentences = infile.readlines()

cleaned_sentences = [clean_text(sentence.strip()) for sentence in sentences]

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("\n".join(cleaned_sentences) + "\n")

print("Cleaned corpus saved as 'cleanCorpus.txt'.")
#step6
