
def creatCounter():
    i=0
    def counter():
        nonlocal i
        i+=1
        return i
    return counter




counterA = creatCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = creatCounter()
print(counterB())