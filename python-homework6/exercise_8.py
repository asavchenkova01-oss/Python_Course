scores = {"nino": 90, "giorgi": 75}

name = "luka"
print(f"{name}'s score is {scores.get(name, 0)}")

# crashed because there is no value 
# with key 'luka' to find in the dictionary

# the fix '{scores.get(name, 0)}' gives us value "0" 
# in case no such key is found