# encoding=utf-8

from basic import word_seq
from basic import word_counter
from basic import word_cloud

#
def basic_word_process():
    word_seq.word_segment()
    word_counter.word_count()
    word_cloud.create_word_cloud()


#
def main():
    basic_word_process()

#
if __name__ == '__main__':
    main()