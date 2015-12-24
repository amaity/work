import re, glob, csv, StringIO, string
import numpy as np
import pandas as pd
from datetime import datetime
from collections import defaultdict

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


files = glob.glob("*.csv")
data, ss_name, divn, n = [], 0, 0, 0

#------------- direct input data ---------------
capacity = """swyd,volt,instal,mva
              HOWRAH,33, ,0
              HOWRAH,132,2x72 (line),144
              BELMURI,33,1x31.5 (trf:132:33),31.5
              BELMURI,132,2x72 (line),144
              BURDWAN,33,2x50+1x80 (trf:132:33),180
              BURDWAN,132,2x100 (line),200
              KHARAGPUR,132,2x72 (line),144
              KOLAGHAT,132,2x72 (line),144
              KALIPAHARI,33,2x80+1x50 (trf:132:33),210
              KALIPAHARI,132,2x72 (line),144
              KALYANESWARI,33,2x50 (trf:132:33),100
              KALYANESWARI,132,3x150 (trf:220:132),450
              KALYANESWARI,220,3x180 (line),540
              MAITHON,33,2x50 (trf:132:33),100
              MAITHON,132,2x72+2x112 (line),368
              KUMARDHUBI,33,3x50 (trf),150
              KUMARDHUBI,132,1x72 (line),72
              PANCHET HYDEL,33,1x10+1x31.5 (trf),41.5
              PANCHET HYDEL,132,2x72 (line),144
              RAMKANALI,132,2x72 (line),144
              BURNPUR,33,2x50 (trf),100
              BURNPUR,220,1x180 (line),180
              CHANDIL,132,2x72 (line),144
              JAMSHEDPUR,33,1x50 (trf),50
              JAMSHEDPUR,132,1x150+1x160 (atr),310
              JAMSHEDPUR,220,2x180 (line),360
              MOSABANI,33,1x31.5+1x20 (trf),51.5
              MOSABANI,132,2x72 (line),144
              PURULIA,33,1x50 (trf),50
              PURULIA,132,2x72 (line),144
              PATHERDIH,33,2x80+1x50 (trf),210
              PATHERDIH,132,2x72 (line),144
              SINDRI,132,2x72 (line),144
              PUTKI,33,3x80 (trf),240
              PUTKI,132,4x72 (line),288
              NIMIAGHAT,33,1x20+1x31.5 (trf),51.5
              NIMIAGHAT,132,2x72 (line),144
              GIRIDIH,33,3x80 (trf),240
              GIRIDIH,132,2x160 (atr),320
              GIRIDIH,220,2x180 (line),360
              CTPS,33,2x80 (trf),160
              CTPS,132,1x160+2x150 (atr),470
              CTPS,220,2x250 (gen),500
              BIADA,33,2x27 (line),54
              DHANBAD,33,2x80 (trf),160
              DHANBAD,132,0 (atr),0
              DHANBAD,220,2x180 (line),360
              BTPS,33,2x50 (trf),100
              BTPS,132,2x150 (atr),300
              BTPS,220,0 (gen),0
              BARHI,33,1x50+1x31.5 (trf),81.5
              BARHI,132,2x72 (line),144
              HAZARIBAGH,33,2x50 (trf),100
              HAZARIBAGH,132,2x72 (line),144
              KONAR,33,1x20 (trf),20
              KONAR,132,1x72 (line),72
              GOLA,33,1x31.5+1x20 (trf),51.5
              GOLA,132,2x72 (line),144
              KODERMA,33,2x50 (trf),100
              KODERMA,132,2x72 (line),144
              RAMGARH,33,2x50+2x80+1x50 (trf),310
              RAMGARH,132,2x150 (atr),300
              RAMGARH,220,2x180 (line),360
              PATRATU,33,1x31.5 (trf),31.5
              PATRATU,132,2x72 (line),144
              NORTH KARANPURA,33,2x50 (trf),100
              NORTH KARANPURA,132,2x72 (line),144
              DTPS,33,3x50 (trf),150
              DTPS,132,2x150 (atr),300
              DTPS,220,4x180 (line),720
              PARULIA,33,2x80 (atr),160
              PARULIA,220,4x180 (line),720
              MTPS,33,2x80 (trf),160
              MTPS,220,4x210+2x250 (gen),1340
              ASP,33,2x50 (trf:132:33),100
              ASP,132,2x72 (line),144
              DURGAPUR,33,2x80+1x50 (trf:220:33),210
              DURGAPUR,220,2x180 (line),360
              BARJORA,33,2x50+1x100 (trf:220:33),200
              BORJORA,132,2x150 (trf:220:132),300
              BARJORA,220,2x180 (line),360"""

