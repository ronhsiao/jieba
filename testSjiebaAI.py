# encoding=utf-8
import jieba
import csv
import re

f = open('D:\\AI.txt', 'a', encoding='UTF-8')
g=open('D:\\nnews.txt', encoding='UTF-8')
lines = g.readlines()
for line in lines:
    temp = line
        # splitpost = []
        # temp = row['article']
    rr = "[\s+\.\!\/_,$%^*(+\"\'\-]+|[+——！，。？、~@#￥%……&*（）「」《》?：·)．〈〉:／；◆■◇×=|°│─;“”\[\]→↓Ｎㄧˋ％\}\{\>\<’`÷‘±↑╱『˙＜≠┤‘§€↑╱★ˇ←≧┐└‧＋ˊ』＞－～\ –ㄟ＊※【】，、。．｝｛（）╴—–｜·‥…！？：；‧〔〕【】《》〈〉「」『』‘’“”☆◎▲△●○〃§※＊＆＃′‵〞〝★◇◆□■▽▼㊣ˍ﹉﹊﹍﹎﹋﹌♀∕＼／∣∥↘↙↗↖→←↓↑⊙⊕♂℅￣＿＋－×÷±√＜＞＝≦≧≠∞＄∴∵∮∫㏑㏒⊿∟∠⊥∪∩～≡≒￥〒￠￡％€℃℉㏕㎝㎜㎞㏎㎡㎎㎏㏄°▁▂▃▄▅▆▆▇█▏▎▍▌▋▊▉┼┴┴┬┤├▔─│┌▕┐└┘╩╚╣╬╠╗╦╔╡╪╞═╯╰╮╭╝╒╤╕╘╧╛╓╥╖╟╫╢╙╨╜║▓◢◣◥◤╱╲╳˙ˉˊˇˋㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄠㄟㄞㄝㄜㄛㄚㄙㄘㄗㄖㄕㄔㄓㄒㄑㄡㄢㄣㄤㄥㄦㄧㄨㄩ１＆４２３５６７８９０ｑａｚｘｓｗｅｄｃｖｆｒｔｇｂｎｈｙｕｊｍｋｉｏｌｐ︱ＱＡＺＸＳＷＥＤＣＶＦＲＴＧＢＮＨＹＵＪＭＫＩＬＯＰⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ＠︰﹪﹣]+"
    article = re.sub(rr, "", temp)
    fil=re.search(r'人工智慧',article)
    #         words = jieba.cut(article, cut_all=False, HMM=True)
#         for word in words:
#             f.write(word)
#             f.write("\n")
    if fil == None:
        continue
    else:
        f.write(article+"\n")

g.close()
f.close()
# rawcsv.close()
