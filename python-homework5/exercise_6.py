words = ['potato', 'milk', 'meat', 'cookies', 'car', 'car']
user_word = input("Search for: ").strip().lower()


if user_word in words:
    print(f"Yes - '{user_word}' is on the list ({words.count(user_word)} times)")
else:
    print(f"No - '{user_word}' is not on the list")