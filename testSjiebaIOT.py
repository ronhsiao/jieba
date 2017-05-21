# encoding=utf-8
import jieba
import csv
import re

f = open('D:\\Shared\\Rawdata\\Split\\test\\splitIOT.txt', 'a', encoding='UTF-8')
splitcsv = []
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('dictnew.txt')
with open('D:\\Shared\\Rawdata\\Raw\\IOT.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.DictReader(rawcsv, delimiter=',')
    for row in readCSV:
        splitpost = []
        temp = row['article']
        rr = "[\s+\.\!\/_,$%^*(+\"\'\-]+|[+——！，。？、~@#￥%……&*（）「」《》?：·)．〈〉:／；◆■◇×=|°│─;“”\[\]→↓Ｎㄧˋ％\}\{\>\<’`÷‘±↑╱『˙＜≠┤‘§€↑╱★ˇ←≧┐└‧＋ˊ』＞－～\ –ㄟ＊※【】，、。．｝｛（）╴—–｜·‥…！？：；‧〔〕【】《》〈〉「」『』‘’“”☆◎▲△●○〃§※＊＆＃′‵〞〝★◇◆□■▽▼㊣ˍ﹉﹊﹍﹎﹋﹌♀∕＼／∣∥↘↙↗↖→←↓↑⊙⊕♂℅￣＿＋－×÷±√＜＞＝≦≧≠∞＄∴∵∮∫㏑㏒⊿∟∠⊥∪∩～≡≒￥〒￠￡％€℃℉㏕㎝㎜㎞㏎㎡㎎㎏㏄°▁▂▃▄▅▆▆▇█▏▎▍▌▋▊▉┼┴┴┬┤├▔─│┌▕┐└┘╩╚╣╬╠╗╦╔╡╪╞═╯╰╮╭╝╒╤╕╘╧╛╓╥╖╟╫╢╙╨╜║▓◢◣◥◤╱╲╳˙ˉˊˇˋㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄠㄟㄞㄝㄜㄛㄚㄙㄘㄗㄖㄕㄔㄓㄒㄑㄡㄢㄣㄤㄥㄦㄧㄨㄩ１＆４２３５６７８９０ｑａｚｘｓｗｅｄｃｖｆｒｔｇｂｎｈｙｕｊｍｋｉｏｌｐ︱ＱＡＺＸＳＷＥＤＣＶＦＲＴＧＢＮＨＹＵＪＭＫＩＬＯＰⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ＠︰﹪﹣]+"
        article = re.sub(rr, "", temp)
        words = jieba.cut(article, cut_all=False, HMM=True)
        for word in words:
            f.write(word)
            f.write("\n")
f.close()
rawcsv.close()
