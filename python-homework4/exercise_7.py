# Explanation: The function crashed because 'print' only displays text on the screen and returns 'None'. 
# To use the result in a mathematical calculation, we must use 'return' to pass the actual value back.
def add(a, b):
    return a + b  

total = add(10, 5) + 100
print(f"{total = }")