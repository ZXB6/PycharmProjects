import qtawesome
import qtwidgets as QtWidgets
import PyQt5
from PyQt5.QtWidgets import QStackedWidget


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
        self.left_label_2 = QtWidgets.QPushButton("成绩统计")
        self.left_label_2.setObjectName('left_label')
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
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart', color='white'), "成绩排名")
        self.left_button_5.setObjectName('left_button')
        self.left_button_5.clicked.connect(self.left_button1_clicked6)
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart', color='white'), "学科统计")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(self.left_button1_clicked7)
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.user-o', color='white'), "个人中心")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.left_button1_clicked)
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.pie-chart', color='white'), "成绩分布")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.left_button1_clicked8)
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
        self.left_layout.addWidget(self.left_label_2, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
