import torndb_for_python3 as torndb
#排序
def queryDatasOrderBy(column):
    rule = 'ASC'

    if column.startswith('-'):
        rule = 'DESC'
        column = column[1:]
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'select * from t_user order by %s %s'%(column,rule)
    users = conn.query(sql)
    conn.close()
    return users
# print(queryDatasOrderBy('-userid'))
#更新
def updateUserByParams(uname,userid):
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'update t_user set uname="%s" where userid="%s"'%(uname,userid)
    conn.update(sql)
    conn.close()
updateUserByParams('zhangjie',11)

#删除
def deleteUserByParams(userid):
    conn = torndb.Connection(host='127.0.0.1', database='db01', user='root', password='1234567')
    sql = 'delete from t_user where userid="%s"'%(userid)
    conn.execute(sql)
    conn.close()
deleteUserByParams(11)