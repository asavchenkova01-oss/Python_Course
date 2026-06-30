import json

profile = {
    "name": "Anastasia",
    "age": 25,
    "hobbies": ["coding", "reading", "gaming"]
}

with open("me.json", "w") as f:
    json.dump(profile, f)
print("Saved me.json")

with open("me.json", "r") as f:
    data = json.load(f)

print(f"Loaded back: {data['name']}, age {data['age']}, hobbies {data['hobbies']}")