import datetime


# set birthdate
birthdate=datetime.date(2000,1,1)
print(birthdate)

# set time 
birthtime=datetime.time(13,5,12,8888)
print(birthtime)

# set both birthdate and birthdate at once
birth_datetime=datetime.datetime(2000,1,1,13,5,12,8888)
print(birth_datetime)

print("........................................\n")

dt_today=datetime.datetime.today() # you can not set TZ info (timezone info)
dt_now=datetime.datetime.now() # you can set TZ info (if not set the result are similar to today())
dt_utcnow=datetime.datetime.utcnow() # you can not set TZ but it provides datetime based on ntc TZ

print(dt_today) 
print(dt_now)   
print(dt_utcnow)