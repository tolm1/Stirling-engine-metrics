import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    if(work):
        ser.write(b's')
        data_for_arduino()
          # Transmit the char 'g' to receive the Arduino data point
        if(count_zero > 20):
            ser.write(b'b')
            work = False

        plt.cla()
        plt.plot(x, y, label='Измерение 1')
        plt.xlabel('Time')
        plt.ylabel('Rm/m')
        plt.legend()

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate,interval=100)
plt.show()