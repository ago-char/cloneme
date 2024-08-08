with open('doc.dat','w') as f:
    l=[1,3,4,6,3]
    bytes_written=f.write(str(l))
    print(f"{bytes_written} bytes written.")
