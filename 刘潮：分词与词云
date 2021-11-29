# -*- coding: utf-8 -*-
import jieba
import wordcloud
import re

txt = open('result.txt', 'r+', encoding='utf-8').read()
txt = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*()]+", "", txt)
words = jieba.lcut(txt)
#print(words)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print('{0:<5}{1:>10}'.format(word, count))
#print(items)
ls = []
for i in range(100):
    a = items[i][0]
    ls.append(a)
#print(ls)
w = wordcloud.WordCloud(width=1000, height=1000, background_color='white', font_path='C:\\Windows\\Fonts\\微软雅黑\\msyh.ttc')
w.generate(' '.join(ls))
w.to_file('1.png')
