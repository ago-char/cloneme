import datetime

# it is like setting date 
date=datetime.date(2000,1,31)
print(date)

# get today's date 
t_date=datetime.date.today()
print(t_date)

# get today's year 
print(t_date.year)

# get today's month
print(t_date.month)

# get today's day 
print(t_date.day)

# get today's weekday
print(t_date.weekday()) # weekday starts with monday 0 through sunday 6

# get today's weekday as per iso standard 
print(t_date.isoweekday()) # weekday starts with monday 1 through sunday 7
