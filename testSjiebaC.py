#encoding=utf-8
import jieba
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('dictnew.txt')
content = open('D:\\Shared\\Rawdata\\Raw\\C.txt', 'rb').read()
words = jieba.cut(content, cut_all=False, HMM=True)
f = open('D:\\Shared\\Rawdata\\Split\\test\\splitC.txt', 'a', encoding='UTF-8')
# words = set(wordss)
for word in words:
    f.write(word)
    f.write("\n")
f.close()
