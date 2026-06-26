shopping_list = ["bread", "milk", "eggs", "coffee"]

with open("shopping.txt", "w") as f:
    for item in shopping_list:
        f.write(item + "\n")

print(f"Wrote {len(shopping_list)} items to shopping.txt")