"""
Beecrowd Problem 1018 - Banknotes
Category: Beginner

This problem reads an integer value and determines the minimum number
of banknotes needed to represent that amount using the available denominations.
"""


# Greedy approach: always use the largest possible banknote first
money_notes = [100, 50, 20, 10, 5, 2, 1]


value = int(input())

print(value)
for banknote in money_notes:
    quantity = value // banknote
    value %= banknote
    print(f'{quantity} nota(s) de R$ {banknote},00')
