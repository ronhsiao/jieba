# encoding=utf-8
import jieba
import csv
import re

f = open('D:\\Shared\\Rawdata\\Split\\test\\RAWsplitBD.csv', 'a', encoding='UTF-8')
splitcsv = []
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('dictnew.txt')
x=5333
with open('D:\\Shared\\Rawdata\\Raw\\BD.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.DictReader(rawcsv, delimiter=',')
    for row in readCSV:
        splitpost = []
        temp = row['article']
        newstype = row['newstype']
        rr = rr = "[\s+\.\!\/_,$%^*(+\"\'\-]+|[+——！，。？、~@#￥%……&*（）「」《》?：·)．〈〉:／；◆■◇×=|°│─;“”\[\]→↓Ｎㄧˋ％\}\{\>\<’`÷‘±↑╱『˙＜≠┤‘§€↑╱★ˇ←≧┐└‧＋ˊ』＞－～\ –ㄟ＊※【】，、。．｝｛（）╴—–｜·‥…！？：；‧〔〕【】《》〈〉「」『』‘’“”☆◎▲△●○〃§※＊＆＃′‵〞〝★◇◆□■▽▼㊣ˍ﹉﹊﹍﹎﹋﹌♀∕＼／∣∥↘↙↗↖→←↓↑⊙⊕♂℅￣＿＋－×÷±√＜＞＝≦≧≠∞＄∴∵∮∫㏑㏒⊿∟∠⊥∪∩～≡≒￥〒￠￡％€℃℉㏕㎝㎜㎞㏎㎡㎎㎏㏄°▁▂▃▄▅▆▆▇█▏▎▍▌▋▊▉┼┴┴┬┤├▔─│┌▕┐└┘╩╚╣╬╠╗╦╔╡╪╞═╯╰╮╭╝╒╤╕╘╧╛╓╥╖╟╫╢╙╨╜║▓◢◣◥◤╱╲╳˙ˉˊˇˋㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄠㄟㄞㄝㄜㄛㄚㄙㄘㄗㄖㄕㄔㄓㄒㄑㄡㄢㄣㄤㄥㄦㄧㄨㄩ１＆４２３５６７８９０ｑａｚｘｓｗｅｄｃｖｆｒｔｇｂｎｈｙｕｊｍｋｉｏｌｐ︱ＱＡＺＸＳＷＥＤＣＶＦＲＴＧＢＮＨＹＵＪＭＫＩＬＯＰⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ＠︰﹪﹣]+"
        article = re.sub(rr, "", temp)
        words = jieba.cut(article, cut_all=False, HMM=True)
        # splitpost.append(article)
        splitpost.append(x)
        splitpost.append(newstype)
        x+=1
        for word in words:
            splitpost.append(word)
        splitcsv.append(splitpost)
w = csv.writer(f)
w.writerows(splitcsv)
f.close()
rawcsv.close()
