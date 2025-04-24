import os

file_path = os.path.join(os.path.dirname(__file__), 'banned_words_pl.txt')
with open(file_path, encoding='utf-8') as f:
    BANNED_WORDS = set(word.strip().lower() for word in f.readlines())

def clean_text(text):
    words = text.split()
    filtered = [
        '***' if word.lower().strip('.,!?') in BANNED_WORDS else word
        for word in words
    ]
    return ' '.join(filtered)
def count_profanities(text):
    with open(file_path, encoding='utf-8') as f:
        banned_words = [line.strip().lower() for line in f.readlines()]
    return sum(word in text.lower() for word in banned_words)
