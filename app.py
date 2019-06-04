import os
import re
import datetime as dt
import numpy
import pandas as pd

data = None
try:
    df = pd.read_csv('privatefiles/t.csv',';')
    #df = pd.read_csv('...','\t')
    #xlsx = Excel_File('t.xlsx')
    #df = pd.read_excel(xlsx,0)
    print(df.head(3))
    print(len(df))
except Exception as err:
    print('Problem with reading the file.<br/> '+err)


checkin = df[df['Transaction']=='Check-in']
checkin = checkin.rename(columns={'Check-in':'time','Date':'date','Departure':'departure'}).reset_index()
checkin = checkin[['date','time','departure']]
checkin['type']='checkin'
#checkin.head(5)

checkout = df[df['Transaction']=='Check-out']
checkout = checkout.rename(columns={'Check-out':'time','Amount':'cost','Destination':'arrival','Date':'date'}).reset_index()
checkout = checkout[['date','time','arrival','cost']]
checkout['type']='checkout'
#checkout.head(5)

cleaned = pd.DataFrame(columns=['type','date','time','departure','arrival','cost','duration','iswork'])
#cleaned

cleaned = pd.concat( [cleaned,checkin] , ignore_index=False, sort=False)
#cleaned.head(5)

cleaned.sort_values(by=['date','time'],ascending=[True,False],inplace=True)
checkout.sort_values(by=['date','time'],ascending=[True,True],inplace=True)
for i,r in checkout.iterrows():
    print(i)
    print(r)
    print('r - date - '+r['date'])
    print(cleaned.loc(['date']==r['date'] and ['time']<r['time']))
    break
#cleaned.head(4)
#cleaned.loc(['date']==r['date'])