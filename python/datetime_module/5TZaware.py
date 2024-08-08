import datetime
import pytz

def isZoneAvl(tzone):
    '''
    return list of alike timezones if matches else return None
    '''
    if not isinstance(tzone,str):
        return None
    zone_list=[]
    for tz in pytz.all_timezones:
        if tzone.lower() in tz.lower():
            zone_list.append(tz)
    return zone_list

# datetime.datetime.now() is timezone aware if you pass in tz 
# getting utc timezone and kathmandu,nepal timezones' time 
t_utc=datetime.datetime.now(tz=pytz.timezone(str(isZoneAvl('UTC')[0])))
t_nep=datetime.datetime.now(tz=pytz.timezone(str(isZoneAvl('Kathmandu')[0])))
t_none=datetime.datetime.now(tz=pytz.timezone(None))
print(t_utc)
print(t_nep)
print(t_none)