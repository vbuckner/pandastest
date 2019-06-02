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
except Exception as err:
    print('Problem with reading the file.<br/> '+err)

checkin = df[df['Transaction']=='Check-in']
checkin = checkin[checkin['Date','Check-in','Departure']]
checkin.rename({'Check-in':'Time'})
checkin = checkin.reset_index()
checkin['Arrival','Cost','Duration','IsWork']=['',0.0,0,'']
#checkin

checkout = df[df['Transaction']=='Check-out']
checkout = checkout[checkin['Date','Check-out','Destination','Cost']]
checkout.rename({'Destination':'Arrival','Check-out':'Time'})
checkout['Departure','Duration'
#checkout

#cleaned = pd.Series([dt.date(2019,6,2),dt.time(22,7,0),'','',0.0,dt.time(0,0,0),'Y'])
#from_dict(['Date','Time','Departure','Arrival','Cost','Duration','IsWork'])
#.columns(['Date','Time','Departure','Arrival','Cost','Duration','IsWork'])
#dt.date(2019,6,2)
#print(str(dt.time(22,11,1)))
##cleaned = pd.DataFrame(columns=['Date','Time','Departure','Arrival','Cost','Duration','IsWork'])
#cleaned

#checkin[['Date','Check-in','Departure']]
#cleaned.append(checkin['Date','Check-in','Departure'].rename({'Check-in':'Time'}))
#cleaned.append([checkin,checkout],ignore_index)
#cleaned

print('done')