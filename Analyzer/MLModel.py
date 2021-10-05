import pandas as pd
import numpy as np
import datetime as dt
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from  sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error
#################################
folder=r"C:\Users\tanma\Desktop\myprograms\PycharmProjects\PycharmProjects\Analyzer\test"+"\\"
toChange='close'
#stock='ITC.NS'
delay=1
remove=['label','close','adjClose','change','changePercent','volume','unadjustedVolume','vwap','changeOverTime']
##################################
def predict(stock,get='rmse',lastX=10):
    f=open(f'{folder}{stock}.csv','r')
    stock_data=pd.read_csv(f)
    #print(stock_data)
    #stock_data.dropna(subset=['close','open'])
    #print(stock_data.keys())
    stock_data['date']=list( map(lambda x:dt.date.fromisoformat(x).timetuple().tm_yday,stock_data['date']))
    #stock_data['diff']=stock_data['open']-stock_data['close']
    raw_data1=stock_data.drop(remove,axis=1).copy()
    raw_data=stock_data.drop(remove,axis=1)[delay:].copy()
    # t=stock_data['open'][:-1].copy()
    # raw_data1['NextDayopen']=list(i for i in t)
    #raw_data1=raw_data[::-1]
    print(raw_data)
    #print(raw_data['date'])
    #print(raw_data.keys())
    labels=stock_data[toChange][:-delay].copy()
    # NextDay= stock_data['open'][:-delay].copy()
    # raw_data=raw_data.reset_index()
    # raw_data=raw_data.drop("index",axis=1)
    # raw_data['NextDayopen']=list(i for i in NextDay)
    #print(raw_data)
    #labels.reset_index()
    #print(raw_data[toChange])
    #print(raw_data.corr()[toChange])
    x=int(len(raw_data)*0.8)
    train_params,test_params=raw_data[:x],raw_data[x:]#train_test_split(raw_data, test_size=0.2, random_state=42)
    train_labels,test_labels=labels[:x],labels[x:]#train_test_split(labels, test_size=0.2, random_state=42)
    #print(test_labels.keys())
    #train_params['nextOpen']=list(i for i in train_labels)
    #x=pd.concat([train_params,train_labels],axis=1)
    #print(raw_data1)
    #test=stock_data.corr()

    #print(test['open'].sort_values(ascending=False))
    my_pipeline=Pipeline([
        ('imputer', SimpleImputer(strategy="median"))
        #     ..... add as many as you want in your pipeline
        #('std_scaler', StandardScaler())
    ])
    train_params_np=my_pipeline.fit_transform(train_params)
    #################################################################################
    from sklearn.linear_model import LinearRegression
    model=LinearRegression()
    #[31.78875315 36.03689725 45.173224   31.08656454 30.27902532 31.46331246
    # 34.72220103 40.18156255 28.64269858 41.20927027]
    ################################################################################
    from sklearn.ensemble import RandomForestRegressor
    #model=RandomForestRegressor()
    #[36.06516849 37.98308801 46.4343824  39.28178911 31.91237981 34.60794988
    # 38.92869631 45.36736637 33.15110674 48.49724894]
    #################################################################################
    from sklearn.tree import DecisionTreeRegressor
    #model=DecisionTreeRegressor()
    ################################################################################
    from sklearn.ensemble import AdaBoostRegressor
    #model=AdaBoostRegressor()
    #[45.85500887 42.77303683 53.99690905 52.06479137 42.86586493 48.70211978
     # 51.23756074 50.56696032 42.35444793 57.80350268]
     ##############################################################################
    from sklearn.linear_model import SGDRegressor
    #model=SGDRegressor()
    # [31.34586262 35.60033987 44.23512751 31.78802207 29.32943695 31.71501199
    #  36.2811919  44.82117152 29.30149568 41.48582352]
    # 35.551947411142635
    ###############################################################################
    from sklearn.neighbors import KNeighborsRegressor
    #model=KNeighborsRegressor()
    # [40.50158836 45.56062336 67.87101547 54.84650179 39.5980947  41.51397242
    #  49.95994509 44.86003242 45.095517   53.74741939]
    # 41.20295699335655
    ###############################################################################
    from sklearn.ensemble import BaggingRegressor
    #model=BaggingRegressor()
    # [35.37712883 42.00445867 47.1960491  42.90969884 35.70919436 36.94102278
    #  38.34011071 44.07474547 34.43938819 48.81833857]
    # 16.875313114526605

    model.fit(train_params_np,train_labels)
    # xdata=train_params.iloc[:10]
    # ydata=train_labels.iloc[:10]
    # processed_data=model.predict(my_pipeline.transform(xdata))
    # print(processed_data,list(ydata))
    #print(test_labels)
    ######################################################
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(model, train_params_np, train_labels, scoring="neg_mean_squared_error", cv=10)
    rmse_scores = np.sqrt(-scores)
    print(rmse_scores.std())
    print(rmse_scores.mean())
    #####################################################
    testdata=mean_squared_error(train_labels,model.predict(train_params_np))

    print(np.sqrt(testdata))
    l=list(map(lambda x,y:str(x)+" "+str(y),model.predict(train_params_np),train_labels))
    #test.append()
    #x=raw_data1.append(test,i)
    #raw_data1.loc[len(raw_data1.index)]=[2054,2054,1985,1991.45,1991.45,10150000,10150000,-55.85,-2.73]
    now=my_pipeline.transform(raw_data1[0:lastX])
    #np.array([[2012.0,2013.699951,1973.699951,-17.34998,-0.862],])
    if get.__eq__('rmse'):
        return mean_squared_error(model.predict(now),labels.to_list()[0:lastX])**0.5
    return model.predict(now)
print(predict('RELIANCE.NS',get='',lastX=10))
#print(raw_data.keys())
# for i in l:
#     print(i)

