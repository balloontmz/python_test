import os,sys,pdb

l = []
def findFile(filename, dir=os.path.abspath('.')):
    for d in os.listdir(dir):
        subDir = os.path.join(dir, d)

        if os.path.isdir(subDir): # 此处应使用绝对路径 ！！！
            findFile(filename, subDir)
        elif filename in d:
            l.append(subDir)





if __name__ == '__main__':
    a = input('请输入需要检索的文件：')
    findFile(a)
    for x in l:
        print(x)