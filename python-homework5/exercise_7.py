grades = [90, 45, 65, 78.4, 69]
grades_1 = [10, 10, 20]

def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print(round(average(grades), 1))
print(round(average(grades_1), 1))