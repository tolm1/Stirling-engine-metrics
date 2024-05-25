from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import QIODevice
from  pyqtgraph import PlotWidget,plot
import pyqtgraph as pg
from  pyqtgraph import PlotWidget
import time

app = QtWidgets.QApplication([])
ui = uic.loadUi("gra.ui")
ui.setWindowTitle("Тахометр 3000")

ser = QSerialPort()
ser.setBaudRate(9200)

x,y = [],[]

'''for x in range(100): x.append(x)
for x in range(100): y.append(0)'''


def Open():
    ser.setPortName('COM3')
    ser.open(QIODevice.ReadWrite)

def graph():
    global x,y

    rx = ser.readLine()
    #rxs = str(rx, 'utf-8')
    print(rx)
    '''rpm,ttime = rxs.split(',')
    rpm = float(rpm)
    x.append(float(ttime))
    y.append(rpm)
    ui.graph.plot(x, y)'''

ser.readyRead.connect(graph)
ui.start.clicked.connect(Open)

ui.show()
app.exec()