import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from datetime import datetime



def read_history():
    cursor.execute("SELECT * FROM history")
    return cursor.fetchall()


def fill_table():
    t = read_history()

    tableWidget.setRowCount(len(t))
    tableWidget.setColumnCount(3)

    for i, j in enumerate(t):
        for j, value in enumerate(j):
            item = QTableWidgetItem(str(value))
            tableWidget.setItem(i, j, item)

tec_tame = 0
difference = 'erg'
# Создание базы данных и таблицы
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

cursor.execute('INSERT INTO history (time, operation) VALUES (?, ?)', (tec_tame, difference))

app = QApplication([])
window = QMainWindow()
tableWidget = QTableWidget()

fill_table()

window.setCentralWidget(tableWidget)
window.show()

app.exec_()