# read 
# readline
# readlines

with open('file.txt','r') as f:
    content=f.read()
    print(content)

print("............................")

with open('file.txt','r') as f:
    content=f.read(10)
    print(content)

print("............................")

with open('file.txt','r') as f:
    content='x'
    while content:
        content=f.read(10)
        if content:
            print(content,end='&')
    print()
