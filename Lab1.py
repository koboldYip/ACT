import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy
import math
import colorama as color

units = {1: 'Безынерционное звено', 2: 'Апериодическое звено', 3: 'Интегрирующее звено',
         4: 'Идеальное дифференциальное звено', 5: 'Реальное дифференциальное звено'}


def choice():
    needNewChoice = True

    while needNewChoice:
        print(color.Style.RESET_ALL)
        print("Введите номер команды: \n")
        for key, value in units.items():
            print(f"{key} — {value}")
        userInput = input()
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput in units:
                name = units.get(userInput)
                print(name)
                needNewChoice = False
            else:
                print(color.Fore.RED + "\nНедопустимое значение!")
        else:
            print(color.Fore.RED + "\nПожалуйста, введите числовое значение!")
    return name


def getUnit(name):
    needNewChoice = True

    while needNewChoice:
        k = input("пожалуйста, введите коэффициент 'k' : ")
        t = input("пожалуйста, введите коэффициент 't' : ")

        try:
            needNewChoice = False
            k = float(k)
            t = float(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                if t == 0:
                    unit = matlab.tf([k], [1, 0])
                else:
                    unit = matlab.tf([1], [t, 1])
            elif name == 'Идеальное дифференциальное звено':
                if t == 0:
                    unit = matlab.tf([k, 0], [1])
                else:
                    unit = matlab.tf([t, 0], [1])
            elif name == 'Реальное дифференциальное звено':
                unit = matlab.tf([k, 0], [t, 1])
        except:
            print(color.Fore.RED + "\nПожалуйста, введите числовое значение!")
    return unit


def graph(num, title, y, x):
    pyplot.subplot(2, 1, num)
    pyplot.grid(True)
    if title == "Переходная характеристика":
        pyplot.plot(x, y, 'purple')
    elif title == "Импульсная характеристика":
        pyplot.plot(x, y, "green")
    pyplot.title(title)
    pyplot.ylabel("Амплитуда")
    pyplot.xlabel("Время (с)")


type(1.)

unitName = choice()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 10000):
    timeLine.append(i / 1000)

[y, x] = matlab.step(unit, timeLine)
graph(1, "Переходная характеристика", y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, "Импульсная характеристика", y, x)
pyplot.show()
matlab.bode(unit, dB=False)
pyplot.plot()
pyplot.xlabel('Частота, Гц')
pyplot.show()
