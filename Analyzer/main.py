import json
import requests
import csv
import time
from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader as web
from matplotlib import pyplot
#######################const##############################
Stockapi ='7336764ddde9210a04d332ba033a4ff9'
LOS=5
folder='test/'
###########################################################
def getNews():
    api="563b86e1120b463c9b33bb1f8ee9c6ec"
    link="https://newsapi.org/v2/top-headlines?country=in&apiKey="

    r=requests.get(f"{link}{api}")
    news=json.loads(r.text)
   # tr=requests.get()
    print(news["articles"][0]["url"])
def getStockNews():
    link=f'https://fmpcloud.io/api/v3/stock_news?limit=50&apikey={Stockapi}'
    j=json.loads(requests.get(link).text)

    j=pd.DataFrame(j)
    for i in j['title']:
        print(i)
def getStocksAsQueryString(x):
    st=pd.read_excel('Stocks.xlsx',usecols='B')
    s= ["",]+list(st['Symbol'])[x*LOS-LOS:x*LOS]
    from functools import reduce
    q=reduce(lambda x,y:x+y+".NS,",s)
    return q

def getStockdata(x):
     #"HC65T6PS80NA0XA1"
    stock=getStocksAsQueryString(x)
    stock=stock[:len(stock)-1]
    #print(stock)
    url2=f"https://fmpcloud.io/api/v3/historical-price-full/{stock}?apikey={Stockapi}"

    j=json.loads(requests.get(url2).text)
    test= pd.DataFrame(j['historicalStockList'],list(i for i in range(LOS)))
    #print(test)
    #print(j)
    for i in range(LOS):
        for days in j['historicalStockList']:

            s=days['symbol']
            datafile = open(f"{folder}{s}.csv", 'w')
            csvWriter = csv.writer(datafile)
            c = 0
           #temp=j['Time Series (Daily)'][days]
            test=pd.DataFrame(days['historical'])
            test.to_csv(datafile,index=False)
def plotgraph(i):
    s = getStocksAsQueryString(i).split(',')
    for i in range(LOS):
        t = s[i]
        y = np.array((pd.read_csv(f'{folder}{t}.csv', usecols=['close']))['close'])
        x = np.array(list(i for i in range(y.size)))
        print(max(y))
        pyplot.subplot(int(LOS/1.5), 2, i + 1)
        pyplot.plot(x[::-1], y)
    pyplot.show()
    #pyplot.waitforbuttonpress()
    pyplot.close()

#
#getNews()
#getStockNews()
#plotgraph(3)
# for i in range(40,200):
#    try:
#         getStockdata(i)
#    except Exception as e:
#        print(e)
#getStocksAsQueryString()