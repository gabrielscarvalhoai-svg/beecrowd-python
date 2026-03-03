"""
Beecrowd Problem 1035 - Selection Test
Category: Beginner

This problem reads four integer values and checks whether they satisfy
a specific set of logical conditions involving comparisons, sums,
positivity, and parity.
"""


n1, n2, n3, n4 = map(int, input().split())

is_even = n1 % 2 == 0
positive_values = n3 > 0 and n4 > 0
sum_condition = (n3 + n4) > (n1 + n2)
greater_conditions = n2 > n3 and n4 > n1

if is_even and positive_values and sum_condition and greater_conditions:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
