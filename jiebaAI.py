#encoding=utf-8
import jieba
import jieba.analyse
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('dictnew.txt')

content = open('D://TestAI.txt', 'rb').read()
jieba.analyse.set_stop_words('D:\\words\\stopwords.txt')

tags = jieba.analyse.extract_tags(content, 500)
f = open('D:\\words\\AI.txt', 'a', encoding='UTF-8')
f.write(",".join(tags))