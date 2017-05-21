import csv

with open('D:\\Shared\\Rawdata\\Split\\Clean\\unix\\postsplittotal.csv', encoding='UTF-8') as rawcsv:
    readCSV = csv.reader(rawcsv, delimiter=',')
    for row in readCSV:
        print(len(row))
rawcsv.close()