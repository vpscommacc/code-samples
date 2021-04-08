# _*_coding: utf-8_*_
import math


class Circle:
    """Круг с радиусом, площадью и диаметром."""

    def __init__(self, radius=1):
        """
        Конструктор класса Circle

        :param token: Переменная
        :type token: int
        :rtype: int
        :return: Присвоение self.radius численного значения
        """
        self.radius = radius

    def __repr__(self):
        """
        Презентация результата

        :rtype: str
        :return: Результат в форматированном виде
        """
        return f'Circle({self.radius})'

    @property
    def area(self):
        """
        Подсчёт площади круга

        :rtype: int
        :return: Площадь круга
        """
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """
        Вычисление диаметра

        :rtype: int
        :return: Диаметр круга
        """
        return self.radius * 2

    def get_diameter(self):
        """
        Получение диаметра

        :rtype: int
        :return: Диаметр круга
        """
        return self.radius * 2

    def set_diameter(self, diameter):
        """
        Установка радиуса для круга

        :param token: Диаметр
        :type token: int
        :rtype: int
        :return: Радиус
        """
        self.radius = diameter / 2

    @property
    def radius(self):
        """
        Запись радиуса

        :rtype: int
        :return: Радиус
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """
        Проверка значения радиуса на отрицательное значение

        :param token: радиус
        :type token: int
        :rtype: str
        :return: Отказ выполнять действие
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius


# создание объекта класса и вывод результата
c = Circle(12)
print(c.area)
