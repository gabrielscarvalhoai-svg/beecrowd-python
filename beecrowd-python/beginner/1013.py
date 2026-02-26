"""
Beecrowd Problem 1013 - The Greatest
Category: Beginner
This script reads three integer values and determines the largest one using the formula: (a + b abs(a - b)) / 2.
"""


# Reading the input and unpacking the list into three variables
# We use map(int, ...) for a slightlty cleaner conversion
a, b, c = map(int, input().split())

# Function to find the greatest between two numbers using the required formula
def find_greatest(num1, num2):
    return int((num1 + num2 + abs(num1 - num2)) / 2)

# Fist, find the greatest between 'a' and 'b'
# Then, compare the result with 'c'
greatest_ab = find_greatest(a, b)
final_result = find_greatest(greatest_ab, c)

print(f'{final_result} eh o maior')
