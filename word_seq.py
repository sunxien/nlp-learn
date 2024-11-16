import jieba

# Python3.13.0
# jieba-0.42.1
# paddlepaddle-tiny-1.6.1
# jieba.enable_paddle()

def word_segment():
    strs = "我来到北京清华大学"

    seg_list = jieba.cut(strs, cut_all=True) # Full mode
    print("Full Mode: " + " / ".join(seg_list))

    seg_list = jieba.cut(strs, cut_all=False)   # Default is precise mode
    print("Default Mode: " + " / ".join(seg_list))

    seg_list = jieba.cut(strs, use_paddle=True)  # Paddle mode
    print("Paddle Mode: " + " / ".join(seg_list))

    seg_list = jieba.cut_for_search(strs)  # Search mode
    print("Search Mode: " + " / ".join(seg_list))