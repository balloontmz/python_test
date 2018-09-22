#!usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module'

_author_='tomtiddler'

import sys

def test():
    argv=sys.argv
    if len(argv)==1:
        print('hello,world')
    elif len(argv)==2:
        print('hello,%s.'%argv[1])
    else:
        print('too many ')

if __name__=='__main__':
    test()


