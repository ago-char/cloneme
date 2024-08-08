import datetime

# time delta is simply the difference between two dates/times 
# date1+time_delta=date2

# for eg. you wanna know the date after 21 days today, you can't simply add 21 to today's date as 'datetime.date' + 'int' is not defined, well you could create such method but there is much simpler way 
# after_21_days=datetime.date.today()+20 # error

# get today date 
today=datetime.date.today()

# set time delta to 21 days 
t_delta=datetime.timedelta(days=21)

# now get the date after 21 days 
print(today+t_delta)

# instead you could set time delta to 3 weeks too 
t_delta=datetime.timedelta(weeks=3)
print(today+t_delta)


# you can also calculate timedelta by subtracting 2 dates 
new_year=datetime.date(2025,1,1)
tday=datetime.date.today()

print(f"..........................\n{(new_year-tday).days} days to go for the New Year 2025.\n" )
