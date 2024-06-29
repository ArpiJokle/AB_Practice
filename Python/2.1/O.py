import datetime
Hours = int(input())
Minutes = int(input())
Delivery = int(input())

Minutes += Delivery

Hours += int((Minutes / 60))
Minutes = int(Minutes % 60)

Hours = int(Hours % 24)

print(datetime.time(Hours, Minutes).strftime('%H:%M'))