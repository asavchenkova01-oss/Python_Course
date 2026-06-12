number = int(input("Enter a number:\n"))

def is_even (n):
    return number % 2 == 0
    
if is_even(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")