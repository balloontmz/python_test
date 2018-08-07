import os
# os.path.splitext(PATH)返回的是一个truple
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']