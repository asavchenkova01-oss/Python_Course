try:
    with open("notes.txt", "r") as f:
        notes = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    notes = []

print(f"You have {len(notes)} note(s).")
for index, note in enumerate(notes, 1):
    print(f"{index}. {note}")

new_note = input("Add a note: ")

with open("notes.txt", "a") as f:
    f.write(new_note + "\n")

print("Saved!")