# encoding=utf-8
import jieba
import csv
import re

f = open('D:\\Shared\\Rawdata\\Split\\test\\TsplitS.txt', 'a', encoding='UTF-8')
splitcsv = []
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('dictnew.txt')
with open('D:\\Shared\\Rawdata\\Raw\\S.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.DictReader(rawcsv, delimiter=',')
    x = 1
    for row in readCSV:
        splitpost = []
        temp = row['article']
        newstype = row['newstype']
        rr = rr = "[\s+\.\!\/_,$%^*(+\"\'\-]+|[+——！，。？、~@#￥%……&*（）「」《》?：·)．〈〉:／；◆■◇×=|°│─;“”\[\]→↓Ｎㄧˋ％\}\{\>\<’`÷‘±↑╱『˙＜≠┤‘§€↑╱★ˇ←≧┐└‧＋ˊ』＞－～\ –ㄟ＊※【】，、。．｝｛（）╴—–｜·‥…！？：；‧〔〕【】《》〈〉「」『』‘’“”☆◎▲△●○〃§※＊＆＃′‵〞〝★◇◆□■▽▼㊣ˍ﹉﹊﹍﹎﹋﹌♀∕＼／∣∥↘↙↗↖→←↓↑⊙⊕♂℅￣＿＋－×÷±√＜＞＝≦≧≠∞＄∴∵∮∫㏑㏒⊿∟∠⊥∪∩～≡≒￥〒￠￡％€℃℉㏕㎝㎜㎞㏎㎡㎎㎏㏄°▁▂▃▄▅▆▆▇█▏▎▍▌▋▊▉┼┴┴┬┤├▔─│┌▕┐└┘╩╚╣╬╠╗╦╔╡╪╞═╯╰╮╭╝╒╤╕╘╧╛╓╥╖╟╫╢╙╨╜║▓◢◣◥◤╱╲╳˙ˉˊˇˋㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄠㄟㄞㄝㄜㄛㄚㄙㄘㄗㄖㄕㄔㄓㄒㄑㄡㄢㄣㄤㄥㄦㄧㄨㄩ１＆４２３５６７８９０ｑａｚｘｓｗｅｄｃｖｆｒｔｇｂｎｈｙｕｊｍｋｉｏｌｐ︱ＱＡＺＸＳＷＥＤＣＶＦＲＴＧＢＮＨＹＵＪＭＫＩＬＯＰⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ＠︰﹪﹣]+"
        article = re.sub(rr, "", temp)
        words = jieba.cut(article, cut_all=False, HMM=True)
        # splitpost.append(article)
        # splitpost.append(x)
        # splitpost.append(newstype)
        # x += 1
        splitAI = ""
        for word in words:
            splitAI = splitAI + word + " "
        f.write(splitAI)
f.close()
rawcsv.close()
