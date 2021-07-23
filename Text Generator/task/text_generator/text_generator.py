# Write your code here
import random

import nltk as nltk
from collections import Counter
from nltk.tokenize import WhitespaceTokenizer


def load_text(file_name_):
    with open(file_name_, encoding="utf-8") as file_:
        return file_.read()


def find_word(dict_):
    freq_counter_ = Counter(dict_)
    list_freq_ = freq_counter_.most_common()
    words_ = [x[0] for x in list_freq_]
    weights_ = [x[1] for x in list_freq_]
    if len(words_) == 0:
        return ""
    return random.choices(words_, weights_)[0]


def sentence_generator():
    global trigrams_dict
    sentence_ = []
    first_word = True
    while True:
        if first_word:
            word_ = random.choice(list(trigrams_dict.keys()))
            if word_ == "":
                continue
            if word_[0].isupper() and word_.split()[0][-1] not in ['.', '!', '?']:
                sentence_.append(word_.split()[0])
                sentence_.append(word_.split()[1])
                first_word = False
        else:
            next_ = sentence_[-2] + " " + sentence_[-1]
            word_ = find_word(trigrams_dict[next_])
            if word_ == "":
                continue
            if word_[-1] in ['.', '!', '?'] and len(sentence_) >= 4:
                sentence_.append(word_)
                break
            elif word_[-1] in ['.', '!', '?']:
                sentence_ = []
                first_word = True
            elif word_ != "":
                sentence_.append(word_)
            else:
                continue
    return sentence_


text = load_text(input())
wst = WhitespaceTokenizer()
tokens = wst.tokenize(text)
trigrams = list(nltk.trigrams(tokens))

trigrams_dict = {}
for a, b, c in nltk.trigrams(tokens):
    trigrams_dict.setdefault(a + " " + b, []).append(c)
for x in range(10):
    sentence = sentence_generator()
    print(" ".join(sentence))
    x += 1
