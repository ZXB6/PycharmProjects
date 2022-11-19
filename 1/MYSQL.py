import numpy as np
import pandas as pd
import pymssql
#连接数据库
from PyQt5.QtGui import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from pythonProject.MYSQL.代码 import myform

conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa', password='123456',
                           database='Restaurant',charset='GBK')
cur = conn.cursor() # 生成游标对象
sql="select * from worke" # SQL语句
cur.execute(sql) # 执行SQL语句
data = cur.fetchall() # 通过fetchall方法获得数据
row=data.rowcount #取得记录个数，用于设置表格的行数
vol=len(row[0]) #取得字段数，用于设置表格的列数
print(data)
cur.close() # 关闭游标
conn.close() # 关闭连接
self.table.setRowCount(row)
self.table.setColumnCount(vol)
for i in range(row):
    for j in range(vol):
        temp_data=row[i][j] #临时记录，不能直接插入表格
        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
        self.table.setItem(i,j,data)
app=QApplication(sys.argv)

w=myform()

app.exec_()
cur.execute(sql)  # 执行SQL语句
        rows = cur.fetchall()  # 通过fetchall方法获得数据
        row = cur.rowcount  # 取得记录个数，用于设置表格的行数
        vol = len(rows[0])  # 取得字段数，用于设置表格的列数
        # print(data)
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        self.table.setRowCount(row)
        self.table.setColumnCount(vol)
        for i in range(row):
            for j in range(vol):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.table.setItem(i, j, data)
                self.table.setItem
        app = QApplication(sys.argv)

        w = myform()

        app.exec_()