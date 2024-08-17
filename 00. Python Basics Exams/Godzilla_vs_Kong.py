movie_budget = float(input())
statists_count = int(input())
suit_price = float(input())

movie_deckor_price = movie_budget * 0.1
statists_suits_price = statists_count * suit_price

if statists_count > 150:
    statists_suits_price = statists_suits_price - statists_suits_price * 0.1

overall_price = movie_deckor_price + statists_suits_price

if overall_price > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {(overall_price - movie_budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(movie_budget - overall_price):.2f} leva left.")
