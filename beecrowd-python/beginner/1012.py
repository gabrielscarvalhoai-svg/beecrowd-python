"""
Beecrowd Problem 1012 - Area
Category: Beginner

This script reads there floating-point values (A, B and C) and calculates
the areas of five geometric shapes based on specific formulas.
"""


# Constants
PI = 3.14159


# Reading input values
# A, B, and C represent, dimensions used across different calculations
a, b, c = map(float, input().split())

# Geometric Calculations:
# 1. Right-angles triangle (base: A, height: C)
triangle_area = (a * c) / 2

# 2. Circule (radius: C)
circle_area = PI * (c ** 2)

# 3. Trapezium (bases: A and B, height: C)
trapezium_area = ((a + b) * c) / 2

# 4. Square (side: B)
square_area = b ** 2

# 5. Rectangle (side: A and B)
rectangle_area = a * b

# Output formatting:
# The exercise requires Portuguese labels with 3 decimal places.
print(f'TRIANGULO: {triangle_area:.3f}')
print(f'CIRCULO: {circle_area:.3f}')
print(f'TRAPEZIO: {trapezium_area:.3f}')
print(f'QUADRADO: {square_area:.3f}')
print(f'RETANGULO: {rectangle_area:.3f}')
