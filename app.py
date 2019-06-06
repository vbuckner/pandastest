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
checkin = checkin.rename(columns={'Check-in':'dtime','Date':'date','Departure':'departure'}).reset_index()
checkin = checkin[['date','dtime','departure']]
checkin.head(5)

checkout = df[df['Transaction']=='Check-out']
checkout = checkout.rename(columns={'Check-out':'atime','Amount':'cost','Destination':'arrival','Date':'date'}).reset_index()
checkout = checkout[['date','atime','arrival','cost']]

checkout.head(5)

cleaned = pd.DataFrame(columns=['date','dtime','departure','atime','arrival','cost','duration','iswork'])
cleaned

cleaned = pd.concat( [cleaned,checkin] , ignore_index=False, sort=False)
cleaned.head(5)

cleaned.sort_values(by=['date','dtime'],ascending=[True,True],inplace=True)
checkout.sort_values(by=['date','atime'],ascending=[True,True],inplace=True)
#print(cleaned.head(5))
#print(checkout.head(3))

for i,r in checkout.iterrows():
    print(cleaned['date'][i])
    print(r['date'])
    print(cleaned['dtime'][i])
    print(r['atime'])
    f = cleaned[(cleaned['date']==r['date']) & (cleaned['dtime']<cleaned['atime'])]
    print(f)
    break
cleaned.head(4)

