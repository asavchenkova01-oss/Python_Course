colors = ["red", "green", "blue"]

for i in range(len(colors)):
    print(colors[i])

# It crashes because len(colors) is 3, and adding 1 makes the range go up to 4.
# This forces Python to look for index 3 (the 4th item), which doesn't exist,
# causing an IndexError.