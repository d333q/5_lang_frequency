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
    amountwordsshow = 10
    frequencywords = Counter(words).most_common(amountwordsshow)
    return frequencywords


def print_words_count(frequencywords):
    print('10 часто используемых слов в данном тексте')
    for number in frequencywords:
        print (number)


if __name__ == '__main__':
    text = load_data(input('Введите названия файла '))
    frequencywords = get_most_frequent_words(text)
    print_words_count(frequencywords)
