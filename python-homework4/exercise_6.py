def door_decision(name, age):
    if age < 18:
        return "Sorry, no entry."
    if age >= 21 and name == "nino":
        return "Welcome, VIP!"
    if age % 2 == 0 or name == "giorgi":
        return "Welcome! Free drink for you!"
    return "Welcome!"

name = input("What's your name?\n").strip().lower()
age = int(input("How old are you?\n"))

print(f"{door_decision(name, age)}")