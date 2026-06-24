students = {}
user_input = int(input("How many students?\n"))

for _ in range(user_input):
    name = input("Name: ").strip().lower()
    score = input("Score: ")
    students[name] = int(score)
    
    
print(f"{students}")
print(f"{len(students)} students recorded")

