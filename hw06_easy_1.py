# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

def line_length(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)



class Triangle:
    def __init__(self, xy_a, xy_b, xy_c):
        self.xy_a = xy_a
        self.xy_b = xy_b
        self.xy_c = xy_c

    def triangle_area(self):
        return 0.5 * abs((self.xy_a[0] - self.xy_c[0]) *
                         (self.xy_b[1] - self.xy_c[1]) -
                         (self.xy_b[0] - self.xy_c[0]) *
                         (self.xy_a[1] - self.xy_c[1])
                         )

    def triangle_perimeter(self):
        return line_length(self.xy_a, self.xy_b) + \
               line_length(self.xy_b, self.xy_c) + \
               line_length(self.xy_c, self.xy_a)

    def triangle_height_A(self):
        return 2 * self.triangle_area() / line_length(self.xy_b, self.xy_c)

    def show_coord(self):
        return(f'А {self.xy_a}, B {self.xy_b}, C {self.xy_c}')


triangles = [Triangle([0, 0], [0, 1], [1, 1]),
             Triangle([-5, -10], [4, 7], [-2, 8],),
             Triangle([0, 2], [1, 0], [-1, 0],)
             ]

for triangle in triangles:
    print(f'Площадь треугольника с координатами {triangle.show_coord()} = ', end='')
    print(triangle.triangle_area())
    print('Высота этого треугольника из точки А = ', end='')
    print(triangle.triangle_height_A())
    print('Периметр этого треугольника = ', end='')
    print(triangle.triangle_perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
