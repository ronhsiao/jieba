# encoding=utf-8
import jieba

content = open('D:\\Shared\\Rawdata\\Raw\\S.txt', 'rb').read()
print("1")
words = jieba.cut(content, cut_all=False)
print("2")
f = open('D:\\Shared\\Rawdata\\Split\\test\\splitS.txt', 'a', encoding='UTF-8')
print("3")
print(type(words))
# words = set(wordss)
print("4")
x = 0
for word in words:
    f.write(word)
    f.write("\n")
    x += 1
    print("value" + str(x))
f.close()
