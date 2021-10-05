list1 = [["tanu", 12], ["Anu", 10],
         ["Manu", 51],
         ["Paanu", 16],
         ["Kanu", 1]]

for item in list1:
    print(item)
""""
['tanu', 12]
['Anu', 10]
['Manu', 51]
['Paanu', 16]
['Kanu', 1]
"""
for item, marks in list1:
    print(item, "Has got", marks)
"""
tanu Has got 12
Anu Has got 10
Manu Has got 51
Paanu Has got 16
Kanu Has got 1
"""
dict1= dict(list1)

for item in dict1:
    print (item)
""""
tanu
Anu
Manu
Paanu
Kanu
"""
#for item,marks in dict1: gives Error
for item,marks in dict1.items():
    print(item, "Has got", marks)
"""
tanu Has got 12
Anu Has got 10
Manu Has got 51
Paanu Has got 16
Kanu Has got 1
"""
#Ex:make listof anything. print only if its a number and >6
list2=[2,3,100,50,"ts0","TAnu"]
for item in list2:
    if(type(item)==int and item>6):
        print(item)
