import string
from collections import Counter

def load_stopwords(filename="stopwords.txt"):
    try:
        with open(filename, "r") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        print("Stopwords file not found")
        return set()

STOPWORDS = load_stopwords()

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return None

def clean_word(word):
    return word.strip(string.punctuation).lower()

def count_word_frequency(text):
    words = text.split()
    freq = Counter()

    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word and cleaned_word not in STOPWORDS:
            freq[cleaned_word] += 1

    return freq

def count_sentences(text):
    sentence_end = ".!?"
    count = 0

    for char in text:
        if char in sentence_end:
            count += 1

    return count

def main():
    filename = input("Enter file name: ").strip()
    text = read_file(filename)

    if text is None:
        return

    word_freq = count_word_frequency(text)
    total_words = sum(word_freq.values())
    sentence_count = count_sentences(text)

    print("File Word Counter")
    print("Total Words: ", total_words)
    print("Total Sentences: ", sentence_count)

    print("Most Common Words:")
    for word, count in word_freq.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()




