import numpy as np
import pandas as pd
import pymssql
import pymysql
import qtawesome
from tkinter import *
import os
import time
import threading
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
import xlrd


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QStackedWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(self.close1)  # 关闭窗口
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_visit.clicked.connect(self.back)  # 关闭窗口
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(self.showMinimized)  # 最小化窗口

        self.left_label_1 = QtWidgets.QPushButton("信息更改")
        self.left_label_1.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("帮助与用户")
        self.left_label_3.setObjectName('left_label')
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.address-card-o', color='white'), "信息查找")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.left_button1_clicked2)
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.trash-o', color='white'), "信息删除")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.left_button1_clicked3)
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='white'), "信息修改")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(self.left_button1_clicked4)
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.plus-square-o', color='white'), "信息增加")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(self.left_button1_clicked5)
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.user-o', color='white'), "个人中心")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.left_button1_clicked)
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(self.left_button1_clicked1)
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        #默认页面
        self.form1 = QWidget()
        self.right_widget.addWidget(self.form1)
        self.formLayout1 = QtWidgets.QGridLayout(self.form1)

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.right_folder_button22 = QtWidgets.QPushButton(qtawesome.icon('fa.folder', color='GoldenRod'), "")
        self.right_folder_button22.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:none}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button22.setObjectName('right_search_button')
        self.right_folder_button22.setFont(qtawesome.font('fa', 16))
        self.right_folder_button22.clicked.connect(self.right_folder_button_clicked31)
        self.right_folder_button22.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button11 = QtWidgets.QPushButton("导入数据库")
        self.right_folder_button11.setObjectName('right_search_button')
        self.right_folder_button11.setFont(qtawesome.font('fa', 16))
        self.right_folder_button11.clicked.connect(self.right_folder_button_clicked51)
        self.right_folder_button11.setFixedSize(140, 40)  # 设置按钮大小
        self.right_folder_button11.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button111 = QtWidgets.QPushButton("清空数据库")
        self.right_folder_button111.setObjectName('right_search_button')
        self.right_folder_button111.setFont(qtawesome.font('fa', 16))
        self.right_folder_button111.clicked.connect(self.view_data23)
        self.right_folder_button111.setFixedSize(140, 40)  # 设置按钮大小
        self.right_folder_button111.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input9 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input9.setPlaceholderText("填入或选择需要上传的文件夹")
        self.right_bar_widget_folder_input9.setObjectName("right_input_item")
        self.right_bar_widget_folder_input9.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.user11 = QtWidgets.QLabel("数据的导入")
        self.user11.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user11, 0, 0,1,10)

        self.recommend_button_11 = QtWidgets.QToolButton()
        self.recommend_button_11.setIcon(QtGui.QIcon('./5.png'))
        self.recommend_button_11.setIconSize(QtCore.QSize(1000, 1000))
        self.right_bar_layout1.addWidget(self.recommend_button_11, 0, 0, 10, 10)
        self.recommend_button_11.setStyleSheet('''
                                                QToolButton{border:none;color:black;}
                                                QToolButton:hover{color:white}
                                                 ''')
        self.right_bar_layout1.addWidget(self.right_folder_button22, 8, 1, 20, 6)
        self.right_bar_layout1.addWidget(self.right_folder_button11, 10, 3, 20,1)
        self.right_bar_layout1.addWidget(self.right_folder_button111, 10, 5, 20, 1)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input9, 8, 2, 20, 6)
        self.formLayout1.addWidget(self.right_bar_widget1, 0, 0, 9, 0)

        #个人中心
        self.form2 = QWidget()
        self.right_widget.addWidget(self.form2)
        self.formLayout2 = QtWidgets.QGridLayout(self.form2)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        # 2.2 个人信息
        self.a = QPushButton(qtawesome.icon('fa.user', color="black"), ":")  #个人账号
        self.a.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.mars', color="black"), ":")  # 个人账号
        self.a1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a2 = QPushButton(qtawesome.icon('fa.university', color="black"), ":")  # 个人账号
        self.a2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a3 = QPushButton(qtawesome.icon('fa.birthday-cake', color="black"), ":")  # 个人账号
        self.a3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a4 = QPushButton(qtawesome.icon('fa.child', color="black"), ":")  # 个人账号
        self.a4.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.user9 = QtWidgets.QLabel("个人资料")
        self.user9.setFont(qtawesome.font('fa', 31))
        self.right_bar_layout1.addWidget(self.user9, 0, 1, 2, 4)
        f = open("2.txt", 'r+')
        word = f.readline()
        self.user = QtWidgets.QLabel(word)
        self.user.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user, 3, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a, 3, 2, 2, 3)
        self.user1 = QtWidgets.QLabel("男")
        self.user1.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user1, 5, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a1, 5, 2, 2, 3)
        self.user4 = QtWidgets.QLabel("username")
        self.user4.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user4, 4, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a4, 4, 2, 2, 3)
        self.user2 = QtWidgets.QLabel("湖南财政经济学院")
        self.user2.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user2, 6, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a2, 6, 2, 2, 3)
        self.user3 = QtWidgets.QLabel("2001.11")
        self.user3.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user3, 7, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a3, 7, 2, 2, 3)
        self.a.setFont(qtawesome.font('fa', 22))
        self.a.setIconSize(QtCore.QSize(20, 20))
        self.user.setObjectName('right_search_button1')
        self.xiugai = QtWidgets.QPushButton(qtawesome.icon('fa.address-card', color='black'), "修改密码")
        self.xiugai.setObjectName('right_search_button2')
        self.xiugai.setFont(qtawesome.font('fa', 30))
        self.xiugai.clicked.connect(self.right_folder_button_clicked)
        self.right_bar_layout1.addWidget(self.xiugai, 26, 4, 1, 3)
        self.xiugai.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.zhuxiao = QtWidgets.QPushButton(qtawesome.icon('fa.reply-all', color='black'),"注销账号")
        self.zhuxiao.setObjectName('right_search_button2')
        self.zhuxiao.setFont(qtawesome.font('fa', 16))
        self.zhuxiao.clicked.connect(self.right_folder_button_clicked1)
        self.right_bar_layout1.addWidget(self.zhuxiao, 27, 4, 1, 3)
        self.zhuxiao.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.bianji = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='black'), "编辑资料")
        self.bianji.setObjectName('right_search_button3')
        self.bianji.setFont(qtawesome.font('fa', 16))
        self.bianji.clicked.connect(self.right_folder_button_clicked2)
        self.right_bar_layout1.addWidget(self.bianji, 25, 4, 1, 3)
        self.bianji.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setIcon(QtGui.QIcon('./3.png'))
        self.recommend_button_1.setIconSize(QtCore.QSize(200, 200))
        self.right_bar_layout1.addWidget(self.recommend_button_1, 3, 1, 6, 1)
        self.recommend_button_1.setStyleSheet('''
                                 QToolButton{border:none;color:black;}
                                 QToolButton:hover{color:white}
                                  ''')
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 9)

        self.right_bar_widget2 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout2 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget2.setLayout(self.right_bar_layout2)
        self.formLayout2.addWidget(self.right_bar_widget2, 1, 0, 1, 9)

        # 右边栏美化
        # 右边框整体风格美化
        self.right_widget.setStyleSheet('''
                    QStackedWidget#right_stacked_Widget{
                        color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-right-radius:10px;
                        border-bottom-right-radius:10px;
                    }

                    QLabel#right_lable{
                        border:none;
                        font-size:16px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                ''')

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
                   QPushButton{border:none;color:white;}
                   QPushButton#left_label{
                       border:none;
                       border-bottom:1px solid SteelBlue;
                       font-size:18px;
                       font-weight:700;
                       font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                   }
                   QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}

                   QWidget#left_widget{
                       background:SteelBlue;
                       border-top:1px solid white;
                       border-bottom:1px solid white;
                       border-left:1px solid white;
                       border-top-left-radius:10px;
                       border-bottom-left-radius:10px;
                   }
               ''')

        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')
        self.main_layout.setSpacing(0)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # 遇到问题
        self.form3 = QWidget()
        self.right_widget.addWidget(self.form3)
        self.formLayout2 = QtWidgets.QGridLayout(self.form3)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        # 2.2 问题
        self.user9 = QtWidgets.QLabel("关于与帮助")
        self.user9.setFont(qtawesome.font('fa', 30))
        self.right_bar_layout1.addWidget(self.user9, 0, 1, 2, 4)
        self.user = QtWidgets.QPushButton(qtawesome.icon('fa.question-circle-o', color="black"), "使用帮助")
        self.user.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user, 8, 3, 1,4)
        self.user.clicked.connect(self.right_folder_button_clicked3)
        self.user.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.user1 = QtWidgets.QPushButton(qtawesome.icon('fa.envelope-open-o', color="black"), "反馈问题")
        self.user1.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user1, 9, 3, 1,4)
        self.user1.clicked.connect(self.right_folder_button_clicked4)
        self.user1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 5)
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setIcon(QtGui.QIcon('./4.jpg'))
        self.recommend_button_1.setIconSize(QtCore.QSize(1000, 1000))
        self.right_bar_layout1.addWidget(self.recommend_button_1, 2, 1, 6, 8)
        self.recommend_button_1.setStyleSheet('''
                                         QToolButton{border:none;color:black;}
                                         QToolButton:hover{color:white}
                                          ''')
        self.right_bar_widget2 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout2 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget2.setLayout(self.right_bar_layout2)
        self.formLayout2.addWidget(self.right_bar_widget2, 1, 0, 1, 9)


        # 订单查询
        self.form4 = QWidget()
        self.right_widget.addWidget(self.form4)
        self.formLayout2 = QtWidgets.QGridLayout(self.form4)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm5 = QtWidgets.QLabel('订单查询')
        self.mm5.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button1 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "查询")
        self.right_folder_button1.setObjectName('right_search_button')
        self.right_folder_button1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button1.setFont(qtawesome.font('fa', 20))
        self.right_folder_button1.clicked.connect(self.view_data111)
        self.right_folder_button1.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "清空")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        self.right_folder_button3.clicked.connect(self.view_data2)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2.clicked.connect(self.view_data)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input88 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input88.setPlaceholderText("请输入订单号/顾客编号/工号/菜品编号")
        self.right_bar_widget_folder_input88.setObjectName("right_input_item");
        self.right_bar_widget_folder_input88.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm5, 0, 0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button1, 1, 21, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input88, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)
        #消息框美化
        self.right_message_Alter.setStyleSheet(''' 
                                           QMessageBox{
                                               background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,stop: 0 rgba(255, 255, 255, 100%),
                                               stop: 1 rgba(70, 130, 180, 100%));
                                               border-top:1px solid black;
                                               border-bottom:1px solid black;
                                               border-left:1px solid black;
                                               border-right:1px solid black;
                                               border-radius:10px;
                                               padding:2px 4px;
                                           }   
                                       ''')
        self.right_batch_result_listView.setStyleSheet('''
                    QListView {
                        alternate-background-color: yellow; 
                        padding:2px 4px;
                    }
                    QListView {
                    show-decoration-selected: 1; /* make the selection span the entire width of the view */
                    }
                    /* 此处QListView::item:alternate覆盖会alternate-background-color: yellow属性*/
                    QListView::item:alternate {
                        background: #EEEEEE; /* item交替变换颜色，如图中灰色 */
                    }
                    QListView::item:selected {
                    border: 1px solid #6a6ea9;
                    }
                    QListView::item:selected:!active {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #ABAFE5, 
                                                 stop: 1 #8588B2);
                    }
                    QListView::item:selected:active {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #6a6ea9, 
                                                 stop: 1 #888dd9);
                    }
                    QListView::item:hover {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                 stop: 0 #FAFBFE, 
                                                 stop: 1 #DCDEF1);

                ''')

        # 信息删除

        self.form5 = QWidget()
        self.right_widget.addWidget(self.form5)
        self.formLayout2 = QtWidgets.QGridLayout(self.form5)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm5 = QtWidgets.QLabel('信息删除')
        self.mm5.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button211 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "删除")
        self.right_folder_button211.setObjectName('right_search_button')
        self.right_folder_button211.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button211.setFont(qtawesome.font('fa', 20))
        self.right_folder_button211.clicked.connect(self.view_data3)
        self.right_folder_button211.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button211.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "清空")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        self.right_folder_button3.clicked.connect(self.view_data22)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2.clicked.connect(self.view_data11)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input112 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input112.setPlaceholderText("请输入订单编号/顾客编号/工号")
        self.right_bar_widget_folder_input112.setObjectName("right_input_item");
        self.right_bar_widget_folder_input112.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm5, 0, 0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button211, 1, 21, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input112, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView1 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView1, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        #信息修改
        self.form6 = QWidget()
        self.right_widget.addWidget(self.form6)
        self.formLayout2 = QtWidgets.QGridLayout(self.form6)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm4 = QtWidgets.QLabel('信息修改')
        self.mm4.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button211 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "查询")
        self.right_folder_button211.setObjectName('right_search_button')
        self.right_folder_button211.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button211.setFont(qtawesome.font('fa', 20))
        self.right_folder_button211.clicked.connect(self.view_data4)
        self.right_folder_button211.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button211.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='balck'), "修改")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        self.right_folder_button3.clicked.connect(self.view_data24)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")


        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2.clicked.connect(self.view_data1111)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input11 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input11.setPlaceholderText("请输入订单号/顾客编号/工号/菜品编号")
        self.right_bar_widget_folder_input11.setObjectName("right_input_item");
        self.right_bar_widget_folder_input11.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm4, 0, 0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        self.right_bar_layout1.addWidget(self.right_folder_button211, 1, 21, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input11, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView2 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView2, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)

        # 信息增加

        self.form6 = QWidget()
        self.right_widget.addWidget(self.form6)
        self.formLayout2 = QtWidgets.QGridLayout(self.form6)

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm = QtWidgets.QLabel('信息增加')
        self.mm.setFont(qtawesome.font('fa', 35))

        self.right_folder_button2111 = QtWidgets.QPushButton(qtawesome.icon('fa.user-o', color='balck'), "查询增加的信息")
        self.right_folder_button2111.setObjectName('right_search_button')
        self.right_folder_button2111.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2111.setFont(qtawesome.font('fa', 20))
        self.right_folder_button2111.clicked.connect(self.view_data53)
        self.right_folder_button2111.setFixedSize(250, 30)  # 设置按钮大小
        self.right_folder_button2111.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button28 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'),
                                                             "清空")
        self.right_folder_button28.setObjectName('right_search_button')
        self.right_folder_button28.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button28.setFont(qtawesome.font('fa', 20))
        self.right_folder_button28.clicked.connect(self.view_data54)
        self.right_folder_button28.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button28.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button23 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'), "查询全部信息")
        self.right_folder_button23.setObjectName('right_search_button')
        self.right_folder_button23.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button23.setFont(qtawesome.font('fa', 20))
        self.right_folder_button23.clicked.connect(self.view_data52)
        self.right_folder_button23.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button23.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button31 = QtWidgets.QPushButton(qtawesome.icon('fa.check-circle', color='balck'), "完成")
        self.right_folder_button31.setObjectName('right_search_button')
        self.right_folder_button31.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button31.setFont(qtawesome.font('fa', 20))
        self.right_folder_button31.clicked.connect(self.view_data51)
        self.right_folder_button31.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button31.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_folder_button311 = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='balck'), "增加")
        self.right_folder_button311.setObjectName('right_search_button')
        self.right_folder_button311.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button311.setFont(qtawesome.font('fa', 20))
        self.right_folder_button311.clicked.connect(self.view_data5)
        self.right_folder_button311.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button311.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_layout1.addWidget(self.mm, 0,0, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button2111, 1, 9, 1, 11)
        self.right_bar_layout1.addWidget(self.right_folder_button23, 0, 9, 1, 6)
        self.right_bar_layout1.addWidget(self.right_folder_button28, 0, 15, 1, 5)
        self.right_bar_layout1.addWidget(self.right_folder_button31, 0, 6, 1, 2)
        self.right_bar_layout1.addWidget(self.right_folder_button311, 0, 4, 1, 2)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))
        self.right_batch_result_listView3 = QtWidgets.QTableView()
        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView3, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)


    # 导入数据库
    def back(self):
            self.right_widget.setCurrentIndex(0)

     #个人中心
    def left_button1_clicked(self):
         self.right_widget.setCurrentIndex(1)

    #遇到问题
    def left_button1_clicked1(self):
        self.right_widget.setCurrentIndex(2)

    #订单查询
    def left_button1_clicked2(self):
         self.right_widget.setCurrentIndex(3)

    #信息删除
    def left_button1_clicked3(self):
        self.right_widget.setCurrentIndex(4)

        # 信息修改
    def left_button1_clicked4(self):
        self.right_widget.setCurrentIndex(5)

        # 信息增加
    def left_button1_clicked5(self):
        self.right_widget.setCurrentIndex(6)


    #修改密码
    def right_folder_button_clicked(self):
        w3.show()

    #个人中心注销账号
    def right_folder_button_clicked1(self):
        demo.close()
        login.show()

    #编辑资料
    def right_folder_button_clicked2(self):
        pass

    #默认页面的路径选择
    def right_folder_button_clicked31(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        demo.right_bar_widget_folder_input9.setText(fileName)

     #导入数据库
    def right_folder_button_clicked51(self):
      try:
        file = open("8.txt", 'w').close()
        ap = demo.right_bar_widget_folder_input9.text()
        if ap == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
          book = xlrd.open_workbook(ap)
          sheet = book.sheet_by_index(0)
        # 建立一个SQL连接
          conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa', password='123456',
                           database='Restaurant',charset='GBK')
        # 获得游标
          cur = conn.cursor()
        # 创建插入SQL语句
          query = 'insert into oder(订单编号,顾客编号,消费时间,餐桌编号,服务员编号) values (%s, %s, %s, %s， %s)'
        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
          for r in range(0, sheet.nrows):
            订单编号 = sheet.cell(r, 0).value
            顾客编号 = sheet.cell(r, 1).value
            消费时间 = sheet.cell(r, 2).value
            餐桌编号 = sheet.cell(r, 3).value
            服务员编号 = sheet.cell(r, 4).value
            with open('8.txt', 'a') as f3:
                f3.write(sheet.cell(r, 0).value + " " + sheet.cell(r, 1).value+"\n")
            values = (订单编号,顾客编号,消费时间,餐桌编号,服务员编号)
            # 执行sql语句
            cur.execute(query, values)
          cur.close()
          conn.commit()
          conn.close()
          QMessageBox.information(self, '成功', '导入成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
      except:
          QMessageBox.information(self, '错误', '导入失败', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #使用帮助
    def right_folder_button_clicked3(self):
        self.right_message_Alter.information(self.right_message_Alter, "联系方式", self.tr("如果有什么问题可以通过以下方式联系我们：\nQQ:"
                                                                                       "1625062875\n邮箱：2466900856@qq.com"))

    #反馈问题
    def right_folder_button_clicked4(self):
        self.right_message_Alter.information(self.right_message_Alter, "使用说明", self.tr("该应用程序使用说明如下：\n在信息更改中可以实现对信息的增删改查。\n如果有问题可以在遇到问题中咨询我们也可以更改代码"))

    #订单查询中查询全部信息
    def view_data(self):
        try:
            # 调用输入框获取数据库名称
            conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',password='123456',database='Restaurant', charset='GBK')
        except:
            pass
        cur = conn.cursor()  # 生成游标对象
        sql = "select * from oder"  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        data=np.array(data)
        # print(data[:,0])
        QMessageBox.information(self, '订单编号', str(data[:,:3]), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        # self.model =QtSql.QSqlTableModel()
        # self.right_batch_result_listView1.setModel(self.model)
        # self.model.setTable('reference')  # 设置使用数据模型的数据表
        # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        # self.model.select()  # 查询所有数据


        # input_table = pd.read_sql(sql, conn)  # 返回全部数据
        # input_table_rows = input_table.shape[0]  # 返回总行数，int类型
        # input_table_colunms = input_table.shape[1]  # 返回总列数对象，int类型
        # input_table_header = input_table.columns.values.tolist()  # 返回sql所有字段名
        # self.tableWidget.setColumnCount(input_table_colunms)
        # self.tableWidget.setRowCount(input_table_rows)
        # self.tableWidget.setHorizontalHeaderLabels(input_table_header)
        # for i in range (input_table_rows) :  # 5即是循环总rows
        #     input_table_rows_values = input_table.iloc[[i]]
        #     input_table_rows_values_array = np.array(input_table_rows_values)
        #     input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
        #     for j in range (input_table_colunms):  # 6即是显示的总列数
        #         input_table_items_list = input_table_rows_values_list[j]
        #     ###==============将遍历的元素添加到tablewidget中并显示=======================
        #         input_table_items = str(input_table_items_list)
        #         newItem = QTableWidgetItem(input_table_items)
        #         newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #         self.tableWidget.setItem(i, j, newItem)
    #删除中的查询全部信息
    def view_data11(self):
            try:
                # 调用输入框获取数据库名称
                conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',password='123456',database='Restaurant', charset='GBK')
            except :
                pass
                # 实例化一个可编辑数据模型
            cur = conn.cursor()  # 生成游标对象
            sql = "select * from menus_oder"  # SQL语句
            cur.execute(sql)  # 执行SQL语句
            data = cur.fetchall()  # 通过fetchall方法获得数据
            print(data)
            data = np.array(data)
            QMessageBox.information(self, '订单', str(data[:, :3]), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            cur.close()  # 关闭游标
            conn.close()  # 关闭连接

    #信息查询中的查询
    def view_data111(self):
        gettxt= self.right_bar_widget_folder_input88.text()
        print(gettxt)

        if gettxt == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
              conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',password='123456',database='Restaurant', charset='GBK')
              cur = conn.cursor()  # 获取一个游标or  O_id ='{}'
              sql_select = "select * from oder where T_id='{}' ".format(gettxt)  # 定义查询
              cur.execute(sql_select)  # 执行查询
              data = cur.fetchall()  # 获取查询到数据
              data = np.array(data)
              stri = "信息"
              if data.size== 0:
                  sql_select = "select * from oder where O_id ='{}' ".format(gettxt)  # 定义查询
                  cur.execute(sql_select)  # 执行查询
                  data = cur.fetchall()  # 获取查询到数据
                  data = np.array(data)
                  stri="订单信息"

              if data.size== 0:
                  sql_select = "select * from foodtable where Cz_id ='{}' ".format(gettxt)  # 定义查询
                  cur.execute(sql_select)  # 执行查询
                  data = cur.fetchall()  # 获取查询到数据
                  data = np.array(data)
                  stri = "餐桌状态信息"
              if data.size== 0:
                  sql_select = "select * from worke where W_id ='{}' ".format(gettxt)  # 定义查询
                  cur.execute(sql_select)  # 执行查询
                  data = cur.fetchall()  # 获取查询到数据
                  data = np.array(data)
                  stri = "员工信息"
              if data.size== 0:
                  sql_select = "select * from menus where M_id ='{}' ".format(gettxt)  # 定义查询
                  cur.execute(sql_select)  # 执行查询
                  data = cur.fetchall()  # 获取查询到数据
                  data = np.array(data)
                  stri = "菜品信息"
              if data.size== 0:
                  QMessageBox.information(self, '错误', '不存在该信息', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
              else:
                  QMessageBox.information(self, stri, str(data[:, :3]), QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)

              cur.close()  # 关闭游标
              conn.close()  # 关闭连接
    #修改中的查询全部信息
    def view_data1111(self):
        try:
            # 调用输入框获取数据库名称
            conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',password='123456',database='Restaurant', charset='GBK')
        except:
            pass
        cur = conn.cursor()  # 生成游标对象
        sql = "select * from oder"  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        data=np.array(data)
        # print(data[:,0])
        QMessageBox.information(self, '订单编号', str(data[:,:3]), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接

    #查询中的清除
    def view_data2(self):
        self
    # 删除中的清空
    def view_data22(self):
        self
    #清空数据库
    def view_data23(self):
        self
    #     try:
    #         conn = pymssql.connect(host='127.0.0.1', user='root', passwd='', db='', charset='utf8')
    #         cur = conn.cursor()  # 获取一个游标
    #         query1 = //////
    #         cur.execute(query1)
    #         conn.commit()  # 提交事务
    #         cur.close()  # 关闭游标
    #         conn.close()  # 释放数据库资源在这里插入代码片
    #         QMessageBox.information(self, '成功', '清除成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #     except:
    #         QMessageBox.information(self, '错误', '清除失败', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


    # 修改
    def view_data24(self):
        try:
            # 调用输入框获取数据库名称
            conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',
                                   password='123456', database='Restaurant', charset='GBK')
            name1 = self.right_bar_widget_folder_input11.text()
            #name1=var
            if name1  =='':
                QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                cur = conn.cursor()  # 生成游标对象
                sql = "update Tomer set T_phone ='{}' where T_id= '{}' ".format(name1,t)  # SQL语句
                print(sql)
                cur.execute(sql)  # 执行SQL语句
                conn.commit()
                cur.close()  # 关闭游标
                conn.close()  # 关闭连接
                QMessageBox.information(self, '成功', '修改成功!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        except:
            QMessageBox.information(self, '错误', '操作错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #删除
    def view_data3(self):
        gettxt1 = self.right_bar_widget_folder_input112.text()
        if gettxt1 == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
                conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',
                                   password='123456', database='Restaurant', charset='GBK')

                cur = conn.cursor()  # 获取一个游标
                sql_select1 = "select * from oder where O_id='{}'".format(gettxt1)  # 定义查询
                cur.execute(sql_select1)  # 执行查询
                data = cur.fetchall()  # 获取查询到数据
                data = np.array(data)
                flag=1
                stri = "信息"
                if data.size == 0:
                    sql_select = "select * from oder where T_id ='{}' ".format(gettxt1)  # 定义查询
                    cur.execute(sql_select)  # 执行查询
                    data = cur.fetchall()  # 获取查询到数据
                    data = np.array(data)
                    flag = 2
                    stri = "订单信息"
                if data.size == 0:
                    sql_select = "select * from worke where W_id ='{}' ".format(gettxt1)  # 定义查询
                    cur.execute(sql_select)  # 执行查询
                    data = cur.fetchall()  # 获取查询到数据
                    data = np.array(data)
                    flag = 3
                    stri = "员工信息"
                if data.size == 0:
                    QMessageBox.information(self, '删除错误', '不存在该订单/员工或订单/员工已删除', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                else:
                    if flag == 2:
                        sql_select = "DELETE from oder where T_id='{}'".format(gettxt1)  # 定义查询
                        cur.execute(sql_select)
                        conn.commit()
                    if flag == 1:
                        sql_select = "DELETE from oder where O_id='{}'".format(gettxt1)  # 定义查询
                        cur.execute(sql_select)
                        conn.commit()
                    if flag == 3:
                        sql_select = "DELETE from worke where W_id='{}'".format(gettxt1)  # 定义查询
                        cur.execute(sql_select)
                        conn.commit()
                    conn.commit()
                    QMessageBox.information(self, stri, '已删除', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    cur.close()
                    conn.close()

    #修改中的查询
    def view_data4(self):

        gettxt11 = self.right_bar_widget_folder_input11.text()
        global t
        t = str(gettxt11)
        if gettxt11 == '':
            QMessageBox.information(self, '错误', '输入不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
                conn = pymssql.connect(host='localhost:54191', server='LAPTOP-BJ3F4QK8\MSSQLSERVER2', user='sa',
                                   password='123456', database='Restaurant', charset='GBK')
                cur = conn.cursor()  # 获取一个游标or  O_id ='{}'
                sql_select = "select * from tomer where T_id='{}' ".format(gettxt11)  # 定义查询
                cur.execute(sql_select)  # 执行查询
                data = cur.fetchall()  # 获取查询到数据
                data = np.array(data)
                if data.size == 0:
                    QMessageBox.information(self, '错误', '不存在该信息', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '查询成功',str(data[:, :3]), QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)


    #增加
    def view_data5(self):
        self.model = QtSql.QSqlTableModel()
        self.right_batch_result_listView3.setModel(self.model)
        self.model.setTable('student')  # 设置使用数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据
        self.model.index(4,4)
        self.model.insertRows(4, 1)
        self.model.insertColumns(1,4)

     #增加中的完成
    def view_data51(self):
      try:
        index = self.model.index(self.model.rowCount() - 1, 0)  # 调用model的index方法获取行和列对应项的索引
        data12 = index.data()

        conn = pymysql.connect
        cur = conn.cursor()  # 获取一个游标
        # 创建插入SQL语句

        # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
        cur.close()
        conn.commit()
        conn.close()
        with open('8.txt', 'a+') as f: # 注意这里a+是可写可追加
            f.write(data12 + " " +'\n')
            QMessageBox.information(self, '成功', '增加成功', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
      except:
          QMessageBox.information(self, '错误', '操作错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #增加中查询全部
    def view_data52(self):
        self

     #查询增加的信息
    def view_data53(self):
     try:
        conn = pymssql.connect
        cur = conn.cursor()  # 获取一个游标
        cur.close()
        conn.commit()
        conn.close()

     except:
        pass

    #清空增加的人的信息
    def view_data54(self):
        self

    #清空
    def view_data66(self):
        self

    #主界面的关闭按钮
    def close1(self):
     try:
        demo.view_data2()
        demo.view_data22()
        self.close()
     except:
         self.close()


#修改密码
class myform3(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('修改密码')
        self.resize(1440, 720)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./12.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QPushButton(qtawesome.icon('fa.user-secret', color='white'), " ")
        self.verticalLayout.addWidget(self.a, 2, 3, 2, 2)
        self.a.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入原有密码")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 2, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_account.setEchoMode(QLineEdit.Password)
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入新密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.a1 = QPushButton(qtawesome.icon('fa.lock', color='white'), " ")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                                   QPushButton{border:none;color:black;}
                                                   QPushButton:hover{color:white}
                                                    ''')
        self.lineEdit_password1 = QLineEdit()
        self.lineEdit_password1.setPlaceholderText("请再次输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password1, 4, 4, 1, 3)
        self.lineEdit_password1.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.a = QPushButton(qtawesome.icon('fa.lock', color='white'), " ")
        self.verticalLayout.addWidget(self.a, 4, 3, 1, 2)
        self.a.setStyleSheet('''
                                           QPushButton{border:none;color:black;}
                                           QPushButton:hover{color:white}
                                            ''')
        self.lineEdit_password1.setEchoMode(QLineEdit.Password)
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("修改")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)
        self.pushButton_quit.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        ###### 绑定按钮事件
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.pushButton_quit.clicked.connect(self.back)

    def on_pushButton_enter_clicked1(self):
        f1 = open("2.txt", 'r+')
        word = f1.readline()
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        password1 = self.lineEdit_password.text()
        password2 = self.lineEdit_password1.text()
        if account1 == account_dict[word]:
         if account1 != "" and password1 != "" and password2 != "":
            if password2 != password1:
                QMessageBox.information(self, '错误', '密码输入错误,请重新确认', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                account_dict[word] = password1
                with open('1.txt', 'w') as f4:
                    f4.write("")
                for item in account_dict.items():
                        for i in range(len(item)):
                            print(item[i], end=' ')
                            with open('1.txt', 'a') as f3:
                                f3.write(item[i]+" ")
                        with open('1.txt', 'a') as f5:
                            f5.write('\n')

                QMessageBox.information(self, '成功', '修改成功',QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
         else:
            QMessageBox.information(self, '错误', '输入不能为空' , QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '输入的密码与本账号不符', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def QCoreApplication(self):
        w3.close()

    def mini(self):
        w3.showMinimized()

    def back(self):
        w3.close()
#找回密码
class myform(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('找回密码')
        self.resize(1440, 720)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./12.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'), ":")
        self.verticalLayout.addWidget(self.a, 3, 3, 2, 2)
        self.a.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 3, 4, 2, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("找回密码")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)
        self.pushButton_quit.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        ###### 绑定按钮事件
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.pushButton_quit.clicked.connect(self.back)

    def on_pushButton_enter_clicked1(self):
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        if account1 == "" :
            QMessageBox.information(self, '注册失败', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
                account_keys = list(account_dict.keys())
                if account1 not in account_keys:
                    QMessageBox.information(self, '错误', '不存在该账号', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '密码找回成功', '你的密码为：'+account_dict[account1] , QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    #找回密码的关闭
    def QCoreApplication(self):
        w1.close()
    #找回密码的最小化
    def mini(self):
        w1.showMinimized()
    #返回
    def back(self):
        w1.close()
#注册账号
class myform2(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('注册账号')
        self.resize(1440, 720)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./12.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'), ":")
        self.verticalLayout.addWidget(self.a, 2, 3, 1, 2)
        self.a.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.unlock-alt', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                           QPushButton{border:none;color:black;}
                                           QPushButton:hover{color:white}
                                            ''')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.a1 = QPushButton(qtawesome.icon('fa.unlock-alt', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 4, 3, 1, 2)
        self.a1.setStyleSheet('''
                                           QPushButton{border:none;color:black;}
                                           QPushButton:hover{color:white}
                                            ''')
        self.lineEdit_password1 = QLineEdit()
        self.lineEdit_password1.setPlaceholderText("请再次输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password1, 4, 4, 1, 3)
        self.lineEdit_password1.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:200px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.lineEdit_password1.setEchoMode(QLineEdit.Password)

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)
        self.pushButton_quit.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        ###### 绑定按钮事件
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.pushButton_quit.clicked.connect(self.back)

    def on_pushButton_enter_clicked1(self):
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        password1 = self.lineEdit_password.text()
        password2 = self.lineEdit_password1.text()
        if account1 != "" and password1 != "" and password2 != "":
            if password2 != password1:
                QMessageBox.information(self, '错误', '密码输入错误,请重新确认', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                account_keys = list(account_dict.keys())
                if account1 not in account_keys:
                    f = "1.txt"
                    with open(f, "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内
                        file.write(account1 + " " + password1 + "\n")
                    QMessageBox.information(self, '注册成功', '注册成功！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                else:
                    QMessageBox.information(self, '注册失败', '账号已存在！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '注册失败', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def QCoreApplication(self):
        w2.close()
    def mini(self):
        w2.showMinimized()
    def back(self):
        w2.close()
#登录界面
class Login(QWidget):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mode = mode
        self.setWindowTitle('登录界面')
        self.resize(1400, 720)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./12.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.h = QPushButton("找回密码->>")
        self.verticalLayout.addWidget(self.h, 7, 5)
        self.h.setStyleSheet('''
                   QPushButton{border:none;color:black;}
                   QPushButton:hover{color:white}
                    ''')
        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'),":")
        self.verticalLayout.addWidget(self.a, 2, 3, 1 ,2)
        self.a.setStyleSheet('''
                           QPushButton{border:none;color:black;}
                           QPushButton:hover{color:white}
                            ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1,3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                        border:1px solid gray;
                        width:200px;
                        border-radius:10px;
                        padding:2px 4px;
                }''')

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.verticalLayout.addWidget(self.left_mini, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.left_close, 0, 8, 1, 1)
        self.verticalLayout.addWidget(self.left_visit, 0, 7, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置最大化按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.lock', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                        border:1px solid gray;
                        width:200px;
                        border-radius:10px;
                        padding:2px 4px;
                }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.checkBox_remeberpassword = QCheckBox()
        self.checkBox_remeberpassword.setText("记住密码")
        self.verticalLayout.addWidget(self.checkBox_remeberpassword, 4, 4, 1, 3)
        self.checkBox_remeberpassword.setStyleSheet(
            "QCheckBox { color : white; }; QCheckBox::indicator { color:black; }");

        self.checkBox_autologin = QtWidgets.QCheckBox()
        self.checkBox_autologin.setText("自动登录")
        self.verticalLayout.addWidget(self.checkBox_autologin, 4, 5, 1, 3)
        self.checkBox_autologin.setStyleSheet(
            "QCheckBox { color : white; }; QCheckBox::indicator { color:black; }");
        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("登录")
        self.verticalLayout.addWidget(self.pushButton_enter, 5, 4, 1, 3)
        self.pushButton_enter.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 6, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.left_close.clicked.connect(self.QCoreApplication)
        self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.left_mini.clicked.connect(self.mini)
        self.h.clicked.connect(self.h1)

        ####初始化登录信息
        self.init_login_info()

        ####自动登录
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.goto_autologin)
        self.timer.setSingleShot(True)
        self.timer.start(1000)

    # 自动登录
    def goto_autologin(self):
        if self.checkBox_autologin.isChecked() == True and self.mode == 0:
            self.on_pushButton_enter_clicked()

    def on_pushButton_enter_clicked(self):
        # 账号判断
        account_dict = {}
        f = open("1.txt", 'r+')
        for line in f:
            (keys, value) = line.strip().split()
            account_dict[keys] = value
        account1 = self.lineEdit_account.text()
        password1 = self.lineEdit_password.text()
        account_keys = list(account_dict.keys())
        f1 = "2.txt"
        with open(f1, "w") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内
            file.write(account1)
        if account1 != "" and password1 != "":
            if account1 not in account_keys:
                reply1 = QMessageBox.information(self, '登录出错', '用户不存在', QMessageBox.Yes | QMessageBox.No,
                                                 QMessageBox.Yes)
            elif password1 == account_dict[account1]:
                ####### 保存登录信息
                self.save_login_info()
                # 通过验证，关闭对话框并返回1
                self.close()
                demo.show()
            else:
                QMessageBox.information(self, '登录出错', '密码错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.information(self, '错误', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def on_pushButton_enter_clicked1(self):
        w2.show()

    def QCoreApplication(self):
        login.close()

    def mini(self):
        login.showMinimized()

    def h1(self):
        w1.show()

    # 保存登录信息
    def save_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("account", self.lineEdit_account.text())
        settings.setValue("password", self.lineEdit_password.text())
        settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
        settings.setValue("autologin", self.checkBox_autologin.isChecked())

    # 初始化登录信息
    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        the_account = settings.value("account")
        the_password = settings.value("password")
        the_remeberpassword = settings.value("remeberpassword")
        the_autologin = settings.value("autologin")

        self.lineEdit_account.setText(the_account)
        if the_remeberpassword == "true" or the_remeberpassword == True:
            self.checkBox_remeberpassword.setChecked(True)
            self.lineEdit_password.setText(the_password)

        if the_autologin == "true" or the_autologin == True:
            self.checkBox_autologin.setChecked(True)
#欢迎界面
def showWelcome():
    sw = root1.winfo_screenwidth()  # 获取屏幕宽度
    sh = root1.winfo_screenheight()  # 获取屏幕高度r
    root1.overrideredirect(True)  # 去除窗口边框
    root1.attributes("-alpha", 1)  # 窗口透明度（1为不透明，0为全透明）
    x = (sw - 800) / 2
    y = (sh - 450) / 2
    root1.geometry("800x450+%d+%d" % (x, y))  # 将窗口置于屏幕中央
    if os.path.exists(r'./9.gif'):  # 搜索图片文件（只能是gif格式）
        bm = PhotoImage(file=r'./9.gif')
        lb_welcomelogo = Label(root1, image=bm)  # 将图片放置于窗口
        lb_welcomelogo.bm = bm
        lb_welcomelogo.place(x=-2, y=-2, )  # 设置图片位置

def closeWelcome():
    for i in range(2):
        time.sleep(1)  # 屏幕停留时间
    root1.destroy()


if __name__ == '__main__':
    root1 = Tk()
    tMain = threading.Thread(target=showWelcome)  # 开始展示
    tMain.start()
    t1 = threading.Thread(target=closeWelcome)  # 结束展示
    t1.start()
    root1.mainloop()
    app = QtWidgets.QApplication(sys.argv)
    demo = MainUi()
    login = Login()
    w2 = myform2()
    w1 = myform()
    w3 = myform3()
    login.show()
    sys.exit(app.exec_())
