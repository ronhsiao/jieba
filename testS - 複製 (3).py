import csv

f = open('D:\\Shared\\Rawdata\\Split\\test\\treedataFE.csv', 'a', encoding='UTF-8')
all = []
with open('D:\\Shared\\Rawdata\\Split\\Clean\\num\\numsplitFE.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        all.append(row)
rawcsv.close()
print("alllen=" + str(len(all)))

b = [["N" for m in range(1231)] for n in range(119049)]

c = ["num", "type"]
with open('D:\\Shared\\Rawdata\\Split\\tree\\newtree.csv', encoding='UTF-8') as rawcsv3:
    readCSV3 = csv.reader(rawcsv3, delimiter=',')
    for row3 in readCSV3:
        c.append(row3[0])
rawcsv3.close()
b[0] = c

i = 0
for x1 in all:
    b[i + 1][0] = all[i][0]
    b[i + 1][1] = all[i][1]
    i += 1
print('case down')

j = 0
hm = {}
for x2 in b[0]:
    hm[b[0][j]] = j
    j += 1
print('keyvalue down')
yes = "Y"
k = 0
end = []
end.append(b[0])

for x3 in range(len(all)):
    h = 2
    for x31 in range(len(all[k]) - 2):
        mm = 2
        for x32 in range(len(c) - 2):
            yy = all[k][h]
            if yy != c[mm]:
                mm += 1
            else:
                zz = hm[yy]
                b[k + 1][zz] = yes
                mm += 1
        h += 1
    # print(b[k + 1])
    end.append(b[k + 1])
    k += 1
w = csv.writer(f)
print("end1")
w.writerows(end)
print("end2")
f.close()
print("end3")
