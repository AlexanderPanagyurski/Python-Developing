import datetime

inputLine = input()
date = datetime.datetime.strptime(inputLine, "%d-%m-%Y").date()
result = date + datetime.timedelta(days=1000)

print(result.strftime("%d-%m-%Y"))
