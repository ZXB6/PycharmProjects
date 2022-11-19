import tkinter as tk
import pyodbc

root = tk.Tk()
root.title('餐厅管理系统')
root.geometry('450x300')

canvas = tk.Canvas(root, height=200, width=500)
canvas.pack(side='top')

tk.Label(root, text='用户名: ').place(x=50, y= 150)
tk.Label(root, text='密码  : ').place(x=50, y= 190)

name = tk.StringVar()
name.set(' ')
uname = tk.Entry(root, textvariable=name)
uname.place(x=160, y=150)
upwd = tk.StringVar()
upwd = tk.Entry(root, textvariable=upwd, show='*')
upwd.place(x=160, y=190)

def usrlogin():
    conn=pyodbc.connect(r'DRIVER={SQL Server Native};SERVER=;DATABASE=ST;UID=sa;PWD=123456789')
    c1=conn.cursor()
    c1.execute("select * from *")
    results=c1.fetchall()
    for result in results:
        print(result)

login=tk.Button(root, text='Login', command=usrlogin)
login.place(x=170, y=230)

root.mainloop()
