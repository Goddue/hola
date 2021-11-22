import sys

import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableView, QTableWidgetItem


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('main.ui', self)
        spisock = ['Сорт', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки']

        self.con = sqlite3.connect("coffe.sqlite")
        cur = self.con.cursor()
        result = cur.execute(f'''SELECT coffe.id, sorts.Name as sort, degree.degree, grind.grind,
description.description, price.price FROM 
coffe join degree on degree.id = coffe.degree
join description on description.id = coffe.description
join grind on grind.id = coffe.grind
join price on price.id = coffe.price
join sorts on sorts.id = coffe.sort''').fetchall()
        print(result)
        self.result = result
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):

                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def do(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
