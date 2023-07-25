from dateutil.relativedelta import *
from datetime import date #pip install python-dateutil

userTF = str(input("Enter your Date Of Birth in dd/mm/yyyy format : "))
dd,mm,yyyy = userTF.split('/')

TODAY = date.today()
userBirthday = date(int(yyyy),int(mm),int(dd))

age = relativedelta(TODAY, userBirthday)
print(f"{age.years} years {age.months} months {age.days} days old")
print(f"{(age.years *12) + age.months} months {age.days} days old")
print(f"{round(((age.years *12) + age.months)*30.4368)+age.days} days old")