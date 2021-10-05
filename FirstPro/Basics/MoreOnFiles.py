f=open("text.txt")
print(f.readline())#tanmai is kind
print(f.tell())#16
print(f.readline())#tanmai is vey bad
print(f.tell())#35
print(f.readline())#tanmai is king
print(f.tell())#49
print(f.readline())# print Nothing
print(f.tell())#49
f.seek(0) # moves pointer to 0 postion of file
print(f.readline())#tanmai is kind
print(f.tell())#16
f.close()

#Using with for reading/writng - Note no f.close req
with open("text.txt") as f:
    print(f.readline()) #tanmai is kind