"""
Beecrowd Problem 1046 - Game Time
Category: Beginner

This problem reads the start and end times of a game in hours.

The program calculates the duration of the game, considering
that it may span across midnight.

If the start and end times are the same, the duration is 24 hours.
"""


start_time, end_time = map(int, input().split())

if start_time == end_time:
    duration = 24
elif start_time > end_time:
    duration = (24 - start_time) + end_time
else:
    duration = end_time - start_time

print(f'O JOGO DUROU {duration} HORA(S)')
