"""
Beecrowd Problem 1017 - Fuel Spent
Category: Beginner

This problem calculates the total amount of fuel required for a trip,
given the time spent driving and the average speed.

The car consumes 1 liter of fuel every 12 kilometers.
"""


time_spent = int(input())
average_speed = int(input())

total_distance = time_spent * average_speed
liters = total_distance / 12

print(f'{liters:.3f}')
