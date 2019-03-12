import time
import calendar
print("ticks:", time.time());
print("Time structure", time.localtime(time.time()))
print("Local Current time:", time.asctime(time.localtime(time.time())));
print("Calendar:", calendar.month(2008, 1));

