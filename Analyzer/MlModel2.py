import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from joblib import dump,load
from sklearn.preprocessing import StandardScaler
#################################
folder=r"C:\Users\tanma\Desktop\myprograms\PycharmProjects\PycharmProjects\Analyzer\test"+"\\"
toChange='close'
MLFolder=r'Estimators/'
stock='RELIANCE.NS'
delay=1
myPipeLine=Pipeline([('imputer',SimpleImputer(strategy='median'))])
remove=['date','label']
##################################


def makeML(st):
    data=pd.read_csv(open(f'{folder}{st}.csv','r'))
    rawdata=data[:][1:].drop(remove,axis=1).copy()
    rawdata=rawdata.reset_index()
    rawdata=rawdata.drop(['index'],axis=1).copy()
    rawdata['NextOpen']=list(i for i in data['open'][:-1])
    labels=pd.DataFrame(np.array(list(i for i in data[toChange][:-1])),columns=['NextCol'])
    labels=labels['NextCol']
    #trainData,testData=train_test_split(rawdata,test_size=0.2,random_state=42)
    #trainLabels,testLabels=train_test_split(labels,test_size=0.2,random_state=42)
    trainData_np= myPipeLine.fit_transform(rawdata)
    from sklearn.ensemble import RandomForestRegressor
    #model=RandomForestRegressor()
    from sklearn.linear_model import LinearRegression,LogisticRegression
    model=LinearRegression()
    #model=LogisticRegression()
    model.fit(trainData_np,labels)
    dump(model,f'{MLFolder}{st}.joblib')

    rmse=mean_squared_error(labels,model.predict(rawdata))**0.5
    err=cross_val_score(model,trainData_np,labels, scoring="neg_mean_squared_error", cv=10)
    rmn_se=np.sqrt(-err)
    print(rmse,rmn_se)
    write_csv(rmn_se.mean(),rmse,st)
def write_csv(rmn_se,rmse,s):
    data=open('data.csv','r')
    test=pd.DataFrame(np.array([[s,rmn_se,rmse]]),columns=["Stock","rmn_se","rmse"])
    test=pd.read_csv(data,usecols=["Stock","rmn_se","rmse"]).append(test)
    #print(test)
    data.close()
    data=open('data.csv','w')
    test.to_csv(data,index=False)
# write_csv('rms','rmse',stock)
makeML('TCS.NS')