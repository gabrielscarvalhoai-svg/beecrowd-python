"""
Beecrowd Problem 1040 - Average 3
Category: Beginner

This problem reads four floating-point grades and calculates
a weighted average using the weights 2, 3, 4, and 1.

Based on the average:
- If the result is greater than or equal to 7.0, the student is approved.
- If the result is less than 5.0, the student is failed.
- Otherwise, the student must take an additional exam.

If an exam is required, the exam grade is read, a new average is
calculated, and the student's final status is determined.
"""


def exam(average):
    print('Aluno em exame.')
    exam_grade = float(input())
    print(f'Nota do exame: {exam_grade:.1f}')

    new_average = (average + exam_grade) / 2

    if new_average >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {new_average:.1f}')


n1, n2, n3, n4 = map(float, input().split())

average = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f'Media: {average:.1f}')
if average < 5.0:
    print('Aluno reprovado.')
elif average <= 6.9:
    exam(average)
else:
    print('Aluno aprovado.')
