import os

# print all environment variables
# print(os.environ)

# get specified env 
homedir=os.environ.get('HOME')
# print(homedir)
path=os.environ.get('PATH')
# print(path)

filename='file.c'

currdir=os.getcwd()

# get full path of file.c in currentdir 
# join currdir with filename 
abs_path=currdir+'/'+filename
print(abs_path)

# use join instead 
absloute_path=os.path.join(currdir,filename)
print(absloute_path)
print("...............\n")
# os.path.basename
# os.path.dirname
# os.path.exists
# os.path.isdir
# os.path.isfile
# os.path.split
# os.path.splitext