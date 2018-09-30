# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, A: Point, B: Point):
        self.A = A
        self.B = B

    def line_length(self, other):
        return math.sqrt((other[0] - self[0]) ** 2 + (other[1] - self[1]) ** 2)

class Trapezoid:
    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def trapez_lines(self):
        tr_ln_ab_left_side = Line.line_length(self.a, self.b)
        tr_ln_bc_top = Line.line_length(self.b, self.c)
        tr_ln_cd_right_side = Line.line_length(self.c, self.d)
        tr_ln_da_bottom = Line.line_length(self.d, self.a)
        return tr_ln_ab_left_side, tr_ln_bc_top, tr_ln_cd_right_side, tr_ln_da_bottom

    def equilateral_trapez(self):
        return Line.line_length(self.a, self.b) == Line.line_length(self.c, self.d)

    def trapez_area(self):
        return (Line.line_length(self.b, self.c) + Line.line_length(self.d, self.a)) / 2 * \
               math.sqrt(Line.line_length(self.a, self.b) ** 2 - (Line.line_length(self.b, self.c) \
               - Line.line_length(self.d, self.a)) ** 2 / 4)

    def trapez_perimeter(self):
        return Line.line_length(self.a, self.b) + \
               Line.line_length(self.b, self.c) + \
               Line.line_length(self.c, self.d) + \
               Line.line_length(self.d, self.a)

    def show_coord(self):
        return(f'А {self.a}, B {self.b}, C {self.c}, D {self.d}')


trapezoids = [Trapezoid([0, 0], [1, 2], [3, 2], [4, 0]),
             Trapezoid([-5, -10], [4, 7], [-2, 8], [-10, 0]),
             Trapezoid([-2, 4], [2, 2], [3, -1], [1, -5])
             ]

for trapez in trapezoids:
    print('-' * 100)
    print(f'Трапеция с координатами {trapez.show_coord()} - ', end='')
    if trapez.equilateral_trapez():
        print(' равнобедренная.')
        print(f'Площадь трапеции = ', end='')
        print(trapez.trapez_area())
        print('Длина сторон: AB, BC, CD, DA:')
        print(trapez.trapez_lines())
        print('Периметр этой трапеции = ', end='')
        print(trapez.trapez_perimeter())
    else:
        print(' неравнобедренная.')
