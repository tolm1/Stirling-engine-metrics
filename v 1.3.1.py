import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial.tools.list_ports
from tkinter import *


root = Tk()


def btn_click():
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description
    ]
    if not arduino_ports:
        print("Ардуина не подключена")
    else:
        if len(arduino_ports) > 1:
            print("Найдено несколько Ардуин - Использую первую")
        else:
            print('Ардуина подключена')
        return arduino_ports[0]


def btn_click2():
    ser = serial.Serial("COM3", 9600)  # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
    time.sleep(2)

    x = []
    y = []
    count_zero = 0
    work = True

    def data_for_arduino():
        global count_zero
        arduinoData_string = ser.readline().decode('utf-8').strip()
        try:
            rpm, ttime = arduinoData_string.split(",")
            rpm = float(rpm)
            x.append(float(ttime))
            y.append(rpm)

            if (rpm == 0.0):
                count_zero += 1
        except:  # Pass if data point is bad
            pass

    def animate(i):
        global work
        if (work):
            ser.write(b's')
            data_for_arduino()
            # Transmit the char 'g' to receive the Arduino data point
            if (count_zero > 20):
                ser.write(b'b')
                work = False

            plt.cla()
            plt.plot(x, y, label='Измерение 1')
            plt.xlabel('Time')
            plt.ylabel('Rm/m')
            plt.legend()

    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()

root.title('Измеритель-оборотов-3000-инатор')
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=0.5, relheight=1)

frame2 = Frame(root, bg='white')
frame2.place(relx=0.5, relwidth=0.5, relheight=1)

#title = Label(frame, text='Проверка оборудования', bg='gray', font=40)
#title.pack()

btn = Button(frame, text='Проверка оборудования', bg='yellow', command=btn_click)
btn.pack()

btn2 = Button(frame2, text='Начать замер', bg='yellow', command=btn_click2)
btn2.pack()

root.mainloop()