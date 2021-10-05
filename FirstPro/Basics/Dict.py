d1={"abhi":1,"tanu":2,"zanu":3}
print(d1) #{'abhi': 1, 'tanu': 2, 'zanu': 3}

d3=d1
d3.pop("zanu")
print(d1) #{'abhi': 1, 'tanu': 2}
print(d3) #{'abhi': 1, 'tanu': 2}

d1.update({"ketam":12})
print(d1) #{'abhi': 1, 'tanu': 2, 'ketam': 12}

d3=d1.copy()
d3.pop("abhi")
print(d1) #{'abhi': 1, 'tanu': 2, 'ketam': 12}
print(d3) #{'tanu': 2, 'ketam': 12}

print(d1.keys()) #dict_keys(['abhi', 'tanu', 'ketam'])

print(d1.items()) #dict_items([('abhi', 1), ('tanu', 2), ('ketam', 12)])