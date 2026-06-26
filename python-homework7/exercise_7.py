numbers = [1, 2, 3, 4, 5, 6]

doubled = [n * 2 for n in numbers]
print(doubled)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

squares_dict = {n: n * n for n in numbers}
print(squares_dict)