# encoding=utf-8

import jieba
import collections

def word_count(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        data = f.readlines()
        word_list = []
        for line in data:
            words = jieba.cut(line, cut_all=False)
            for word in words:
                word_list.append(word)

    counter = collections.Counter(word_list).most_common()
    print(counter)