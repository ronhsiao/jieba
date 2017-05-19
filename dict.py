a = [["post1", 4, 2, 1, 3, 6, 0, 0, 0, 0], ["post2", 5, 6, 7, 0, 0, 0, 0, 0, 0], ["post3", 8, 9, 4, 6, 7, 0, 0, 0, 0]]
print(a[0])
b = [[0 for m in range(10)] for n in range(4)]
print(b)
c = ["     ", 1, 2, 3, 4, 5, 6, 7, 8, 9]
b[0] = c
end = []
i = 0
for x1 in a:
    b[i + 1][0] = a[i][0]
    i += 1

j = 0
hm = {}
for x2 in b[0]:
    hm[j] = b[0][j]
    j += 1

k = 0
yes = 1
print(b[k])
for x3 in a:
    h = 1
    for x31 in range(len(a[0]) - 2):
        yy = a[k][h]
        zz= hm[yy]
        if yy==0:
            continue
        else:
            b[k + 1][zz] = yes
        h += 1

    k += 1
    print(b[k])







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
