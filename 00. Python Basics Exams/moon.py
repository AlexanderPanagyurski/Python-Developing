import math

average_speed = float(input())
liters_fuel_per_hundred_km = float(input())

total_distance = 384400 * 2
travel_time = math.ceil(total_distance / average_speed)

overall_time = travel_time + 3
fuel = (liters_fuel_per_hundred_km * total_distance)/100

print(overall_time)
print(f"{fuel:.0f}")
