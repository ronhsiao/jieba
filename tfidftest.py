import jieba.analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import csv

""" TF-IDF权重： 1、CountVectorizer 构建词频矩阵 2、TfidfTransformer 构建tfidf权值计算 3、文本的关键字 4、对应的tfidf矩阵 """

# # 读取文件
# def read_news():
#     news = open('news.txt').read()
#     return news


# # jieba分词器通过词频获取关键词
# def jieba_keywords(news):
#     keywords = jieba.analyse.extract_tags(news, topK=10)
#     print keywords

# def tfidf_keywords():
#     # 00、读取文件,一行就是一个文档，将所有文档输出到一个list中
#     corpus = []
#     for line in open('D:\\Shared\\Rawdata\\Split\\test\\TsplitAI.txt', 'r',encoding="UTF-8").readlines():
#         corpus.append(line)
#
#     # 01、构建词频矩阵，将文本中的词语转换成词频矩阵
#     vectorizer = CountVectorizer()
#     # a[i][j]:表示j词在第i个文本中的词频
#     X = vectorizer.fit_transform(corpus)
#     print(X)  # 词频矩阵
#
#     # 02、构建TFIDF权值
#     transformer = TfidfTransformer()
#     # 计算tfidf值
#     tfidf = transformer.fit_transform(X)
#
#     # 03、获取词袋模型中的关键词
#     word = vectorizer.get_feature_names()
#
#     # tfidf矩阵
#     weight = tfidf.toarray()
#
#     # 打印特征文本
#     print(len(word))
#     for j in range(len(word)):
#         print(word[j])
#
#     # 打印权重
#     for i in range(len(weight)):
#         for j in range(len(word)):
#             print(weight[i][j])
#             # print '\n'
#
#
# if __name__ == '__main__':
#     # news = read_news()
#     # jieba_keywords(news)
#     tfidf_keywords()

corpus = []
for line in open('D:\\Shared\\Rawdata\\Split\\test\\splitS.txt', 'r', encoding="UTF-8").readlines():
    corpus.append(line)
# print(len(corpus[0]))

# #将文本中的词语转换为词频矩阵
# vectorizer = CountVectorizer()
# #计算个词语出现的次数
# X = vectorizer.fit_transform(corpus)
# #获取词袋中所有文本关键词
# word = vectorizer.get_feature_names()
# print(word)
# #查看词频结果
# X.toarray()
# print(X)

vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
word = vectorizer.get_feature_names()  # 所有文本的关键字
weight = tfidf.toarray()  # 对应的tfidf矩阵
f = open('D:\\Shared\\Rawdata\\Split\\test\\TFIDFS.csv', 'a', encoding='UTF-8')
x = []
with open('D:\Shared\\stopwords.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        x.append(row)
# print(x[944][0])
# print(word[115390])

for i in range(len(weight)):
    for j in range(len(word)):
        if weight[i][j] == 0.0:
            continue
        else:
            a = 0
            q = 0
            for y in x:
                if word[j] == x[q][0]:
                    continue
                else:
                    a += 1
                q += 1
            if a == 2456:
                f.write(word[j] + "," + str(weight[i][j]) + "\n")
