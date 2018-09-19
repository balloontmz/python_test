def triangles():
    ls = [1]
    while True:
        yield ls
        ls = [1] + [ls[i] + ls[i + 1] for i in range(len(ls) - 1)] + [1]


n = 0
for x in triangles():
    print(x)
    n = n + 1
    if n == 10:
        break
else:
    print("END")  # break没用吧好象是
