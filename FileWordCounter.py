import string
from collections import Counter

from gensim.parsing.preprocessing import STOPWORDS

STOPWORDS = set(STOPWORDS)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return None

def count_word_frequency(text):
    words = text.split()
    freq = Counter()

    for word in words:

