word = input("Type a word:\n").strip().lower()

counter = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        counter += 1

print(f"'{word}' has {counter} vowel(s) out of {len(word)} letters.")