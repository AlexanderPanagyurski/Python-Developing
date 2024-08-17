month = input()
spent_hours_count = int(input())
group_people_count = int(input())
time_of_day = input()

price_per_person = 0
total_cost = 0

if time_of_day == "day":
    if month == "march" or month=="april" or month == "may":
        price_per_person = 10.5
    elif month == "june" or month == "july" or month == "august":
        price_per_person = 12.6
elif time_of_day == "night":
    if month == "march" or month == "april" or month == "may":
        price_per_person = 8.4
    elif month == "june" or month == "july" or month == "august":
        price_per_person = 10.2

if group_people_count >= 4:
    price_per_person = price_per_person * 0.9

if spent_hours_count >= 5:
    price_per_person = price_per_person * 0.5

print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {(price_per_person * spent_hours_count * group_people_count):.2f}")
