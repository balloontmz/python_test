# -*- coding: utf-8 -*-

# 来自评论区，关于dir -l的内部逻辑，未定义外部接口

# 引入datetime的实现方式
import os
import datetime
import time
print( "%-20s%-5s%-8s%s" % ('时间','类型','大小','名字',) )
for item in os.listdir( "." ):
    finalmodifytime = datetime.datetime.strftime( datetime.datetime.fromtimestamp( os.path.getmtime( item ) ), "%Y/%m/%d %H:%M" )
    type = "<DIR>" if os.path.isdir( item ) else ""
    size = os.path.getsize( item )
    name = item
    print( "%-20s%-8s%-8s%s" % ( finalmodifytime, type, size, name ) )

# 引入time模块的实现方式import os
# import os
# import time

# for item in os.listdir( "." ):
    # finalmodifytime = time.strftime( "%Y/%m/%d %H:M", time.localtime( os.path.getmtime( item ) ) )
    # type = "<DIR>" if os.path.isdir( item ) else ""
    # size = os.path.getsize( item )
    # name = item
    # print( "%-20s%-8s%-8s%s" % ( finalmodifytime, type, size, name ) )

# time与datetime类上同样有格式化时间的方法strftime，但用法却不同