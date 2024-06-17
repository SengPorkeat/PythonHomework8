from datetime import datetime,timedelta,date
import time

def calculateBirthDate(birthDate):
    today = date.today()
    age = today - birthDate
    return age

inputBirthDate = date(day=4,month=9,year=2004)
age = calculateBirthDate(inputBirthDate).days
print("Days:",age)

def convertAgeToYear(age):
    return age // 365

ageInYear = convertAgeToYear(age)
print("Age:",ageInYear)

def calculateFutureDate(duration):
    return datetime.now() + duration
futureEvent = timedelta(days=10,hours=5,minutes=10)
futureDay =  calculateFutureDate(futureEvent)
print(futureDay.strftime("%d/%B/%Y - %I:%M:%S %p"))