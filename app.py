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

checkin = df[df['Transaction']=='Check-in'].rename(columns={'Check-in':'Time'}).reset_index()
checkin['Type','Arrival','Duration','Cost']=['Check-in','',0.,0.]
#checkin.head(5)

checkout = df[df['Transaction']=='Check-out']
checkout = checkout[['Date','Check-out','Destination','Amount']].rename(columns={'Check-out':'Time','Amount':'Cost'}).reset_index()
checkout['Type','Departure','Duration']=['Check-out','',0.]
#checkout.head(5)

#cleaned = pd.Series([dt.date(2019,6,2),dt.time(22,7,0),'','',0.0,dt.time(0,0,0),'Y'])
#from_dict(['Date','Time','Departure','Arrival','Cost','Duration','IsWork'])
#.columns(['Date','Time','Departure','Arrival','Cost','Duration','IsWork'])
#dt.date(2019,6,2)
#print(str(dt.time(22,11,1)))
cleaned = pd.DataFrame(columns=['Type','Date','Time','Departure','Arrival','Cost','Duration','IsWork'])
#.astype('object','datetime64','datetime64','object','object','float_','float_','bool_')
#cleaned

cinout = checkin['Date','Time','Departure'].append(checkout['Date','Time','Arrival','Cost'])
#cinout

