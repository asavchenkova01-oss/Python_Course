def high_and_low(numbers):
    biggest = numbers[0]
    smallest = numbers[0]

    for n in numbers:
        if n > biggest:
            biggest = n
        if n < smallest:
            smallest = n

    return biggest, smallest

scores = [45, 54, 87, 6789, 1, 2, 345]

high, low = high_and_low(scores)

print(f"highest: {high}")
print(f"lowest: {low}")   
    
