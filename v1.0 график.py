import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

import serial
import time
from datetime import datetime
from openpyxl import Workbook
import math

ser=serial.Serial()
ser.port = "COM3"
ser.baudrate = 9600
#arduino.timeout = 1
#arduino.setDTR(False)
import numpy
ser.open()

workbook = Workbook()
sheet = workbook.active
arr = []
_ = 0
x = []
y = []

while True:
    data = ser.readline().decode('utf-8').strip()

    rpm, ttime = data.split(",")
    rpm = float(rpm)

    if(rpm == 0.00):
        _+=1
    if(_ == 50):
        break
    print(_)
    #if(numpy.isnan(rpm) != True):
    sheet.append([int(ttime), (rpm)])
    #arr.append([0,float(ttime), float(rpm)])
    print([0, float(ttime), float(rpm)])
    x.append(ttime)
    y.append(rpm)
    #print(x,y)
    workbook.save('data3.xlsx')

plt.figure()
plt.plot(x,y)
plt.show()
