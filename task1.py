"""
Дескриптор это атрибут объекта со “связанным поведением”,
то есть такой атрибут, при доступе к которому его поведение
переопределяется методом протокола дескриптора.
"""

import time


class NonNegative:
    """
    Этот класс делает атрибуты дескрипторами
    """

    def __set_name__(self, owner, atr):
        self.atr = atr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.atr] = value


class TrafficLight:
    """
    Светофор
    """
    red_time = NonNegative()
    yellow_time = NonNegative()
    green_time = NonNegative()
    num_time = NonNegative()
    __color = ["Red", "Yellow", "Green"]

    def __init__(self, red_time, yellow_time, green_time, num_time):
        self.red_time = red_time
        self.yellow_time = yellow_time
        self.green_time = green_time
        self.num_time = num_time

    def running(self):
        """
        переключает цвета светофора в соответсвии с заданными параметрами
        """
        col = [red_t, yellow_t, green_t]
        colors = dict(zip(TrafficLight.__color, col))
        i = 0
        while i < num_t:
            print("Красный")
            time.sleep(colors.get("Red"))
            print("Жёлтый")
            time.sleep(colors.get("Yellow"))
            print("Зелёный")
            time.sleep(colors.get("Green"))
            print("-------")
            i = i + 1
        print("Программа завершена")


red_t = int(input("Введите время работы красного сигнала: "))
yellow_t = int(input("Введите время работы жёлтого сигнала: "))
green_t = int(input("Введите время работы зелёного сигнала: "))
num_t = int(input("Введите количество циклов работы светофора: "))
a = TrafficLight(red_t, yellow_t, green_t, num_t)
a.running()
