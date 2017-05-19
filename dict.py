import numpy

a = [["post1", 4, 2, 1, 3, 6, 0, 0, 0, 0], ["post2", 5, 6, 7, 0, 0, 0, 0, 0, 0], ["post3", 8, 9, 4, 6, 7, 0, 0, 0, 0]]
b = [[0 for m in range(10)] for n in range(4)]
# a = numpy.array([["post1", 1, 2, 3, 4, 0, 0, 0, 0, 0], ["post2", 5, 6, 7, 0, 0, 0, 0, 0, 0], ["post3", 8, 9, 4, 6, 7, 0, 0, 0, 0]])
# b = numpy.zeros((3, 10), int)
c = ["     ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
b[0] = c
end = []
# print(b)
i = 0
for x1 in a:
    b[i + 1][0] = a[i][0]
    i += 1
# print(b)

j = 0
hm = {}
for x2 in b[0]:
    hm[j] = b[0][j]
    j += 1
# print(hm)
k = 0
yes = 1
no = 0
for x3 in a:
    h = 1
    for x31 in range(len(a[0]) - 2):
        yy = a[k][h]
        zz= hm[yy]
        if yy==0:
            b[k + 1][yy] = no
        else:
            b[k + 1][zz] = yes
        print("b[" + str(k + 1) + "]" + " " + "a[" + str(k) + "][" + str(h) + "]")
        h += 1
        print(b)
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
