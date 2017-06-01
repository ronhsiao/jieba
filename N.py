import csv

all = []
with open('D:\\Shared\\Rawdata\\down\\newC.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        all.append(row)
rawcsv.close()
b = [["N" for m in range(6)] for n in range(32765)]
c = ["num", "type", "T", "S", "FE", "C"]
T = []
with open('D:\\Shared\\Rawdata\\down\\dict\\wordT.csv', encoding='UTF-8') as rawcsv3:
    readCSV3 = csv.reader(rawcsv3, delimiter=',')
    for row3 in readCSV3:
        T.append(row3[0])
rawcsv3.close()
S = []
with open('D:\\Shared\\Rawdata\\down\\dict\\wordS.csv', encoding='UTF-8') as rawcsv4:
    readCSV4 = csv.reader(rawcsv4, delimiter=',')
    for row4 in readCSV4:
        S.append(row4[0])
rawcsv4.close()
print()
FE = []
with open('D:\\Shared\\Rawdata\\down\\dict\\wordFE.csv', encoding='UTF-8') as rawcsv5:
    readCSV5 = csv.reader(rawcsv5, delimiter=',')
    for row5 in readCSV5:
        FE.append(row5[0])
rawcsv5.close()
C = []
with open('D:\\Shared\\Rawdata\\down\\dict\\wordC.csv', encoding='UTF-8') as rawcsv6:
    readCSV6 = csv.reader(rawcsv6, delimiter=',')
    for row6 in readCSV6:
        C.append(row6[0])
rawcsv6.close()
f = open('D:\\NdataC.csv', 'a', encoding='UTF-8')
pn = 0
for post in all:
    t = 0
    s = 0
    fe = 0
    c = 0
    for word in post:
        for tw in T:
            if word == tw:
                t += 1
                break
        for sw in S:
            if word == sw:
                s += 1
                break
        for cw in C:
            if word == cw:
                c += 1
                break
        for fw in FE:
            if word == fw:
                fe += 1
    b[pn][0] = all[pn][0]
    b[pn][1] = all[pn][1]
    b[pn][2] = t
    b[pn][3] = s
    b[pn][4] = fe
    b[pn][5] = c
    w = csv.writer(f)
    w.writerow(b[pn])
    pn += 1
