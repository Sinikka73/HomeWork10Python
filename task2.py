"""
Изучение дескрипторов
"""


class NonNegative:
    """
    В этом классе атрибуты делаем дескрипторами
    """

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    """
    Расчёт массы дорожного полотна
    """
    length = NonNegative()
    width = NonNegative()
    thickness = NonNegative()

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness

    def calculation(self):
        """
        Масса покрытия дороги длиной 5000м, шириной 20м, заданной толщиной
        """
        weigth = 0.025
        print("Принимаем расход асфальта на покрытие 1кв.м - 25кг")
        calc = self._length * self._width * weigth * self.thickness / 100
        print(f'Для покрытия дороги длиной 5000м, шириной 20м, '
              f'толщиной {self.thickness} cм '
              f'необходимо  {round(calc)}т. асфальта')


thick = int(input("Введите толщину дорожного "
                  "полотна в сантиметрах: "))
asphalt_weight = Road(5000, 20, thick)

asphalt_weight.calculation()