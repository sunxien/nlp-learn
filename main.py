# encoding=utf-8

import word_seq
import word_counter
import word_cloud

word_count_file = "./dataset/test.txt";

def main():
    # word_seq.word_segment()
    # word_counter.word_count(word_count_file)
    word_cloud.create_word_cloud()



if __name__ == '__main__':
    main()