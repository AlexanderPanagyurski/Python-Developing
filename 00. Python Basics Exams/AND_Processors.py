import math

needed_processors_count = int(input())
employees_count = int(input())
work_days = int(input())

total_worked_hours = employees_count * work_days * 8
produced_processors = math.floor(total_worked_hours / 3)

if produced_processors < needed_processors_count:
    diff = needed_processors_count - produced_processors
    print(f"Losses: -> {(diff * 110.10):.2f} BGN")
else:
    diff = produced_processors - needed_processors_count
    print(f"Profit: -> {(diff*110.10):.2f} BGN")
