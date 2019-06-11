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

for i,r in checkout.iterrows():
    ind = -1
    f = cleaned[cleaned['atime'].isnull()]
    print('1',len(f))
    #print(f.head(4))
    if f is not None:
        f = f[f['date']==r['date']]
    print('2',len(f))
    #print(f.head(4))
    if f is not None:
        f = f[f['dtime']<r['atime']]
    print('3',len(f))
    #print(f.head(4))
    if f is not None:
        ind = iloc(f)
    print('4',f.head(4))
    if ind>=0:
        print(ind)
        cleaned[ind]['atime','arrival','cost']=r['atime','arrival','cost']
        break

+