""""
"r" - for reading(default)
"w" -for writing
"x" - create file if it doesnot Exist
"a" - add more content to file
"t" - text mode(default)
"b" - binaryMode
"+" -read and write
"""

#Reading a file

#/////////////////
f= open("text.txt")
cont=f.read()
print(cont)
"""
tanmai is kind
tanmai is vey bad
tanmai is king
"""
cont1=f.read()
print(cont1)
#prints Nothing
f.close()
#/////////////////

#using for
f= open("text.txt")
for line in f:
    print(line)
    """
    
tanmai is kind

tanmai is vey bad

tanmai is king
    
    """
cont1=f.read()
print(cont)
"""
tanmai is kind
tanmai is vey bad
tanmai is king
"""
#thus its better to use for line in when working with files instead of read

f.close()

#ReadLine function allows to read one line each
