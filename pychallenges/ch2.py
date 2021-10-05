l=list(i for i in 'abcdefghijklmnopqrstuvwxyz')
stri=""
with open("t2.txt",'r') as f:
    for line in f:
        stri=stri+"".join(list(map(lambda i:i if l.__contains__(i) else "",line)))

print(stri)