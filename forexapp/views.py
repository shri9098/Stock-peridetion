#-----ML library
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display

#-------------------------------
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from forexapp.models import *
import requests
import random
import json
import pandas_datareader as dr
# from .sentiment import *
from datetime import date
todays = date.today()
#---historical data intialise into dataframe------------------

#Put data into Pandas Dataframe
# df = dr.data.get_data_yahoo('GBPUSD=X',start=pd.to_datetime("2021-01-01"),end=pd.to_datetime(todays))
# csv = df.to_csv('CSV/gbp_usd.csv')
# print(csv,'csv')
# df = pd.read_csv('CSV/gbp_usd.csv')
#df[['Open','High','Low','Close','Adj Close']] = df[['Open','High','Low','Close','Adj Close']].applymap(lambda x: 1.0/x)
#display(df.tail())
# df.plot(x='Date', y='Adj Close', figsize=(10,4))

# # Normalize aclose value
# # We use this value to train model

# df['return'] = df['Adj Close'] - df['Adj Close'].shift(1)
# return_range = df['return'].max() - df['return'].min()
# df['return'] = df['return'] / return_range

# df.plot(x='Date', y='return', figsize=(10,4))
# display(df.head())

# # Make label, 1 as rising price, 0 as falling price

# df['label'] = df['return'].shift(-1)
# df['label'] = df['label'].apply(lambda x: 1 if x>0.0 else 0)
# # df.dropna(inplace=True)
# df.head()

# # Make training dataset

# n_features = 60 # number of features

# train_x = np.array([]).reshape([-1,n_features])
# train_y = np.array([]).reshape([-1,1])
# for index, row in df.iterrows():
#     i = df.index.get_loc(index)
#     if i<n_features:
#         continue
    
#     _x = np.array(df[i-n_features+1:i+1]['return']).T.reshape([1, -1])
#     _y = df.loc[i]['label']
#     train_x = np.vstack((train_x, _x))
#     train_y = np.vstack((train_y, _y))
# train_y = train_y.reshape([-1])
# print(train_x.shape)
# print(train_y.shape)
# print('%% of Class0 : %f' % (np.count_nonzero(train_y == 0)/float(len(train_y))))
# print('%% of Class1 : %f' % (np.count_nonzero(train_y == 1)/float(len(train_y))))

# # Define Model and fit
# # Here we use 95% of data for training, and last 5% for testing

# from sklearn.ensemble import GradientBoostingClassifier
# clf = GradientBoostingClassifier(random_state=0, learning_rate=0.01, n_estimators=10000)

# train_len = int(len(train_x)*0.95)
# clf.fit(train_x[:train_len], train_y[:train_len])

# accuracy = clf.score(train_x[train_len:], train_y[train_len:])
# print('Testing Accuracy: %f' % accuracy)

# # Predict test data

# pred = clf.predict(train_x[train_len:])


# # Calculate equity..

# contracts  = 10000.0
# commission = 0.0


# df_trade = pd.DataFrame(train_x[train_len:,-1], columns=['return'])
# df_trade['label']  = train_y[train_len:]
# df_trade['pred']   = pred
# df_trade['won']    = df_trade['label'] == df_trade['pred']
# df_trade['return'] = df_trade['return'].shift(-1) * return_range
# df_trade.drop(df_trade.index[len(df_trade)-1], inplace=True)

# def calc_profit(row):
#     if row['won']:
#         return abs(row['return'])*contracts - commission
#     else:
#         return -abs(row['return'])*contracts - commission

# df_trade['pnl'] = df_trade.apply(lambda row: calc_profit(row), axis=1)
# df_trade['equity'] = df_trade['pnl'].cumsum()

# display(df_trade.tail())
# df_trade.plot(y='equity', figsize=(10,4), title='Backtest with $10000 initial capital')
# plt.xlabel('Trades')
# plt.ylabel('Equity (USD)')
# for r in df_trade.iterrows():
#     if r[1]['won']:
#         plt.axvline(x=r[0], linewidth=0.5, alpha=0.8, color='g')
#     else:
#         plt.axvline(x=r[0], linewidth=0.5, alpha=0.8, color='r')


# # Calculate summary of trades

# n_win_trades = float(df_trade[df_trade['pnl']>0.0]['pnl'].count())
# n_los_trades = float(df_trade[df_trade['pnl']<0.0]['pnl'].count())
# print("Net Profit            : $%.2f" % df_trade.tail(1)['equity'])
# print("Number Winning Trades : %d" % n_win_trades)
# print("Number Losing Trades  : %d" % n_los_trades)
# print("Percent Profitable    : %.2f%%" % (100*n_win_trades/(n_win_trades + n_los_trades)))
# print("Avg Win Trade         : $%.3f" % df_trade[df_trade['pnl']>0.0]['pnl'].mean())
# print("Avg Los Trade         : $%.3f" % df_trade[df_trade['pnl']<0.0]['pnl'].mean())
# print("Largest Win Trade     : $%.3f" % df_trade[df_trade['pnl']>0.0]['pnl'].max())
# print("Largest Los Trade     : $%.3f" % df_trade[df_trade['pnl']<0.0]['pnl'].min())
# print("Profit Factor         : %.2f" % abs(df_trade[df_trade['pnl']>0.0]['pnl'].sum()/df_trade[df_trade['pnl']<0.0]['pnl'].sum()))

