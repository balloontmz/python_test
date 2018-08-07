from command import MyObject

computer=MyObject()
def run(x):
    inp = input('method>')
    # 判断是否有这个属性
    if hasattr(computer,inp):
    # 有就获取然后赋值给新的变量
        func = getattr(computer,inp)
        print(func())
    else:
    # 没有我们来set一个
        setattr(computer,inp,lambda x:x+1)
        func = getattr(computer,inp)
        print(func(x))


if __name__=='__main__':
    run(10)
