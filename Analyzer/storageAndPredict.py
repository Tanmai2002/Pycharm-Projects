from MlModel2 import makeML
import pandas as pd
################################################

################################################
st = pd.read_excel('Stocks.xlsx', usecols='B')
stocks = list((str(i)+'.NS') for i in st['Symbol'])[:200]
print(len(stocks))
for j in stocks:
    try:
        makeML(j)
    except Exception as e:
        print(e)

