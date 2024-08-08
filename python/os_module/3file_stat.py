import os 
from datetime import datetime

# get file stat 
readme_stat= os.stat('readme.md')

# this will result something like following if you do    print(readme_stat)
'''
os.stat_result(st_mode=33188, st_ino=2824, st_dev=2080, st_nlink=1, st_uid=1000, st_gid=1000, st_size=448, st_atime=1722067459, st_mtime=1722067459, st_ctime=1722067459)
'''

# you can print any of those (i will print size in bytes)
print(f"Size of 'readme.md' = {readme_stat.st_size}")

# now last modification time (will be in timestamp format)
mod_time=readme_stat.st_mtime

print(f"Last modified (timestamp) = {mod_time}")

# convert that timestamp into standard form 
standard_mod_time=datetime.fromtimestamp(mod_time)

print(f"Last modified (standard) = {standard_mod_time}")