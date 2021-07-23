# Write your code here
import random

import nltk as nltk
from collections import Counter
from nltk.tokenize import WhitespaceTokenizer


def load_text(file_name_):
    with open(file_name_, encoding="utf-8") as file_:
        return file_.read()


def sentence_generator(word_):
    word_ = word_.strip()
    global trigrams_dict
    sent_ = []
    first_word = True
    counter_ = 0
    is_ok = False
    while True:
        if is_ok:
            break
        freq_counter_ = Counter(trigrams_dict[word_])
        list_freq_ = freq_counter_.most_common()
        words_ = [x[0] for x in list_freq_]
        weights_ = [x[1] for x in list_freq_]
        if first_word:
            while True:
                # next_word_ = random.choices(words_, weights=weights_, k=1)
                next_word_ = words_[0]
                if next_word_[0].isupper() and next_word_[-1].isalpha():
                    first_word = False
                    break
                del words_[0]
                # del weights_[0]
        # elif counter_ >= 4:
        elif counter_ >= 4:
            # next_word_ = random.choices(words_, weights=weights_, k=1)
            next_word_ = words_[0]
            if next_word_[-1] in [".", "?", "!"]:
            # if next_word_[0][-1] in [".", "?", "!"]:
                is_ok = True
        else:
            # next_word_ = random.choices(words_, weights=weights_, k=1)
            next_word_ = words_[0]
        # sent_.append(next_word_[0])
        sent_.append(next_word_)
        # word_ = next_word_[0]
        word_ = word_.split()[1] + " " + next_word_
        counter_ += 1
    return sent_


text = load_text(input())
wst = WhitespaceTokenizer()
tokens = wst.tokenize(text)
trigrams = list(nltk.trigrams(tokens))

trigrams_dict = {}
for a, b, c in nltk.trigrams(tokens):
    trigrams_dict.setdefault(a + " " + b, []).append(c)

start_word = random.choice(list(trigrams_dict.items()))

start_word = start_word[0].split()[1] + " " + start_word[1][0]
# print(start_word)
# print(trigrams_dict.get(start_word))
# freq_counter_ = Counter(trigrams_dict[start_word])
# print(freq_counter_)
for x in range(10):
    sentence = sentence_generator(start_word)
    print(" ".join(sentence))
    x += 1
    start_word = sentence[-2] + " " + sentence[-1]
