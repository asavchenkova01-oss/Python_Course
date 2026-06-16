numbers = [5, 78, 4, 9, 12, 24, 30]
evens = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(f"Original: {numbers}")
print(f"Evens: {evens}")