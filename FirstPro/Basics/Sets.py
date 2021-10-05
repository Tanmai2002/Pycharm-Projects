#Sets r imp becoz it retains all value only once
s=set()
s.add(1)
print(s) #{1}

s.add(2)
print(s) #{1, 2}

s.add(1)
print(s) #{1, 2}

s1=s.union({2,3})
print(s) #{1, 2}
print(s1) #{1, 2, 3}
