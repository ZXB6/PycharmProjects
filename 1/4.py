from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase('QODBC')
#db.setHostName('localhost')
db.setDatabaseName("sqlsv")
#db.setPort(54191)
db.setUserName("sa")
db.setPassword("123456")

# QString dsn ="Driver={sql server};server='LAPTOP-BJ3F4QK8\MSSQLSERVER2';database='Restaurant';uid=sa;pwd=pass;"
if db.open():  # 判断数据库是否打开
    print("yes")
else:
    print(db.lastError())
    print("no")