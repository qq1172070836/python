# pip install opencv-python(cv2)

from wordcloud import WordCloud
import jieba
import cv2

f = open('test.txt', 'r', encoding='UTF-8').read()
txt = jieba.cut(f, cut_all=True)
wl = ' '.join(txt)
mk = cv2.imread('test.psd')
wd = WordCloud(mask=mk, background_color='white', font_path='msyhbd.ttf', width=500, height=365, margin=2).generate(wl)
wd.to_file('000.jpg')