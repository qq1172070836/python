#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# author: xin lan 2017/8/21

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba
import os
from PIL import Image
import numpy as np

def word_cloud(text=None, img_path=None):
    if img_path:
        abel_mask = np.array(Image.open(img_path))
    else:
        abel_mask = np.array(Image.open("2.jpg"))

    text_from_file_with_apath = text
    # with open(u'凡人修仙传.txt', 'r') as f:
    #     text_from_file_with_apath = f.read()
    # jieba.add_word("加词")
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)

    font = os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
    my_wordcloud = WordCloud(font_path=font,  # 字库
                             background_color="white",  # 背景颜色
                             mask=abel_mask,  # 设置背景图
                             # stopwords=STOPWORDS | {"我们", "他们", "自己"},
                             # max_font_size=40,  #字体最大值
                             ).generate(wl_space_split)

    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(abel_mask)

    # 以下代码显示图片
    plt.imshow(my_wordcloud)
    plt.axis("off")
    # 绘制词云
    plt.figure()
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    plt.imshow(abel_mask, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()
    # 保存图片
    my_wordcloud.to_file(u"wordcloud名称.png")


