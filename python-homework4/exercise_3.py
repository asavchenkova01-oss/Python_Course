def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80 and score <= 89:
        return "B"
    if score >= 70 and score <= 79:
        return "C" 
    return "F"

score = int((input("Enter your score:\n")))
print(f"Score {score} -> grade {letter_grade(score)}")
