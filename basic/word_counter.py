# encoding=utf-8

import jieba
import collections

WORD_COUNT_FILE = "./dataset/test.txt";

def word_count():
    with open(WORD_COUNT_FILE, "r", encoding='utf-8') as f:
        data = f.readlines()
        word_list = []
        for line in data:
            words = jieba.cut(line, cut_all=False)
            for word in words:
                word_list.append(word)

    counter = collections.Counter(word_list).most_common()
    print(counter)