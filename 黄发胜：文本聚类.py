import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import os
import re

path=r'C:\Users\user\Desktop\文本挖掘\环境1'
files= os.listdir(path) #得到文件夹下的所有文件名称
print(files)
with open(r'C:\Users\user\Desktop\文本挖掘\zifu.txt', 'w', encoding='utf-8') as f:
    for i in range(len(files)):
        with open(path + "\\" + files[i],'r',encoding='utf-8')as fr:
            lines=fr.readline().strip('\n')
            f.write(lines)
        f.write('\n')

# jieba分词
with open(r'C:\Users\user\Desktop\文本挖掘\zifu.txt', "r", encoding='utf-8') as fr:
    lines = fr.readlines()
    jiebaword = []
    for line in lines:
        line = line.strip('\n')
        # 清除多余的空格
        line = "".join(line.split())
        # jieba.load_userdict(r'C:\Users\user\Desktop\文本挖掘\dict_file.txt')
        seg_list = jieba.cut(line, cut_all=True)
        word = "/".join(seg_list)
        print(word)
        jiebaword.append(word)
#
stopwords = []
with open(r'C:\Users\user\Desktop\文本挖掘\stopwords.txt', "r", encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        stopwords.append(line.strip())

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

fw = open(r'C:\Users\user\Desktop\文本挖掘\123.txt', 'w',encoding='utf-8')
for words in jiebaword:
    words = words.split('/')
    for word in words:
        if word not in stopwords:
# 在python中，“\t”是指制表符，代表着四个空格，也就是一个tab；它的作用是对齐表格数据的各列，可以在不使用表格的情况下，将数据上下对齐
            if is_Chinese(word):
                fw.write(word + '\t')
    fw.write('\n')
fw.close()
#
# 生成tf-idf矩阵文档
with open(r'C:\Users\user\Desktop\文本挖掘\123.txt', "r", encoding='utf-8') as fr:
    lines = fr.readlines()
tfidf = TfidfVectorizer().fit_transform(lines)
tfidf_arr = tfidf.toarray()
a=tfidf_arr
print(tfidf_arr)
print(tfidf_arr.shape)

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
K = range(2,45) # 设置主题个数区间
coef = []
for k in K:
    km = KMeans(n_clusters=k,random_state = 0).fit(a) #构建kmeans模型并训练
    score = silhouette_score(a, km.labels_,sample_size=1000) # 计算对应模型的轮廓系数
    coef.append(score)
import matplotlib.pyplot as plt
plt.plot(K,coef) # K为x轴输出，coef是y轴输出
plt.show()
#
from sklearn.cluster import KMeans
import matplotlib as plt
import numpy as np
clf = KMeans(n_clusters=22).fit(a)
y=clf.labels_.tolist()
print(y)

for i in range(50):
    file=files[i]
    print(file)
    text=open('C:/Users/user/Desktop/文本挖掘/环境1/'+file,'r',encoding='utf-8').read()
    fw = open('C:/Users/user/Desktop/文本挖掘/cluster - 副本/' + str(y[i]) + '.txt', 'a+', encoding='utf-8')
    fw.write(text)

for i in range(50):
    file=files[i]
    print(file)
    text=open('C:/Users/user/Desktop/文本挖掘/环境1/'+file,'r',encoding='utf-8').read()
    fw = open('C:/Users/user/Desktop/文本挖掘/cluster - 副本/' + str(y[i]) + '.txt', 'a+', encoding='utf-8')
    fw.write(text)
    print(y[i])
    print(i)
#
import jieba.analyse
import re
# 获取主题词
def guanjiancitiqu(position):
    txt = open(position, 'r+', encoding='utf-8').read()
    keywords=jieba.analyse.extract_tags(txt, topK=10, withWeight=False, allowPOS=())
    for keyword in keywords:
        print(keyword,end=' ')
    print()

jieba.analyse.set_stop_words(r'C:\Users\user\Desktop\文本挖掘\stopwords.txt')
for i in range(22):
    txt = open('C:/Users/user/Desktop/文本挖掘/cluster - 副本/' + str(i) + '.txt', 'r+', encoding='utf-8').read()
    keywords=jieba.analyse.extract_tags(txt, topK=10, withWeight=False, allowPOS=())
    for keyword in keywords:
        print(keyword,end=' ')
    print()
