import os

# create file 
os.mknod('newfile')
# rename file 
os.rename('newfile','tsf')
# remove file 
os.remove('tsf')

# create folder 
os.mkdir('temp')
# rename folder 
os.rename('temp','tmp')
# remove folder
os.rmdir('tmp')