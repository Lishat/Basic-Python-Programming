import time
import calendar
print("calendar.calendar(2013, 2, 1, 6) is\n",calendar.calendar(2013, 2, 1, 6))
print("calendar.firstweekday() is", calendar.firstweekday())
print("calendar.isleap(2016) is",calendar.isleap(2016))
print("calendar.leapdays(2000, 2016) is",calendar.leapdays(2000, 2016))
print("calendar.month(2016, 4, 2, 1)", calendar.month(2016, 4, 2, 1))
print("calendar.monthcalendar(2016, 10) is\n",calendar.monthcalendar(2016, 10))
print("calendar.prcal(2016, 2, 1, 6) is",calendar.prcal(2016, 2, 1, 6)) #works like calendar.calendar but returns None at last
print("calendar.prmonth(2016, 4, 2, 1) is", calendar.prmonth(2016, 4, 2, 1))#works like calendar.month but returns None at last
calendar.setfirstweekday(6)
print("calendar after setting firstday", calendar.calendar(2016))
print("calendar.timegm((2009, 11, 5, 12, 30, 16)) is",calendar.timegm((2009, 11, 5, 12, 30, 16)))
print("calendar.weekday(2017, 4, 6) is",calendar.weekday(2017, 4, 6)) #returns the day of week as an integer
