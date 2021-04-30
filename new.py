
# # a = list(range(1,100))
# # print(a)
# # total2 = 0
# # for e in range(1,100):
# #     if e % 3 == 0:
# #         total2 = total2 + e
# # print(total2)
# # total = 0
# # for elements in a :
# #     total1 = total + elements
# #     print(total)
# a = [1,2,3,-2,-3,-4,2, -6, -8]
# b = 0
# c = 0
# while a[c] > 0 :
#     b = b + a[c]
#     c = c - 1
# print(b)
#
# import time ,  calendar
# from datetime import date
# cal = calendar.month(2021, 12)
# print ("Here is the calendar:")
# print (cal)
# print(date.today())
# from datetime import datetime
# from pytz import timezone
#
# format = "%Y-%m-%d %H:%M:%S %Z%z"
#
# # Current time in UTC
# now_utc = datetime.now(timezone('UTC -3 '))
# print (now_utc.strftime(format))
# while True:
#     localtime = time.asctime( time.localtime(time.time()) )
#
#     print ("\r Local current time :", localtime, end = '')
a = [1,2,3,2,1,4,]
b = []
for elements in a :
    if elements not in b:
        b.append(elements)
    else:
        print(elements)