
#1
import datetime

a = datetime.date.today()
b = a - datetime.timedelta(5)
print(b)


#2
import datetime

a = datetime.date.today()
b = datetime.timedelta(1)

print(a-b)
print(a)
print(a+b)


#3
import datetime

a = datetime.datetime.today()
print(a.strftime("%Y" + " " + "%b" + " " + "%d" + "  %H" + ":%M:%S"))


#4
import datetime

a = datetime.datetime.today()
b = datetime.datetime(1966, 5, 28)

print((a-b).total_seconds())
