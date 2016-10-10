import os
import re
from collections import Counter
import string


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as text:
        return text.read()


def get_most_frequent_words(text):
    lowercase = text.lower()
    words = re.findall('\w+', lowercase)
    amount_words = 10
    frequency_words = Counter(words).most_common(amount_words)
    return frequency_words


if __name__ == '__main__':
    text = load_data(input('Введите названия файла '))
    print(get_most_frequent_words(text))
