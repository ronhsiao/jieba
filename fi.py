import csv

x = []
with open('D:\\Shared\\Rawdata\\Split\\test\\TFIDFTECH.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        x.append(row)
y = []
with open('D:\\Shared\\stopwords.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        y.append(row)
print(len(y))
print(x[0][0])
xx = 0
f = open('D:\\Shared\\Rawdata\\Split\\test\\TFIDFTECH1.csv', 'a', encoding='UTF-8')
for i in x:
    yy = 0
    a = 0
    for j in y:
        if x[xx][0] == y[yy][0]:
            continue
        else:
            a += 1
            if a== 2456:
                f.write(word[j] + "," + str(weight[i][j]) + "\n")
    xx += 1
