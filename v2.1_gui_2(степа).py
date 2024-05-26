from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QMessageBox
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import time

app = QtWidgets.QApplication([])
ui = uic.loadUi("gra3stopandnew_start.ui")
ui.setWindowTitle("Тахометр 3000")

ser = QSerialPort()
ser.setBaudRate(9600)

portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comboBox.addItems(portList)

x, y, x1, y1 = [], [], [], []
popravka = 0
active = False

data = {"a": [], "b": []}
print(list(data.items())[0][0])


def Open():
    ser.setPortName(ui.comboBox.currentText())
    ser.open(QIODevice.ReadWrite)
    if len(ui.comboBox.currentText()) != 0:
        print(ui.comboBox.currentText())
        ui.check.setText('Подключено')
        ui.check.setStyleSheet("background-color: green")
    else:
        ui.check.setText('Не подключено')
        ui.check.setStyleSheet("background-color: red")


def Stop():
    global active
    active = False


def Start():
    global active
    active = True


# добавили новые массив и теперь надо его обработаь
def New_Data():
    global data, popravka
    #print(data)
    n = len(data)
    data[n * 'x'] = []
    data[n * 'y'] = []
    popravka = 0


def graph():
    global x, y, popravka, active

    if not ser.canReadLine(): return

    if (active == True):
        rx = ser.readLine()
        rxs = str(rx, 'utf-8').strip()
        rpm, ttime = rxs.split(',')
        ttime = float(ttime)
        rpm = float(rpm)

        if (popravka == 0):
            popravka = float(ttime)

        ttime -= popravka


        n = len(data)
        x = list(data.items())[n - 2][0]
        y = list(data.items())[n - 1][0]  # индекс масива куда вставлять

        data[y].append(rpm)
        data[x].append(ttime)
        pen = pg.mkPen(color=(100*n%255, 0, 100*n%255))
        ui.graph.plot(data[x], data[y],pen=pen)

        ui.graph.setTitle("Rm", color="b", size="10pt")
        styles = {"color": "#f00", "font-size": "15px"}
        ui.graph.setLabel("left", "RM/min", **styles)
        ui.graph.setLabel("bottom", "Sec", **styles)

    # print(ttime, rpm)


def Close_window():
    reply = QMessageBox.question(ui, 'Закрыть окно.', 'Вы уверены, что хотите закрыть окно?',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        ui.close()
        print('Окно закрыто.')
    else:
        pass


# ноеое измерение/стоп
# новое измерение - создается новый массив и в него записываются все данные
# стоп, чтение с порта отсанавлявается

ser.readyRead.connect(graph)
ui.check.clicked.connect(Open)
ui.end.clicked.connect(Close_window)
ui.stop.clicked.connect(Stop)
ui.start.clicked.connect(Start)
ui.new_start.clicked.connect(New_Data)

ui.show()
app.exec()
