import os
if not os.path.exists("Test"):
    os.mkdir("Test")
print(os.getcwd())
os.chdir("Test")
print(os.getcwd())
input()
os.mkdir("Test2")
os.rename("Test2","Test3")

print(os.listdir())
print(os.listdir("C://"))
print(os.path.join("hii","hiil","hello"))

