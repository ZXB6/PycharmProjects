import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setWindowTitle('MainWidget 模板')

        self.top_layout = QVBoxLayout()
        self.setLayout(self.top_layout)
        self.resize(500, 300)

        self.data_table_view = QTableView()
        self.model = QStandardItemModel(3, 0, self)

        self.model.setHorizontalHeaderItem(0, QStandardItem("姓名"))
        self.model.setHorizontalHeaderItem(1, QStandardItem("性别"))
        self.model.setHorizontalHeaderItem(2, QStandardItem("体重(kg)"))

        for row in range(3):                                   # 2
            for column in range(3):
                item = QStandardItem('({}, {})'.format(row, column))
                self.model.setItem(row, column, item)

        #self.model.setItem()
        item1 = QStandardItem('李雷')
        self.model.setItem(0, 0, item1)

        item2 = QStandardItem('男')
        self.model.setItem(0, 1, item2)

        item3 = QStandardItem('70')
        self.model.setItem(0, 2, item3)

        self.model.appendRow([QStandardItem('韩梅'), QStandardItem('女'), QStandardItem('60'), QStandardItem('请假')])
        self.model.insertRow(4, [QStandardItem('吉姆'), QStandardItem('男'), QStandardItem('65')])
        self.data_table_view.setModel(self.model)

        self.data_table_view.horizontalHeader().setStretchLastSection(True)
        self.data_table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.data_table_view.clicked.connect(self.show_info)

        self.info_label = QLabel(self)
        self.info_label.setAlignment(Qt.AlignCenter)

        self.top_layout.addWidget(self.data_table_view)
        self.top_layout.addWidget(self.info_label)

    def show_info(self):
        row = self.data_table_view.currentIndex().row()
        column = self.data_table_view.currentIndex().column()
        print('({}, {})'.format(row, column))

        data = self.data_table_view.currentIndex().data()
        self.info_label.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()

    sys.exit(app.exec_())


