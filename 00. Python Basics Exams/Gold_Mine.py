locations_count = int(input())

for i in range(0, locations_count):
    expected_average_gold_yild_per_day = float(input())
    yilding_days_count = int(input())
    average_gold_per_day = 0
    for i in range(0, yilding_days_count):
        yilded_gold_for_the_day = float(input())
        average_gold_per_day += yilded_gold_for_the_day
    average_gold_per_day = average_gold_per_day / yilding_days_count
    if average_gold_per_day >= expected_average_gold_yild_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(f"You need {(expected_average_gold_yild_per_day - average_gold_per_day):.2f} gold.")
    average_gold_per_day = 0
