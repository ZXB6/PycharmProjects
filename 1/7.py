from PyQt5 import QtSql

db = QtSql.QSqlDatabase('QODBC')
db.setHostName('localhost')
db.setPort(54191)
db.setDatabaseName('LAPTOP-BJ3F4QK8\MSSQLSERVER2')
db.setUserName("sa")
db.setPassword("123456")
            # db = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',
            #                      password='123456',
            #                      database='Restaurant', charset='GBK')
print(QtSql.QSqlDatabase.drivers())
if db.open():  # 判断数据库是否打开
                print("456")
                print(db.lastError().text())  # 打印操作数据库时出现的错误
                print("4")
                #return False
else:
    print(db.lastError().text())
    print("连接失败")