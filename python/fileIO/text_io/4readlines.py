with open('file.txt','r') as f:
    cont=f.readlines()
    print(cont)

print(".......................")

with open('file.txt','r') as f:
    # hint=34 means don't read more lines if 34 bytes of chuck is already read, remember it does not mean to read 34 bytes only. so first is read a line and then see if it exceed 34 bytes, if then return else go read next line and then repeat the same
    cont=f.readlines(34)
    print(cont,end='&')
    print()

print("............................")

with open('file.txt','r') as f:
    while cont:
        cont=f.readlines(12)
        if cont:
           print(cont,end='&')
    print()
