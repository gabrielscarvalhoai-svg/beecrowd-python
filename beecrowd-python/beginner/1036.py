"""
Beecrowd Problem 1036 - Bhaskara's Formula
Category: Beginner

This problem reads three floating-point values (A, B, and C)
and calculates the roots of a quadratic equation using
Bhaskara's formula.

If A is zero or the discriminant (delta) is negative,
it is impossible to calculate the real roots.

The results must be printed with five digits after
the decimal point.
"""


from math import sqrt


def calculate_roots(a, b, delta):
    root = sqrt(delta)
    r1 = (-b + root) / (2 * a)
    r2 = (-b - root) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')


a, b, c = map(float, input().split())

delta = (b ** 2) - (4 * a * c)

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    calculate_roots(a, b, delta)