# df_trade['pnl'].hist(bins=20)

##################CustomerRegister start #######################
class CustomerRegist(ViewSet):
    def create(self,request):
        data=request.data
        try:
            username1=data.get("mobile")
            password1=data.get("password")
            fname=data.get("fullname")
        except:
            response_data = {'response_code':200,'comments':'All Fields is required',"status": False}
            return Response(response_data)

        if username1=='' or fname=='' or password1=='':
            response_data = {'response_code':200,'comments':'All Fields is required',"status": False}
            return Response(response_data)
        else:
            try:
                x=User(username=username1,password=make_password(password1),first_name=fname)
                x.save()
                response_data = {'response_code':200,'comments':'Accout Created',"status": True}
            except:
                response_data = {'response_code':200,'comments':'Username is already taken',"status": False}
            return Response(response_data)

    def list(self,request):
        user_obj=User.objects.all()
        if user_obj:
            dat_dict={}
            data_list=[]
            for x in user_obj:
                dat_dict={'user_id':x.id,'user_phone':x.username,'user_name':x.first_name}
                data_list.append(dat_dict)
            user_dict={"user_details":data_list,'response_code':200,'comments':'all list of user',"status": True}
            return Response(user_dict)
        else:
            user_dict={'response_code':200,'comments':'no details of user',"status": False}
            return Response(user_dict)


class Login(ViewSet):
    def create(self,request):
        data=request.data
        try:
            user=User.objects.filter(username=data.get('username'))
            user_password=data.get('password')
        except:
            user=None
            response_data = {'response_code':200,'comments':'All fields are Required',"status": False}
            return Response(response_data)

        if user:
            if user_password:
                if user[0].check_password(user_password):
                    name = User.objects.get(username=data.get('username'))
                    response_data = {'response_code':200,'user_name':name.first_name,'comments':'login successfully',"status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'invalid password',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'Please enter your password',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'Invalid User',"status": False}
            return Response(response_data)


class Logout_check(ViewSet):
    def list(self,request):
        logout(request)
        response_data = {'response_code':200,'comments':'logout is successful',"status": True}
        return Response(response_data) 


class ForexApi(ViewSet):
    def list(self,request):
        try:
            predict_list = [1,1,1,2,0,1,0,0]
            sell = random.choice(predict_list)
            if sell > 0:
                sell = True
                buy = False
            else:
                sell = False
                buy = True
            sell_one = {'sell':sell}
            url = "https://marketdata.tradermade.com/api/v1/historical"

            currency = "GBPUSD"
            api_key = "Hx0NiwGquVIZiKfXvuZY"
            fields = "open", "high", "low","close"
            date=todays
            interval="hourly"
            querystring = {"currency":currency,"date":date,"api_key":api_key}

            response = requests.get(url, params=querystring)
            res_url = json.loads(response.text)
            quotes = res_url['quotes']
            for i in quotes:
                i.update(sell_one)
                i.update({"buy":buy})
            response_data = {"data":res_url['quotes'],'Time frame':'5 Min','response_code':200,'comments':'data get',"status": True}
            return Response(response_data) 
        except:
            response_data = {'response_code':200,'comments':'no data get',"status": False}
            return Response(response_data)




class OrderdetailsApi(ViewSet):

    def create(self,request):
        data = request.data

        try:
            user = User.objects.get(username=data.get('username'))
            print(user,"username")
            currency = data.get("currency")
            action = data.get("action")
            price = data.get("price")
        except:
            response_data = {'response_code':200,'comments':'All fields are Required!',"status": False}
            return Response(response_data)
        if user:
            order = UserHistory(user=user,currency=currency,price=price,action=action)
            order.save()
            response_data = {'response_code':200,'comments':'Create order successfully!',"status": True}
            return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'User Not Exist!',"status": False}
            return Response(response_data)

class Indicatores(ViewSet):
    def list(self,request):
        window_10 = 10
        window_50 = 50
        indicators = {}
        list_ofma10 = []
        list_ofma50 = []
        try:
            currency_name = 'GBPUSD'
        except:
            response_data = {'response_code':200,'comments':'Please Choose time frame and currencies',"status": False}
            return Response(response_data)
        if currency_name=="":
            response_data = {'response_code':200,'comments':'Please Choose currencies',"status": False}
            return Response(response_data)
        else:
            df = pd.read_csv('CSV/gbp_usd.csv')
            indicators["currency_name"] = currency_name
            currency = currency_name
            data_set = df['Open']
            date = df['Date']
            open_price = df['Open']
            high = df['High']
            low = df['Low']
            # use for simple moving average 
            weights = np.repeat(1.0,window_10)/window_10
            smas_10 = np.convolve(data_set,weights,'valid')
            weights = np.repeat(1.0,window_50)/window_50
            smas_50 = np.convolve(data_set,weights,'valid')
            for i in smas_10:
                list_ofma10.append(i)
            for i in smas_50:
                list_ofma50.append(i)

            indicators["MA10"] = list_ofma10
            indicators["MA50"] = list_ofma50
            indicators["price"] = data_set
            indicators["date"] = df['Date']
            indicators["open"] = open_price
            indicators["close"] = low
            indicators["high"] = high
            indicators["low"] = low

            response_data = {'data':indicators,'response_code':200,'comments':'MA10,Ma50',"status": True}
            return Response(response_data)