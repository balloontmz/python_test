import pymysql

# 建立数据库连接
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='test',
    passwd='123456',
    db='bigsdut',
    charset='utf8'
)

