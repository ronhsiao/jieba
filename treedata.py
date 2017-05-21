import csv

x=1
f = open('D:\\Shared\\Rawdata\\Split\\Clean\\unix\\numsplittotal.csv', 'a', encoding='UTF-8')
end=[]
with open('D:\\Shared\\Rawdata\\Split\\Clean\\unix\\postsplittotal.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        row[0]=x
        x+=1
        end.append(row)
w = csv.writer(f)
w.writerows(end)
rawcsv.close()
f.close()