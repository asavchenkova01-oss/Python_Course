items = []
items_q = int(input("How many items?"))

for item in range(items_q):
    items.append(input("Item: "))

print(f"You added {len(items)} items.")
print(f"{items} =")