import json

class NoteBook:
    def __init__(self):
        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def display_notes(self):
        print(f"You have {len(self.notes)} note(s).")
        for index, note in enumerate(self.notes, start=1):
            print(f"{index}. {note}")

    def add(self, note):
        self.notes.append(note)
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)
        print("Saved!")

notebook = NoteBook()

notebook.display_notes()

new_note = input("Add a note: ")

notebook.add(new_note)