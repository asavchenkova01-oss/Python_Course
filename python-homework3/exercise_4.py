n = int(input("Add up to:\n"))

total = 0 

for i in range(1, n + 1):
    total += i
print(f"The sum of 1 to {n} is {total}")