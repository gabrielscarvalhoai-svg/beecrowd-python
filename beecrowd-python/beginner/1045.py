"""
Beecrowd Problem 1045 - Triangle Types
Category: Beginner

This problem reads three floating-point values representing
the lengths of three line segments.

The values are first sorted in descending order to simplify
the triangle classification.

The program determines:
- whether the segments form a triangle
- the type of triangle based on its angles
  (right, obtuse, or acute)
- the type based on its sides
  (equilateral or isosceles)
"""


a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:

    a2, b2, c2 = a * a, b * b, c * c

    if a2 == (b2 + c2):
        print('TRIANGULO RETANGULO')
    elif a2 > (b2 + c2):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOSCELES')
