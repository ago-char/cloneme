import os

# find any obj inside os module 
# print(dir(os))

# name the operating system 
print("OS In Work : ",os.name)

# print current working direcotry 
# print("CurrentWorkingDirectory : ",os.getcwd())

# os.curdir is just string value of current directory 
# print("CWD : ",os.curdir)

# change directory to parent directory
os.chdir('..')
print(os.getcwd())

# create directory on current position # remember dir was changed 
# os.mkdir('os_helper')

# remove that os_helper directory 
# os.rmdir('os_helper')

# create directory in tree level 
os.makedirs('os_helper/test')

# remove tree level directorys (note: it removes all dir/subdirs in path listed so be careful )


# list the directory 
# if no path is passed it will take current path and return all files/directory in current path
print(os.listdir())
