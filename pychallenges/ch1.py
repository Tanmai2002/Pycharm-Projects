l=list(i for i in 'abcdefghijklmnopqrstuvwxyz')
l2=list(i for i in 'cdefghijklmnopqrstuvwxyzab')
inp=input()
stri="".join(list(map(lambda i:l2[l.index(i)] if l.__contains__(i) else i,inp)))

print(stri)