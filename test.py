import csv

# a = [["post1", 4, 2, 1, 3, 6, 0, 0, 0, 0], ["post2", 5, 6, 7, 0, 0, 0, 0, 0, 0], ["post3", 8, 9, 4, 6, 7, 0, 0, 0, 0]]
all = []
with open('D:\\Shared\\224\\AI.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        all.append(row)
with open('D:\\Shared\\224\\IOT.csv', encoding='UTF-8') as rawcsv2:
    readCSV2 = csv.reader(rawcsv2, delimiter=',')
    for row2 in readCSV2:
        all.append(row2)
# eee= 0   #看內容
# for www in all:
#     print(all[eee])
#     eee+=1

b = [[0 for m in range(604)] for n in range(51)]
c = ["num", "type"]
with open('D:\\Shared\\224\\test.csv', encoding='UTF-8') as rawcsv3:
    readCSV3 = csv.reader(rawcsv3, delimiter=',')
    for row3 in readCSV3:
        c.append(row3[0])
# oo = 1
# for tt in range(1, 602):
#     c.append(oo)
#     oo += 1
b[0] = c
#
i = 0
for x1 in all:
    b[i + 1][0] = all[i][0]
    b[i + 1][1] = all[i][1]
    i += 1
j = 0
hm = {}
for x2 in b[0]:
    hm[j] = b[0][j]
    j += 1
k = 0
yes = 1
for x3 in all:
    h = 2
    for x31 in range(len(all[0]) - 3):
        yy = all[k][h]
        for yy in c :
            mm=0
            if yy!=[mm]:
                mm+=1
                continue
            else:
                zz = hm[yy]
                b[k + 1][zz] = yes
                h += 1
        print(b[k])
        k += 1
















# x = 0
# y = 0
# z = 1
# q = 0
# for asd in a:
#     xxx = [9]
#     for qwe in range(1, 10):
#         if a[x][q] == z:
#             xxx[y] = 1
#             print(a[x][z])
#             print("T" + str(z))
#             z += 1
#             q += 1
#         else:
#             xxx[y] = 0
#             print(a[x][q])
#             print("F" + str(z))
#             z += 1
#             q += 1
#     x += 1
#     y += 1
#     end.append(xxx)
# print(end)
