money = float(input())
fromMoney = input()
toMoney = input()

converter = {
    "BGN-USD": money / 1.79549,
    "BGN-EUR": money / 1.95583,
    "BGN-GBP": money / 2.53405,
    "USD-BGN": money * 1.79549,
    "USD-EUR": money * 1.79549 / 1.95583,
    "USD-GBP": money * 1.79549 / 2.53405,
    "EUR-BGN": money * 1.95583,
    "EUR-USD": money * 1.95583 / 1.79549,
    "EUR-GBP": money * 1.95583 / 2.53405,
    "GBP-BGN": money * 2.53405,
    "GBP-USD": money * 2.53405 / 1.79549,
    "GBP-EUR": money * 2.53405 / 1.95583,
}

key = '{0}-{1}'.format(fromMoney, toMoney)
print('%.2f' % converter[key], '{0}'.format(toMoney))
