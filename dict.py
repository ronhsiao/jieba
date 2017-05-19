a = [["post1", 1, 2, 3, 4, 0, 0, 0, 0, 0], ["post2", 5, 6, 7, 0, 0, 0, 0, 0, 0], ["post3", 8, 9, 4, 6, 7, 0, 0, 0, 0]]
end = []
x = 0
y = 0
z = 1
q = 0
for asd in a:
    xxx = [9]
    for qwe in range(1, 10):
        if a[x][q] == z:
            xxx[y] = 1
            print(a[x][z])
            print("T" + str(z))
            z += 1
            q += 1
        else:
            xxx[y] = 0
            print(a[x][q])
            print("F" + str(z))
            z += 1
            q += 1
    x += 1
    y += 1
    end.append(xxx)
print(end)
