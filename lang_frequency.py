import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as text:
        return text.read()


def get_most_frequent_words(text):
    words = re.findall('\w+', text)
    return Counter(words).most_common(10)


if __name__ == '__main__':
    text = load_data(input('Введите названия файла '))
    print ('''10 самых встречаемых слов в данном тексте
{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}'''.format(
        *get_most_frequent_words(text)))
