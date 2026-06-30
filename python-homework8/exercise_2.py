from random import randint, choice

dice_roll = randint(1, 6)

food_options = ["pizza", "khinkali", "salad"]
dinner_choice = choice(food_options)

print(f"You rolled a {dice_roll}")
print(f"Tonight: {dinner_choice}")