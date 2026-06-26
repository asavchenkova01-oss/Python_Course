text = input("Type a number: ")

try:
    number = int(text)
except ValueError:
    print(f"'{text}' is not a number.")
else:
    double = number * 2
    print(f"Double is {double}.")