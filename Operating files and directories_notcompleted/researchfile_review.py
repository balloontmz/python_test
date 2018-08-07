import os
# from the review area
# need to completed
# 有个问题，相同名字的文件无法重复搜索，如果把字典对换，相同目录下的相似文件则不可显示
def findfile(a,b,c,d):
    e=os.path.join(a,b,'.')
    f=os.listdir(e)
    for x in f:
        g=os.path.join(a, b, x)
        if os.path.isfile(g):
            if c in x:
                c2[x] = b
        else:
            e=os.path.join(b,x)
            findfile(a,e,c,d)

if __name__ == '__main__':
    a = input("请输入您要查找的文件：")
    b = os.path.abspath('.')
    c2 = {}
    findfile(b, '', a, c2)
    if len(c2) == 0:
        print("未找到您要搜索的文件！")
    else:
        print("搜索到%d个文件：\n"%len(c2))
        for x in c2.keys():
            print(c2[x],x)