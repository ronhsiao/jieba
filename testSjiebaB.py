#encoding=utf-8
import jieba
content = open('D:\\Shared\\Rawdata\\Raw\\B.txt', 'rb').read()
wordss = jieba.cut(content, cut_all=False)
f = open('D:\\Shared\\Rawdata\\Split\\test\\splitB.txt', 'a', encoding='UTF-8')
words = set(wordss)
for word in words:
    f.write(word)
    f.write("\n")
f.close()
