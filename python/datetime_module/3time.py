import datetime

# working with time means getting past year,month,week and day 

# set time to the time ms dhoni retired 
ms_retire=datetime.time(19,49,5,234)

# print(f"MS Dhoni Retired at {ms_retire}\n")

# get hour minute second and microsecond from that time 
print(f"Ms Dhoni retired exactly at {ms_retire.hour} HR past {ms_retire.minute} minutes, {ms_retire.second} seconds and {ms_retire.microsecond} microsecond.")
