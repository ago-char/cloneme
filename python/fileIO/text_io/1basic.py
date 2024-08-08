file=open('doc.dat','r')

print(f"Reading '{file.name}'........\n")
content=file.read()
print(content)
file.close()