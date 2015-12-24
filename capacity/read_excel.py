# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:00:11 2013

@author: SYSTEM
"""
import re, glob, datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

divs = {'GOMD-I': ['HOWRAH','BELMURI','BURDWAN','KHARAGPUR','KOLAGHAT'],
        'GOMD-II': ['KALIPAHARI','KALYANESWARI','MAITHON L/Bank',
                    'MAITHON R/Bank','KUMARDHUBI', 'PANCHET HYDEL',
                    'RAMKANALI','Burnpur', 'Jamuria'],
        'GOMD-III': ['CHANDIL','JAMSHEDPUR','MOSABANI','PURULIA'],
        'GOMD-IV': ['PATHERDIH', 'SINDRI', 'PUTKI','NIMIAGHAT','GIRIDIH',
                     'CTPS','BIADA','Dhanbad'],
        'GOMD-V': ['BTPS-A','BARHI','HAZARIBAGH','KONAR','GOLA','KODERMA',
                   'RAMGARH','PATRATU','North Karanpura'],
        'GOMD-VI': ['DTPS', 'PARULIA', 'MTPS', 'ASP', 'DURGAPUR', 'BARJORA']}


def xls2df(fn):
    xls = pd.ExcelFile(fn)
    df = xls.parse(xls.sheet_names[0],parse_cols="A:D",skiprows=3,skip_footer=1,
               header=0,index_col=None)
    df.columns = ['Divn','Substn','Consumer','CD']
    df.ix[df['Substn'].notnull(),'Divn'] = np.nan 
    df['Divn'].fillna(method='ffill',inplace=True)
    df['Substn'].fillna(method='ffill',inplace=True)
    df = df[pd.notnull(df['CD'])]
    return df


chunks=[]
for f in glob.glob('./*.xls'):
    datestr = re.search(r'(?<=\s)[\d\.]+(?=\.)',f).group(0)
    dateobj = datetime.datetime.strptime(datestr,'%d.%m.%Y').date()
    df = xls2df(f)
    df['Date'] = dateobj
    #df.set_index(['Date'],inplace=True)
    chunks.append(df)

df1 = pd.concat(chunks)
df2 = df1.ix[:,df1.columns-['Divn','Consumer']]
df3 = df2.groupby(['Date','Substn']).sum().unstack(level=-1)
df3.plot(x_compat=True)
#plt.show()
print df3.tail()

