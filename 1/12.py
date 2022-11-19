import pyodbc

import sys

conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=.;DATABASE=ST;UID=sa;PWD=123456')

cursor = conn.cursor()

cursor.execute("select IDCard, Name from T_UserInfo")

row = cursor.fetchone()

if row:
    print(row)