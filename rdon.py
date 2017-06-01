import csv
import random

all = []
with open('D:\\Shared\\Rawdata\\Split\\Clean\\num\\numsplitC.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        all.append(row)
rawcsv.close()



rdn = []
nrdn = set(rdn)
while True:
    if len(nrdn) == 32764:
        break
    else:
        nrdn.add(random.randint(0, 121226))

rdn=list(nrdn)


f = open('D:\\Shared\\Rawdata\\Split\\test\\downC.csv', 'a', encoding='UTF-8')
end=[]
for x in rdn:
    end.append(all[x])
w = csv.writer(f)
print("end1")
w.writerows(end)
print("end2")
f.close()
print("end3")
