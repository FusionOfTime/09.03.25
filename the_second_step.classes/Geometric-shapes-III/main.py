# S = a * b
# P = (a + b) * 2
"""
Модуль для вычисления площади и периметра прямоугольника.
"""
class Rectangle:
    """
    Класс для представления прямоугольника на плоскости.

    Атрибуты:
        x1 (float): Координата x первой вершины.
        y1 (float): Координата y первой вершины.
        x2 (float): Координата x второй вершины.
        y2 (float): Координата y второй вершины.
    """
    def __init__(self, x1, y1, x2, y2):
        """
        Инициализирует объект Rectangle.

        Args:
            x1 (float): Координата x первой вершины.
            y1 (float): Координата y первой вершины.
            x2 (float): Координата x второй вершины.
            y2 (float): Координата y второй вершины.
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def rectangle_square(self):
        """
        Вычисляет площадь прямоугольника.

        Returns:
            float: Площадь прямоугольника.
        """
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width * height

    def rectangle_perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Returns:
            float: Периметр прямоугольника.
        """
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return 2 * (width + height)

def main():
    """
    Основная функция программы.
    Читает координаты двух вершин прямоугольника,
    вычисляет его площадь и периметр,
    и выводит результаты.
    """
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())

    rect = Rectangle(x1, y1, x2, y2)
    square = rect.rectangle_square()
    perimeter = rect.rectangle_perimeter()

    print(f"{square:.6f}\n{perimeter:.6f}")

if __name__ == '__main__':
    main()