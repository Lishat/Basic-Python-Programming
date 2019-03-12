import time
import calendar
import os
print("ticks:", time.time());
print("Time structure", time.localtime(time.time()))
print("Local Current time:", time.asctime(time.localtime(time.time())));
print("Calendar:", calendar.month(2008, 1));
#time.sleep(2.5)
print("time.altzone is",time.altzone);
print("time.asctime(time.localtime()) is",time.asctime(time.localtime()))
print("time.clock() is", time.clock())
print("time.ctime(100000000000) is", time.ctime(100000000000))
print("time.gmtime(15000) is", time.gmtime(15000))
print("time.mktime(time.localtime(time.time())) is", time.mktime(time.localtime(time.time())))
print("time.strftime('%a %A %b %B %c %C %d %D %e %g %G %h %H %I %j %m %M %n %p %r %R %S %t %T %u %U %V %W %w %x %X %y %Y %Z') is", time.strftime("%a\n%A\n%b\n%B\n%c\n%C\n%d\n%D\n%e\n%g\n%G\n%h\n%H\n%I\n%j\n%m\n%M\n%n\n%p\n%r\n%R\n%S\n%t\n%T\n%u\n%U\n%V\n%W\n%w\n%x\n%X\n%y\n%Y\n%Z"))
print("time.strptime('30 Nov 00', '%d %b %y') is", time.strptime("30 Nov 00", "%d %b %y"))
os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print("time.strftime('%X %x %Z') when time.tzset() is", time.strftime('%X %x %Z'))
print("time.tzname is", time.tzname)
print("time.timezone is",time.timezone)
