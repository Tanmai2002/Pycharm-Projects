import requests
import os
import pickle
if not os.path.exists("Picklingproject"):
    os.mkdir("Picklingproject")
os.chdir("Picklingproject")

url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
with open("mainText.txt",'w') as f:
    text=requests.get(url)
    f.write(text.text)
with open("mainText.txt",'r') as f:
    l=f.read().splitlines()
    with open("pickle.pkl",'wb') as f1:
        pickle.dump(l,f1)
with open("pickle.pkl",'rb') as f:
    outp=pickle.load(f)
    print(outp)