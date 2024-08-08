import os
# cwd=os.getcwd()
# tree=os.walk(cwd)
# print(tree)

def tree_len(root):
    l=0
    for p,d,f in root:
        l+=1
    return l

tree=os.walk(os.getcwd())
print(tree_len(os.getcwd())) 

print(".............................\n")

for path,dirs,files in tree:
    print("dirpath = ",path)
    print("dirnames = ",dirs)
    print("filenames = ",files)