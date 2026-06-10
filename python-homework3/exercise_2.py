score = int((input("Your score:\n")))

if score >= 90:
    print("Your grade is A")
elif score >= 80 and score <= 89:
    print("Your grade is B")
elif score >= 70 and score <= 79:
    print("Your grade is C")
else: 
    print("Your grade is F")