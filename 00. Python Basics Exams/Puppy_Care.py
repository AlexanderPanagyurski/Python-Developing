dog_food_kilos_amount = int(input())

text = input()

dog_food_grams_amount = dog_food_kilos_amount * 1000
total_food = 0

while text != "Adopted":
    food_kilos_per_meal = int(text)
    total_food += food_kilos_per_meal
    text = input()

if dog_food_grams_amount >= total_food:
    print(f"Food is enough! Leftovers: {dog_food_grams_amount - total_food} grams.")
else:
    print(f"Food is not enough. You need {total_food - dog_food_grams_amount} grams more.")
