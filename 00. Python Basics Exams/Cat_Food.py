cats_count = int(input())
small_cats_group = 0
big_cats_group = 0
large_cats_group = 0
total_food_amount = 0

for i in range(0, cats_count):
    grams_food_per_cat = float(input())
    if 100 <= grams_food_per_cat < 200:
        small_cats_group += 1
    elif 200 <= grams_food_per_cat < 300:
        big_cats_group += 1
    elif 300 <= grams_food_per_cat < 400:
        large_cats_group += 1
    total_food_amount += grams_food_per_cat

food_price_per_day = (total_food_amount / 1000) * 12.45

print(f"Group 1: {small_cats_group} cats.")
print(f"Group 2: {big_cats_group} cats.")
print(f"Group 3: {large_cats_group} cats.")
print(f"Price for food per day: {food_price_per_day:.2f} lv.")