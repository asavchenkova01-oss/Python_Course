scores = {"irakli": 90, "sandro": 89}

search = input("Whose score?\n")

try:
    score = scores[search]
except KeyError:
    print(f"No score recorded for {search}")
else:
    print(f"{search}'s score is {score}")