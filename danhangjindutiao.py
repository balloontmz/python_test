# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import time
import sys

# 单行进度条
for i in range(10):
    for j in range(10):
        # sys.stdout.write(' '*10+'\r')  # 先用空格清屏
        sys.stdout.write('\r'+'='*j)
        time.sleep(1)