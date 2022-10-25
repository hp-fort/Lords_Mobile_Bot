min1 = int(input("accel 1 min : ") * 1)
min3 = int(input("accel 3 min : ") * 3)
min5 = int(input("accel 5 min : ") * 5)
min10 = int(input("accel 10 min : ") * 10)
min15 = int(input("accel 15 min : ") * 15)
min30 = int(input("accel 30 min : ") * 30)
min60 = int(input("accel 60 min : ") * 60)
min180 = int(input("accel 3h : ") * 180)
min480 = int(input("accel 8h : ") * 480)
min900 = int(input("accel 15h : ") * 900)
min1440 = int(input("accel 24h : ") * 1440)
min4320 = int(input("accel 3j : ") * 4320)
min10080 = int(input("accel 7j : ") * 10080)
min43200 = int(input("accel 30j : ") * 43200)


min = min1+min3+min5+min10+min15+min30+min60+min180+min480+min900+min1440+min4320+min10080+min43200


def truncate_day(day, n):
    integer_day = int(day * (10**n))/(10**n)
    return int(integer_day)

day = truncate_day(min/1440, 0)

def truncate_hour(day, n):
    integer_hour = int(day * (10**n))/(10**n)
    return int(integer_hour)

min = min - day*1440

hour = truncate_hour(min/60, 0)

min = min - hour*60

print(day)
print(hour)
print(min)



if min == hour : pass
else :
    pass