import requests
import json
from bs4 import BeautifulSoup
import re
import os

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}

key = input('想要爬取的政策文本的关键词：')
n = input('想要爬取几页：')
if not os.path.exists(f'../file/{key}/'):
    os.makedirs(f'../file/{key}/')
# 得到搜索网页中所有政策文本网页的title和url
# 对想查询关键字进行编码成字节的格式，去掉开头的b'
keyword = str(key.encode()).replace(r'\x', '%').upper()[2:-1]
url_dict = dict()
for i in range(int(n)):
# 从network里的响应里找数据，这里的url返回的是json格式的数据
# 这里的url是XHR对象的地址
    url = f'http://sousuo.gov.cn/data?t=zhengce&q={keyword}&timetype=timeqb&mintime=&maxtime=&sort=&sortType=1&searchfield=title&pcodeJiguan=&childtype=&subchildtype=&tsbq=&pubtimeyear=&puborg=&pcodeYear=&pcodeNum=&filetype=&p={i}&n=5&inpro='
# 获取html网页，把apparent_encoding的编码格式赋值给encoding，解决乱码的问题
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    json_text = response.json()
# 得到搜索网页中所有连接地址
    dic = dict()
    for each in json_text['searchVO']['catMap']['gongwen']['listVO']:
        dic[each['url']] = each['title'].replace('<em>', '').replace('</em>', '')
    for each in json_text['searchVO']['catMap']['otherfile']['listVO']:
        dic[each['url']] = each['title'].replace('<em>', '').replace('</em>', '')
    url_dict.update(dic)

for url in url_dict:
    url_dict[url] = re.sub(r'[< > / \ | : " * ?]', ',', url_dict[url])
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    fp = open(fr'../file/{key}/{url_dict[url]}.txt', 'w', encoding='utf-8')
    #    for each in soup.find_all('p'):
    #        if each.string:
    #            fp.writelines(each.string)
    for each in soup.select('p'):
        fp.writelines(each.get_text())
    fp.close()
    print("写入成功")

def get_text(soup):
    for p in soup.select('p'):
        t = p.get_text()
        return t
