"""
Beecrowd Problem 1038 - Snack
Category: Beginner

This problem reads an item code and a quantity,
then calculates the total amount to be paid based
on a predefined menu.

Each item code corresponds to a specific price,
and the result must be printed with two decimal places.
"""


menu = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}


code, quantity = map(int, input().split())

total = menu[code] * quantity

print(f'Total: R$ {total:.2f}')
