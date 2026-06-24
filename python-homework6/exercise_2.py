phone = {'luka': '555-123', 'nino':'782-836469','giorgi': '293-38972'}

name = input("Whose number?\n").strip().lower()

if name in phone:
    print(f"{name}'s number is {phone[name]}")
else:
    print(f"Sorry, {name} is not in the phonebook")