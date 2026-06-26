with open("shopping.txt", "r") as f:
    count = 0 

    for line in f:
        print(f"- {line.strip()}")
        count += 1

print(f"{count} items total")
