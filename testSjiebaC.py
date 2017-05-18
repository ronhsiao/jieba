#encoding=utf-8
import jieba
content = open('D:\\Shared\\Rawdata\\Raw\\C.txt', 'rb').read()
words = jieba.cut(content, cut_all=False)
f = open('D:\\Shared\\Rawdata\\Split\\test\\splitC.txt', 'a', encoding='UTF-8')
# words = set(wordss)
for word in words:
    f.write(word)
    f.write("\n")
f.close()
