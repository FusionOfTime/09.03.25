# √((хА – хВ)² + (уА – уВ)²
"""
Этот модуль содержит функции для расчета
расстояния между точками.
"""
import math
class Point:
    """
        Представляет точку на плоскости с координатами x и y.
    """
    def __init__(self, x, y):
        """
               Инициализирует новый объект Point.

               Args:
                   x (float): Координата x точки.
                   y (float): Координата y точки.
               """
        self.x = x
        self.y = y
    def distance_ptr(self, other):
        """
                Вычисляет расстояние между текущей точкой и другой точкой.

                Args:
                    other (Point): Другая точка, до которой вычисляется расстояние.

                Returns:
                    float: Расстояние между двумя точками.
                """
        return math.sqrt((math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)))
def main():
    """
       Основная функция, которая считывает координаты двух точек,
       вычисляет расстояние между ними и выводит результат.
    """
    x1, y1, = map(float, input().split())
    x2, y2 = map(float, input().split())
    a = Point(x1, y1)
    b = Point(x2, y2)
    answer = Point.distance_ptr(a, b)
    print(f"{answer:.6f}")

if __name__ == '__main__':
    main()