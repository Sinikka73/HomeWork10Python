"""
Создать метакласс для паттерна Синглтон
"""


class Singleton(type):
    """
    Изучение синглтона
    """
    a = None

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super().__call__(*args, **kwargs)
        return cls.a


class Stationery:
    """
    Канцелярия
    """

    def __init__(self, title):
        self.title = title

    def draw(self):
        """
        :return: отрисовка
        """
        print("Отрисовка")


class Pen(Stationery, metaclass=Singleton):
    def draw(self):
        """
        :return: text
        """
        return "ручка"


class Handle(Stationery, metaclass=Singleton):
    def draw(self):
        """
        :return: text
        """
        return "маркер"


pen = Pen('pen')
red_pen = Pen('red_pen')
green_pen = Pen('green_pen')

print(pen.draw(), "", red_pen.draw(), pen is red_pen)
print(red_pen.draw(), "", green_pen.draw(), red_pen is green_pen)

red_handle = Handle('red Handle')
green_handle = Handle('green handle')

print(red_handle.draw(), '', green_handle.draw(), red_handle is green_handle)
print(red_pen.draw(), "", red_handle.draw(), red_pen is red_handle)