# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month,date,year=input().split() 
day=calendar.weekday(int(year),int(month),int(date))

if day==6:
    print("SUNDAY")
elif day==0:
    print("MONDA")
elif day==1:
    print("TUESDAY")
elif day==2:
    print("WEDNESDAY")
elif day==3:
    print("THURSDAY")
elif day==4:
    print("FRIDAY")
elif day==5:
    print("SATURDAY") 
