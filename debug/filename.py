import os,sys,pdb

l = []
def findFile(filename, dir='.'):
    for d in os.listdir(dir):
        subDir = os.path.join(os.path.abspath(dir), d)
        if os.path.isdir(d):
             findFile(filename, subDir)
        elif filename in d:
            l.append(subDir)

findFile('logging')
for x in l:
    print(x)
    