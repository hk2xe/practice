import math
import argparse


def quadratic_equation(a: int, b: int, c: int):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return "Нет корней"
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return x1, x2


parser = argparse.ArgumentParser(description='Решение квадратного уравнения')
parser.add_argument('a', type=int, help='Значение a')
parser.add_argument('b', type=int, help='Значение b')
parser.add_argument('c', type=int, help='Значение c')
args = parser.parse_args()

print(quadratic_equation(args.a, args.b, args.c))
