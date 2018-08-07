class Myobject(object):
    def __init__(self):
        self.__x = 9
        self.__y = 9

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def add(self, x, y):
        return self.__x + self.__y

    def sub(self, x, y):
        return self.__x - self.__y


computer = Myobject()


def run(x, y):
    computer.set_x(x)
    computer.set_y(y)
    inp = input('计算方法')
    if hasattr(computer, inp):
        func = getattr(computer, inp)
    else:
        setattr(computer, inp, lambda x, y: x * y)
        func = getattr(computer, inp)
    print(func(x,y))


if __name__ == '__main__':
    m = int(input('x'))
    n = int(input('y'))
    run(m, n)
