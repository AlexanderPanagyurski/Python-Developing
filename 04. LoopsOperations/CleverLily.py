age = int(input())
laundry_price = float(input())
toy_price = int(input())

toys_count = 0
money = 0
brother = 0
even_birthdays = 0

for year in range(1, age + 1):
    if year % 2 != 0:
        toys_count += 1
    else:
        even_birthdays += 1
        brother += 1
        if year != 2:
            money += 10 * even_birthdays
        else:
            money += 10

savings = toys_count * toy_price + money - brother
diff = abs(savings - laundry_price)

if savings >= laundry_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')