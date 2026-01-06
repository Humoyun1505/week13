import datetime as dt

year = int(input("Enter exam year: "))
month = int(input("Enter exam month: "))
day = int(input("Enter exam day: "))
exam_date = dt.date(year, month, day)
today = dt.date.today()
difference = exam_date - today
days = difference.days

if days > 0:
    print(f"You have {days} days left to study!")
elif days == 0:
    print("Good luck! The exam is today.")
else:
    print(f"The exam was {abs(days)} days ago.")