df_cap = pd.read_csv(StringIO.StringIO(capacity))
#print df_cap.head()
d = defaultdict(list)
for i, row in enumerate(csv.reader(StringIO.StringIO(capacity))):
    if not i or not row:
        continue
    d[row[0].strip()].append(row[1:])

#---------- contract demand data ---------------
with open(files[0], 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row_list = filter(None, row)
        if row_list:
            if 'CD AS ON' in row_list[0] and n<2:
                n += 1
            elif row_list[0] == 'sl' or row_list[0] == 'no':
                pass
            elif 'GOMD' in row_list[0]:
                divn = row_list[0]
            elif is_number(row_list[0]):
                ss_name = row_list[1]
            elif n==2:
                break
            else:
                row_list.insert(0,divn)
                row_list.insert(1,ss_name)
                data.append(row_list)
 
                
df_cd = pd.DataFrame(data)
colidx = df_cd.columns.values
df_cd[colidx[0]] = df_cd[colidx[0]].map(lambda x: x.split('.')[-1])
df_cd[colidx[1]] = df_cd[colidx[1]].str.replace("[_()]*","")
df_cd[colidx[1]] = df_cd[colidx[1]].str.replace(r'^\S*BTPS\S*',"BTPS")
df_cd[colidx[1]] = df_cd[colidx[1]].str.replace(r'^\S*MAIT\S*\s*\S*','maithon')
df_cd[colidx[1]] = df_cd[colidx[1]].str.replace(r'^\S*KUMA\S*\s*\S*','kumardhubi')
df_cd[colidx[1]] = df_cd[colidx[1]].str.upper()
df_cd[colidx[1]] = df_cd[colidx[1]].str.strip()
df_cd[colidx[3]] = df_cd[colidx[3]].convert_objects(convert_numeric=True)
#df_cd['kv'] = np.where(df_cd[colidx[2]].str.contains('132|Rly')==True,132,
#                       np.where(df_cd[colidx[2]].str.contains('220')==True,220,33))
segs = '132|Rly|Skipper|ECR|Ellen|Food'
conditions = [df_cd[colidx[2]].str.contains(segs)==True,
              df_cd[colidx[2]].str.contains('220')==True]
choices = [132,220]
df_cd['KV'] = np.select(conditions,choices,default=33)
#print df_cd.tail()
gpcd = df_cd.groupby([colidx[1],'KV'])
#print gpcd.sum().loc['GIRIDIH',33].tolist()

#---------- construction clearance data ---------------
reobj = re.compile(
r"""\s*  # optional whitespace
(\d+)    # Day
[.-/]    # separator
(\d+)    # Month
[.-/]    # separator
(?:20)?  # century (optional)
(\d+)    # years (YY)
\s*      # optional whitespace""",
re.VERBOSE)
regx = re.compile('[.-/]')

def dparse(date):
    d, m, y = regx.split(date.strip())
    #ndate = "".join(ldate)
    #return datetime.strftime(datetime.strptime(ndate,"%d%m%Y"), "%d-%m-%Y")
    return '-'.join((d.zfill(2),m.zfill(2),('20'+y.zfill(2) if len(y)==2 else y)))
#print dparse('21.05.1965')
f = lambda x: x if "" else dparse(x)

df_const = pd.read_csv(files[1], skiprows=1, skipfooter=2, header=True,
                       parse_dates=[2], date_parser=f)
colidx = df_const.columns.values
df_const[[colidx[4],colidx[5]]] = df_const[[colidx[4],colidx[5]]].convert_objects(convert_numeric=True)
df_const[colidx[1]] = df_const[colidx[1]].str.upper()
#print df_const.head()
#print df_const.columns.values
#print df_const.dtypes
#dfc = df_const[[colidx[1],colidx[4],colidx[5]]]
conditions = [df_const[colidx[3]].str.contains(segs)==True,
              df_const[colidx[3]].str.contains('220')==True]
df_const['KV'] = np.select(conditions,choices,default=33)
gpconst = df_const.groupby([colidx[1],'KV'])
#print gpconst.get_group(('GIRIDIH',33)).values.tolist()
#print gpconst.sum().loc['DURGAPUR',33].tolist()

#---------- survey progress data ---------------
df_survey = pd.read_csv(files[2], skiprows=1, skipfooter=1, header=True)
colidx = df_survey.columns.values
df_survey[colidx[2]] = df_survey[colidx[2]].str.replace(r'^\S*GIRI\S*\s*\S*','Giridih')
df_survey[colidx[2]] = df_survey[colidx[2]].str.replace(r'^\S*KODER\S*\s*\S*','Koderma')
df_survey[colidx[2]] = df_survey[colidx[2]].str.replace(r'^\S*Maith\S*\s*\S*','Maithon')
df_survey[colidx[2]] = df_survey[colidx[2]].str.replace(r'^\S*Pather\S*/*\s*\S*','Patherdih')
df_survey[colidx[2]] = df_survey[colidx[2]].str.replace(r'^\S*Raghu\S*\s*\S*','RTPS')
df_survey[colidx[2]] = df_survey[colidx[2]].str.upper()
df_survey[colidx[4]].fillna(0, inplace=True)
df_survey[colidx[5]].fillna(0, inplace=True)
df_survey[colidx[4]].replace({'-':0},inplace=True)
df_survey[colidx[5]].replace({'-':0},inplace=True)
df_survey[[colidx[4],colidx[5]]] = df_survey[[colidx[4],colidx[5]]].convert_objects(convert_numeric=True)
#print df_survey.head()
conditions = [df_survey[colidx[3]].str.contains(segs)==True,
              df_survey[colidx[3]].str.contains('220')==True]
df_survey['kv'] = np.select(conditions,choices,default=33)
gpsurvey = df_survey.groupby([colidx[2],'kv'])
#print gpsurvey.sum()#.loc['RAMGARH',33].tolist()
#---------- print output ---------------

def capacity(d,key):
    print "{0}".format("-"*80)
    print "|{:<12}|{:^26}|{:>12}|{:>12}|{:>12}|".format("Voltg level",
                                                  "Installed capacity",
                                                  "Total (MVA)",
                                                  "Enhancement","")
    print "{0}".format("-"*80)
    for lst in d[key]:
        print "|{:<12}|{:^26}|{:>12}|{:>12}|{:>12}|".format(lst[0],lst[1],
                                                              lst[2],'','')
    print "{0}".format("-"*80)
    print

def connected(key,lst,gpcd):
    try:
        arr = gpcd.get_group((key,int(lst[0]))).values.tolist()
        print "Existing consumers at {0} KV: {1}".format(lst[0],'')
        print "{0}".format("-"*80)
        print "|{:<12}|{:^26}|{:>12}|{:<12}|{:<12}|".format("Con no.",
                                                    "Consumer name",
                                                    "CD (MVA)",
                                                    "Enhancement","")
        print "{0}".format("-"*80)            
        for i in arr:
            print "|{:<12}|{:^26.26}|{:>12}|{:<12}|{:<12}|".format('',i[2],
                                                            i[3],'','')
        print "{0}".format("-"*80)
        tot = gpcd.sum().loc[key,int(lst[0])].tolist()
        print "|{:<12}|{:>26}|{:>12}|{:<12}|{:<12}|".format('','Total',
                                                            tot[0],'','')
        print "{0}".format("-"*80)
    except KeyError:
        print "Existing consumers at {0} KV: {1}".format(lst[0],'None')
        print ''

def sumd(key,lst,gpcd):
    try:
        tot = gpcd.sum().loc[key,int(lst[0])].tolist()
        return tot[0]
    except KeyError:
        return 0

def construction(key,lst,gpconst):
    try:
        arr = gpconst.get_group((key,int(lst[0]))).values.tolist()
        print "Existing construction clearances at {0} KV: {1}".format(lst[0],'')
        print "{0}".format("-"*80)
        print "|{:<12}|{:^26.26}|{:>12}|{:>12}|{:<12}|".format("CC date",
                                                               "Consumer name",
                                                               "IniCD (MVA)",
                                                               "FinCD (MVA)","")
        print "{0}".format("-"*80)            
        for i in arr:
            print "|{:<12}|{:^26.26}|{:>12}|{:>12}|{:<12}|".format(i[2],
                                                            i[3],i[4],i[5],'')
        print "{0}".format("-"*80)
        tot = gpconst.sum().loc[key,int(lst[0])].tolist()
        print "|{:<12}|{:>26}|{:>12}|{:>12}|{:<12}|".format('','Total',
                                                            tot[1],tot[2],'')
        print "{0}".format("-"*80)
    except KeyError:
        print "Existing construction clearances at {0} KV: {1}".format(lst[0],'None')
        print ''

def sumc(key,lst,gpconst):
    try:
        tot = gpconst.sum().loc[key,int(lst[0])].tolist()
        return tot[1]
    except KeyError:
        return 0

def survey(key,lst,gpsurvey):
    try:
        arr = gpsurvey.get_group((key,int(lst[0]))).values.tolist()
        print "Existing survey at {0} KV: {1}".format(lst[0],'')
        print "{0}".format("-"*80)
        print "|{:<12}|{:^26}|{:>12}|{:>12}|{:<12}|".format("App. date",
                                                    "Consumer name",
                                                    "IniCD (MVA)",
                                                            "FinCD (MVA)","")
        print "{0}".format("-"*80)            
        for i in arr:
            print "|{:<12}|{:^26.26}|{:>12}|{:>12}|{:<12}|".format('',i[3],
                                                            i[4],i[5],'')
        print "{0}".format("-"*80)
        tot = gpsurvey.sum().loc[key,int(lst[0])].tolist()
        print "|{:<12}|{:>26}|{:>12}|{:>12}|{:<12}|".format('','Total',
                                                            tot[0],tot[1],'')
        print "{0}".format("-"*80)
    except KeyError:
        print "Existing survey at {0} KV: {1}".format(lst[0],'None')
        print ''

def sums(key,lst,gpsurvey):
    try:
        tots = gpsurvey.sum().loc[key,int(lst[0])].tolist()
        return tots[0]
    except KeyError:
        return 0

def demand(d,key,gpcd,gpconst):
    print "Demand versus installed capacity considering enhancement requests and \n\
construction clearances (with initial demand) issued till date"
    print "{0}".format("-"*80)
    print "|{:<12}|{:^26}|{:>12}|{:>12}|{:>12}|".format("Voltg level",
                                                        "Installed capacity",
                                                        "Exist demand",
                                                        "Proj demand",
                                                        "Shortfall")
    print "{0}".format("-"*80)
    for lst in d[key]:
        totd = sumd(key,lst,gpcd)
        totc = sumc(key,lst,gpconst)
        e = float(lst[2])-float(totd)-float(totc)
        print "|{:<12}|{:^26}|{:>12}|{:>12}|{:>12}|".format(lst[0],lst[2],
                                                            totd,totc,
                                                            e if e < 0 else 0)
    print "{0}".format("-"*80)
    print
    print "Demand versus installed capacity considering enhancement requests, construction\n\
 clearances (with initial demand) as well as applications in hand"
    print "{0}".format("-"*80)
    print "|{:<12}|{:^26}|{:>12}|{:>12}|{:>12}|".format("Voltg level",
                                                        "Installed capacity",
                                                        "Exist demand",
                                                        "Proj demand",
                                                        "Shortfall")
    print "{0}".format("-"*80)
    for lst in d[key]:
        totd = sumd(key,lst,gpcd)
        totc = sumc(key,lst,gpconst)
        tots = sums(key,lst,gpsurvey)
        e = float(lst[2])-float(totd)-float(totc)-float(tots)
        print "|{:<12}|{:^26}|{:>12}|{:>12}|{:>12}|".format(lst[0],lst[2],
                                                            totd,
                                                float(totc)+float(tots),
                                                            e if e < 0 else 0)
    print "{0}".format("-"*80)
    print
    

def printout(d,gpcd,gpconst,gpsurvey):
    print "{0}".format("*"*80)
    print "{:^80}".format("Capacity Evaluation")
    print "{0}".format("*"*80)
    for key in d:
        print "{: ^80}".format(key)
        capacity(d,key)
        for lst in d[key]:
            print
            connected(key,lst,gpcd)
            print
            construction(key,lst,gpconst)
            print
            survey(key,lst,gpsurvey)
        print
        demand(d,key,gpcd,gpconst)

def shortfall():
    print
    print "{0}".format("*"*80)
    print "{:^80}".format("Shortfall Calculation")
    print "{0}".format("*"*80)
    print
    for key in d:
        print "{0}".format("-"*80)
        print "|{:<12.12}|{:<12}|{:^26}|{:>12}|{:>12}|".format("Substation",
                                                        "Voltg (KV)",
                                                        "Installed/Projected",
                                                        "Total (MVA)",
                                                        "Shortfl(MVA)")
        print "{0}".format("-"*80)
        totd = 0
        for lst in d[key]:
            print lst[1]
            #s = lst[2].translate(None, "()").split()[1].split(":")
            s = lst[1] if 'trf' in lst[1] else ''
            totd += sumd(key,lst,gpcd) if repr(lst[0]) in s else 0
            totc = sumc(key,lst,gpconst)
            tots = sums(key,lst,gpsurvey)
            e = float(lst[2])-float(totd)-float(totc)-float(tots)
            print "|{:<12.12}|{:<12}|{:<26}|{:>12}|{:>12}|".format(key,lst[0],
                                                        "Installed capacity",
                                                                   lst[2],"")
            print "|{:<12.12}|{:<12}|{:<26}|{:>12}|{:>12}|".format("","",
                                                        "Present demand",
                                                                  totd,"")
            print "|{:<12.12}|{:<12}|{:<26}|{:>12}|{:>12}|".format("","",
                                                        "Projected demand",
                                            float(totc)+float(tots),
                                                        e if e < 0 else 0)
        print "{0}".format("-"*80)
            
                                                                   
print printout(d,gpcd,gpconst,gpsurvey)
print shortfall()
#print '  '+'abcd'
