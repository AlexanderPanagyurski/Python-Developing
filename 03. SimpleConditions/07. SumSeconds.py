time1 = int(input())
time2 = int(input())
time3 = int(input())

sum = time1 + time2 + time3
minutes = int(sum / 60)
seconds = sum % 60

if seconds <= 9:
    print('{0}:0{1}'.format(minutes, seconds))
else:
    print('{0}:{1}'.format(minutes, seconds))