#файл нужен для теста масшабирования и взятия данных из файла
#вариант плохой, потому что при больши файлах системе надо просомтреть несколько тысяч измерений, что занимает какое-то время
#за это время система может измениться и будут еще данные или не так часто данные посылать
#даже при мальных измерениях файл
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def data_ani(i):
    data = open('data2.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []

    for line in lines:
        if len(line) != 0:
            x,y = line.split(";")
            xs.append(float(x))
            ys.append(float(y))
        else:
            break

    ax.clear()
    ax.plot(xs,ys)

    plt.xlabel("time")
    plt.ylabel("rm/s")
    plt.title("Rm/s in real time")

ani = animation.FuncAnimation(fig,data_ani,interval=1000)
plt.show()