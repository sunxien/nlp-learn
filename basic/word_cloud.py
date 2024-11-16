# encoding=utf-8

import jieba
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud

# create stop word list
def read_stop_word_list(file_path):
    stop_word_list = [line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()]
    return stop_word_list


#
STOP_WORD_FILE = "./dataset/stopwords.txt"
LIGHTNING_FILE = "./dataset/lightning.txt"
MASK_IMAGE_FILE = "./resource/mask.jpg"
LOCAL_FONT_PATH = "./resource/simsun.ttf"

# segment sentence
def segment_sentence(sentence):
    sentence_segment = jieba.cut(sentence.strip(), cut_all=False)
    stop_word_list = read_stop_word_list(STOP_WORD_FILE)
    out_string = ''
    for word in sentence_segment:
        if word not in stop_word_list:
            if word != '\t':
                out_string += word
                out_string += " "
    return out_string


# read original data file
def read_file(file_path):
    lines = open(file_path, 'r', encoding='utf-8')
    word_list = []
    for line in lines:
        line_segment = segment_sentence(line)
        word_list.append(line_segment + '\n')

    lines.close()
    return "".join(word_list)


def create_word_cloud():
    word_strings = read_file(LIGHTNING_FILE)
    mask_image = np.array(Image.open(MASK_IMAGE_FILE))
    word_cloud = WordCloud(background_color="white",
                           max_words=1000, width=2000, height=1600, margin=2,
                           font_path=LOCAL_FONT_PATH,
                           mask=mask_image).generate(word_strings)

    plt.imshow(word_cloud)
    plt.savefig("./target/word_cloud.png")
    plt.axis("off")