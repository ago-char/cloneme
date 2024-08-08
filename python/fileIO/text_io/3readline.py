with open('file.txt','r') as f:
    cont=f.readline()

print(".....................")

# reading 'chunk' chunk of data 
chunk=3

with open('file.txt','r') as f:
    cont=f.readline(chunk)
    print(cont)

print(".....................")

with open('file.txt','r') as f:
    while cont:
        cont=f.readline(chunk)
        if cont:
            print(cont,end='&')
    print()