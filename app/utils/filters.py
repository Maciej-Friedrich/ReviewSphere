import re
import os

# Wczytaj wulgarne słowa z pliku
file_path = os.path.join(os.path.dirname(__file__), 'banned_words_pl.txt')
with open(file_path, encoding='utf-8') as f:
    BANNED_WORDS = [line.strip() for line in f if line.strip()]

def clean_text(text):
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, BANNED_WORDS)) + r')\b', re.IGNORECASE)
    return pattern.sub('[cenzura]', text)
