"""
Beecrowd Problem 1016 - Distance
Category: Beginner

This problem calculates the time required for one car to get a certain
distance ahead of another, given that their speed difference is 30 km/h.

Since the faster car gains 1 km every 2 minutes, the total time in minutes
is simply twice the given distance.
"""


distance = int(input())

minutes = distance * 2

print(f'{minutes} minutos')
