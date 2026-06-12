def count_vowels(word):
    counter = 0
    for char in word.lower():
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            counter += 1
    return counter


word = input("Enter a word:\n").strip()
vowel_count = count_vowels(word)
print(f"'{word}' has {vowel_count} vowels.")





