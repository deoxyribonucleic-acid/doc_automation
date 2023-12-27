import torndb_for_python3 as torndb
#插入单个
def insertData(uname,pwd):
    conn = torndb.Connection(host='localhost', database='db01', user='root', password='1234567')
    conn.insert('insert into t_administrator values(null,"%s","%s")'%(uname,pwd))
    conn.close()

insertData('2020211023021','123')
#插入多个
def insertDatas(args=[]):
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'insert into t_administrator values(null,%s,%s,now())'
    conn.insertmany(sql,args)
    conn.close()

# insertDatas([('zhangsan',123), ('lisi',1234)])
#查询
def queryDatas():
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'select * from t_user'
    users = conn.query(sql)
    conn.close()
    return users
#条件查询
def queryDataByParams(uname,pwd):
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'select * from t_user where uname="%s" and pwd="%s"'%(uname,pwd)
    users = conn.query(sql)
    conn.close()
    return users

# print(queryDataByParams('zhangsan','123'))
#模糊查询
def queryDatasByLike(uname):
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'select * from t_user where uname like "%%{ua}"'.format(ua=uname)
    users = conn.query(sql)
    conn.close()
    return users
# print(queryDatasByLike('u'))