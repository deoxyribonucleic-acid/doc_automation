import pymysql

try:
    # 连接到MySQL数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234567', db='db01')
except pymysql.err.OperationalError as e:
    if e.args[0] == 1049:  # 数据库不存在
        print("数据库不存在")
    else:
        raise e