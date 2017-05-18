import csv

post = [661]
keywords = [49991]

dd = {}
with open('C:\\Users\\Tao\\Desktop\\test\\totalword.csv', 'r', encoding='UTF-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        dd[row[0]] = row[1]
cc = {}

with open('C:\\Users\\Tao\\Desktop\\test\\totalpost.csv', 'r', encoding='UTF-8') as csvfile2:
    spamreader2 = csv.reader(csvfile2, delimiter=',')
    for row2 in spamreader2:
        print(row2)
        temp = []
        x = 0
        for xxx in row2:
            temp.append(dd[str(row2[x])])
            x += 1
        temp[0]=row2[0]
        temp[1]=row2[1]
        with open('C:\\Users\\Tao\\Desktop\\test\\totalpost1.csv', 'w', encoding='UTF-8') as csvfile3:
            spamreader3 = csv.writer(csvfile3)
            spamreader3.writerows(temp)
        print("end")

