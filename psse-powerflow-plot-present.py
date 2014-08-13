import os,sys
import operator

#PSSE_LOCATION = r"C:\Program Files\PTI\PSSE32\PSSBIN"
PSSE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION 

import psspy

import redirect
redirect.psse2py()
#---------------------------------------------------------------------

from itertools import groupby
from operator import itemgetter
attr_type = itemgetter(0)
from dvc_mapping import busMark

def subsystem_info(name, attributes, sid=-1, flag=1, ties=1):
     name = name.lower()
     gettypes = getattr(psspy, 'a%stypes' % name)
     apilookup = {
           'I': getattr(psspy, 'a%sint' % name),
           'R': getattr(psspy, 'a%sreal' % name),
           'X': getattr(psspy, 'a%scplx' % name),
           'C': getattr(psspy, 'a%schar' % name), }
     result = []
     ierr, attr_types = gettypes(attributes)
     for k, group in groupby(zip(attr_types, attributes), key=attr_type):
         func = apilookup[k]
         strings = list(zip(*group)[1])
         ierr, res = func(sid, flag, ties=3 if name=='brn' else None, string=strings)
         result.extend(res)
     return zip(*result)

# radian if deg=0; degree if deg=1
def rect(r, w, deg=0):
     from math import cos, sin, pi
     if deg:
          w = pi*w/180.0
     return r*cos(w), r*sin(w)

# radian if deg=0; degree if deg=1
def polar(x, y, deg=0):
     from math import hypot, atan2, pi
     if deg:
          return hypot(x, y), 180.0*atan2(y, x)/pi
     else:
          return hypot(x, y), atan2(y, x)
#---------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import groupby

# PSS/E Saved case
#CASE = r"C:\Program Files\PTI\PSSE32\EXAMPLE\11TH_PLAN_REV_MAR_2012.sav"
#CASE = r"C:\Program Files\PTI\PSSE32\EXAMPLE\12TH_PLAN_MAR_2017R1.sav"
CASE = r"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\11TH_PLAN_REV_MAR_2012.sav"
psspy.psseinit(9000)
psspy.case(CASE)

#------------------------
ierr = psspy.bus_data_2(44405, intgar1=4) #BkroA
ierr = psspy.bus_data_2(44010, intgar1=4) #BkroA
ierr, realaro = psspy.two_winding_data(44010, 44405, "1", intgar1=0) #BTPSAG to BkroA
ierr, realaro = psspy.two_winding_data(44200, 44405, "1", intgar1=0) #btps-b to bokaro-a interconnection
ierr = psspy.branch_data(44402, 44405, "1", intgar1=0) #Koderma - BkroA line
ierr = psspy.branch_data(44402, 44405, "2", intgar1=0) #Koderma - BkroA line

# Case specific load changes to be indicated here
# CD as on 28.2.2014
ierr = psspy.load_data_3(44100, realar1=44.6) #BOKARO
ierr = psspy.load_data_3(44101, realar1=24.4) #MOSABANI
ierr = psspy.load_data_3(44102, realar1=123.7) #BURDWAN
ierr = psspy.load_data_3(44103, realar1=43.0) #BELMURI
ierr = psspy.load_data_3(44104, realar1=15.0) #HOWRAH
ierr = psspy.load_data_3(44105, realar1=17.0) #KHARAGPUR
ierr = psspy.load_data_3(44106, realar1=359.5) #CHANDRAPURA
ierr = psspy.load_data_3(44107, realar1=10.0) #KOLAGHAT
ierr = psspy.load_data_3(44108, realar1=140.0) #JAMSHEDPUR
ierr = psspy.load_data_3(44101, realar1=42.2) #DTPS
ierr = psspy.load_data_3(44110, realar1=20.0) #BARHI
ierr = psspy.load_data_3(44111, realar1=59.4) #MAITHON HYDEL
ierr = psspy.load_data_3(44112, realar1=17.6) #PANCHET HYDEL
ierr = psspy.load_data_3(44113, realar1=89.65) #KODERMA
ierr = psspy.load_data_3(44114, realar1=30.0) #HAZARIBAGH
ierr = psspy.load_data_3(44115, realar1=36.35) #GOLA
ierr = psspy.load_data_3(44116, realar1=0.) #CHANDIL
ierr = psspy.load_data_3(44117, realar1=135.8) #PUTKI
ierr = psspy.load_data_3(44118, realar1=140.0) #KALIPAHARI
ierr = psspy.load_data_3(44119, realar1=57.3) #ASP
ierr = psspy.load_data_3(44120, realar1=116.0) #RAMGARH
ierr = psspy.load_data_3(44121, realar1=140.2) #KALYANESWARI
ierr = psspy.load_data_3(44122, realar1=89.6) #KUMARDUBI
ierr = psspy.load_data_3(44123, realar1=172.0) #PATHERDIH
ierr = psspy.load_data_3(44124, realar1=46.5) #NIMIAGHAT
ierr = psspy.load_data_3(44125, realar1=143.2) #GIRIDIH
ierr = psspy.load_data_3(44126, realar1=28.25) #SINDRI
ierr = psspy.load_data_3(44127, realar1=32.5) #RAMKANALI
ierr = psspy.load_data_3(44128, realar1=48.0) #PATRATU
ierr = psspy.load_data_3(44129, realar1=45.0) #NORTH KARANPURA
ierr = psspy.load_data_3(44133, realar1=15.0) #PURULIA
ierr = psspy.load_data_3(44134, realar1=72.0) #JAMURIA
ierr = psspy.load_data_3(44135, realar1=25.0) #KONAR
ierr = psspy.load_data_3(44205, realar1=182.8) #DURGAPUR
ierr = psspy.load_data_3(44206, realar1=44.0) #DHANBAD
ierr = psspy.load_data_3(44207, realar1=70.2) #MTPS
ierr = psspy.load_data_3(44208, realar1=90.0) #BURNPUR
ierr = psspy.load_data_3(44209, realar1=43.0) #RAMGARH2
ierr = psspy.load_data_3(44217, realar1=197.1) #BORJORA
ierr = psspy.load_data_3(44218, realar1=166.3) #PARULIA


# 2017 load forecast 
##ierr = psspy.load_data_3(44100, realar1=68.1, realar2=32.9) #BOKARO
##ierr = psspy.load_data_3(44101, realar1=24.4, realar2=11.8) #MOSABANI
##ierr = psspy.load_data_3(44102, realar1=143.7, realar2=69.6) #BURDWAN
##ierr = psspy.load_data_3(44103, realar1=63., realar2=30.51) #BELMURI
##ierr = psspy.load_data_3(44104, realar1=85., realar2=41.1) #HOWRAH
##ierr = psspy.load_data_3(44105, realar1=57., realar2=27.6) #KHARAGPUR
##ierr = psspy.load_data_3(44106, realar1=384.5, realar2=186.22) #CHANDRAPURA
##ierr = psspy.load_data_3(44107, realar1=22.5, realar2=10.9) #KOLAGHAT
##ierr = psspy.load_data_3(44108, realar1=140., realar2=67.8) #JAMSHEDPUR
##ierr = psspy.load_data_3(44109, realar1=42.2, realar2=20.4) #DTPS
##ierr = psspy.load_data_3(44110, realar1=35., realar2=16.9) #BARHI
##ierr = psspy.load_data_3(44111, realar1=59.4, realar2=28.7) #MAITHON HYDEL
##ierr = psspy.load_data_3(44112, realar1=17.6, realar2=8.5) #PANCHET HYDEL
##ierr = psspy.load_data_3(44113, realar1=91.6, realar2=44.4) #KODERMAOLD
##ierr = psspy.load_data_3(44114, realar1=60., realar2=29.) #HAZARIBAGH
##ierr = psspy.load_data_3(44115, realar1=36.35, realar2=17.61) #GOLA
##ierr = psspy.load_data_3(44116, realar1=60., realar2=29.0) #CHANDIL
##ierr = psspy.load_data_3(44117, realar1=158.3, realar2=76.6) #PUTKI
##ierr = psspy.load_data_3(44118, realar1=155., realar2=75.0) #KALIPAHARI
##ierr = psspy.load_data_3(44119, realar1=146.8, realar2=71.1) #ASP
##ierr = psspy.load_data_3(44120, realar1=134., realar2=64.9) #RAMGARH
##ierr = psspy.load_data_3(44121, realar1=195.2, realar2=94.5) #KALYANESWARI
##ierr = psspy.load_data_3(44122, realar1=109.3, realar2=52.9) #KUMARDUBI
##ierr = psspy.load_data_3(44123, realar1=185.5, realar2=89.8) #PATHERDIH
##ierr = psspy.load_data_3(44124, realar1=80.5, realar2=39.0) #NIMIAGHAT
##ierr = psspy.load_data_3(44125, realar1=152.7, realar2=73.9) #GIRIDIH
##ierr = psspy.load_data_3(44126, realar1=28.25, realar2=13.68) #SINDRI
##ierr = psspy.load_data_3(44127, realar1=47.5, realar2=23.0) #RAMKANALI
##ierr = psspy.load_data_3(44128, realar1=67.5, realar2=32.6) #PATRATU
##ierr = psspy.load_data_3(44129, realar1=45., realar2=21.8) #NORTH KARANPURA
##ierr = psspy.load_data_3(44133, realar1=15., realar2=7.26) #PURULIA
##ierr = psspy.load_data_3(44134, realar1=120., realar2=58.1) #JAMURIA
##ierr = psspy.load_data_3(44135, realar1=25., realar2=12.11) #KONAR
##ierr = psspy.load_data_3(44136, realar1=69.2, realar2=33.5) #BORJORA1
##ierr = psspy.load_data_3(44137, realar1=0.0,	realar2=0.0) #KODRMANEW
##ierr = psspy.load_data_3(44139, realar1=20.,	realar2=9.6) #MUGMA
##ierr = psspy.load_data_3(44202, realar1=100., realar2=48.4) #CTPS2
##ierr = psspy.load_data_3(44205, realar1=239.8, realar2=116.1) #DURGAPUR
##ierr = psspy.load_data_3(44206, realar1=59., realar2=28.5) #DHANBAD
##ierr = psspy.load_data_3(44207, realar1=100.2, realar2=48.5) #MTPS
##ierr = psspy.load_data_3(44208, realar1=105., realar2=50.8) #BURNPUR
##ierr = psspy.load_data_3(44209, realar1=53.0, realar2=25.6) #RAMGARH2
##ierr = psspy.load_data_3(44217, realar1=207.4, realar2=100.4) #BORJORA
##ierr = psspy.load_data_3(44218, realar1=178.3, realar2=86.3) #PARULIA
##ierr = psspy.load_data_3(44219, realar1=0., realar2=0.) #GOLA2
##ierr = psspy.load_data_3(44220, realar1=20., realar2=9.6) #GIRIDIH2
##ierr = psspy.load_data_3(44223, realar1=40., realar2=19.3) #KODERMA2
##ierr = psspy.load_data_3(44227, realar1=50., realar2=24.2) #RTPS2
##ierr = psspy.load_data_3(44230, realar1=30., realar2=14.5) #CHAS2
##ierr = psspy.load_data_3(44233, realar1=20., realar2=9.6) #PANAGARH
##ierr = psspy.load_data_3(44235, realar1=25., realar2=12.1) #NKPURA2
##ierr = psspy.load_data_3(44236, realar1=50., realar2=24.2) #PATRATU
##ierr = psspy.load_data_3(44239, realar1=40., realar2=19.3) #PARULIA

# Case specific generation dispatch changes to be indicated here
##ierr = psspy.machine_data_2(44003, intgar1=0) #KTPS gen
##ierr = psspy.machine_data_2(44004, realar1=540.0) #BTPS gen
##ierr = psspy.machine_data_2(44006, realar1=500.0) #DSTPS gen
##ierr = psspy.machine_data_2(44007, intgar1=0) #RTPS gen
##ierr = psspy.machine_data_2(44008, realar1=180.0) #DTPS gen4
##ierr = psspy.machine_data_2(44009, intgar1=0, realar1=120.0) #DTPS gen3
##ierr = psspy.machine_data_2(44010, intgar1=0) #BkroA gen
##ierr = psspy.machine_data_2(44013, realar1=450.0) #MTPSB gen1
##ierr = psspy.machine_data_2(44014, intgar1=0) #MTPSB gen2
##ierr = psspy.machine_data_2(44015, realar1=110.0) #CTPS gen1
##ierr = psspy.machine_data_2(44016, realar1=110.0) #CTPS gen2
##ierr = psspy.machine_data_2(44017, realar1=110.0) #CTPS gen3
##ierr = psspy.machine_data_2(44018, intgar1=1, realar1=230.0) #CTPS gen7
##ierr = psspy.machine_data_2(44019, intgar1=1, realar1=230.0) #CTPS gen8
##ierr = psspy.machine_data_2(44020, realar1=180.0) #MTPS gen1
##ierr = psspy.machine_data_2(44021, realar1=180.0) #MTPS gen2
##ierr = psspy.machine_data_2(44022, realar1=180.0) #MTPS gen3
##ierr = psspy.machine_data_2(44023, realar1=200.0) #MTPS gen4
##ierr = psspy.machine_data_2(44024, realar1=225.0) #MTPS gen5
##ierr = psspy.machine_data_2(44025, realar1=225.0) #MTPS gen6
##ierr = psspy.machine_data_2(44026, realar1=0) #RTPS gen1
##ierr = psspy.machine_data_2(44027, realar1=0) #RTPS gen2

# Case specific branch interconnection changes to be indicated here
##ierr = psspy.branch_data(44220, 44223, "1", intgar1=0) #giridih - koderma line
##ierr = psspy.branch_data(44220, 44223, "2", intgar1=0) 
##ierr = psspy.branch_data(44123, 44130, "1", intgar1=0) #patherdih - dhanbad line
##ierr = psspy.branch_data(44123, 44130, "2", intgar1=0) 
##ierr = psspy.branch_data(44111, 44123, "1", intgar1=1) #maithon hydel - patherdih line
##ierr = psspy.branch_data(44111, 44123, "2", intgar1=1) 
##ierr = psspy.branch_data(44109, 44118, "1", intgar1=1) #dtps-kalipahari line
##ierr = psspy.branch_data(44109, 44118, "2", intgar1=1)
##ierr = psspy.branch_data(44207, 44208, "1", intgar1=0) #mejia-burnpur line
##ierr = psspy.branch_data(44204, 44208, "1", intgar1=0) #mejia-klyn line
##ierr = psspy.branch_data(44202, 44207, "1", intgar1=0) #ctps-mtps line
##ierr = psspy.branch_data(44202, 44207, "2", intgar1=0)
##
##ierr = psspy.branch_data(44403, 45400, "1", intgar1=0) #RTPS - ranchi line
##ierr = psspy.branch_data(44403, 45400, "2", intgar1=0) 
##ierr = psspy.branch_data(44404, 45404, "1", intgar1=0) #DSTPS - paruliaPG line
##ierr = psspy.branch_data(44404, 45404, "2", intgar1=0) 
##ierr = psspy.branch_data(44404, 44403, "1", intgar1=1) #DSTPS - RTPS line
##ierr = psspy.branch_data(44404, 44403, "2", intgar1=1) 

#----------------------------

psspy.solution_parameters_2(intgar1=150)
psspy.fdns(option1=0, #tap adjustment disabled
           option2=0, #area interchange disables
           option3=0, #phase shift option disabled
           option4=0, #dc tap adjustment option disabled
           option5=0, #switched shunt adjustment option disabled
           )
psspy.fnsl()
psspy.inibus(0)
#ierr = psspy.pout(sid=1, all=0)
#n = psspy.totbus()

ierr = psspy.bsys(sid=1, numzone=1, zones=44)
businfo = subsystem_info('bus', ['NUMBER', 'BASE', 'NAME'], sid=-1)
#print businfo
mybuslst = subsystem_info('bus', ['NUMBER', 'BASE', 'NAME'], sid=1)
#print mybuslst
mygeninfo = subsystem_info('mach', ['NUMBER', 'PGEN', 'NAME'], sid=1)
#print mygeninfo
myloadinfo = subsystem_info('load', ['NUMBER', 'MVAACT', 'NAME'], sid=1)
#print myloadinfo
branchinfo = subsystem_info('brn', ['FROMNUMBER', 'TONUMBER', 'MVA', 'P'], sid=1)
#print branchinfo
trfinfo = subsystem_info('trn', ['FROMNUMBER', 'TONUMBER', 'MVA', 'P'], sid=1)
#print trfinfo

fig = plt.figure()
ax = fig.add_subplot(111)

a = list(reduce(tuple.__add__,[x[:2] for x in branchinfo])) 
b = [x[0] for x in mybuslst]
mybusdat = list(set(a+b))
tiebusdat = list(set(a)-set(b))
#print mybusdat

#generation markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for bus in mybusdat:
     if bus in busMark:
          mybus = [tup for tup in businfo if tup[0] == bus]
          #print mybus
          if mybus[0][1] == 132.0: dot = 'go'
          elif mybus[0][1] == 220.0: dot = 'bo'
          elif mybus[0][1] == 400.0: dot = 'ro'
          else: pass
          marker = ax.plot(busMark[bus][0], busMark[bus][1], dot)
          plt.text(busMark[bus][0]+2, busMark[bus][1], mybus[0][2], fontsize=6)

#generation markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
rbus=[]; rgenbus=[]
trinfo = [tup for tup in trfinfo if abs(tup[3]) >= 0.1]
for gen in mygeninfo:
     temp = [tup[1:] for tup in trinfo if tup[0] == gen[0]]
     if temp != []:
          rbus.append(temp[0])
#print trinfo
#print rbus

rbus.sort()
for key, group in groupby(rbus, lambda x:x[0]):
     gentot=0
     for rgen in group:
          gentot += rgen[1]
     rgenbus.append((rgen[0], gentot))
#print rgenbus

for bus in rgenbus:
     if bus[0] in busMark:
          plt.annotate(int(bus[1]), xy=(busMark[bus[0]][0], busMark[bus[0]][1]),
                       xytext=(busMark[bus[0]][0], busMark[bus[0]][1]+4),
                       bbox=dict(boxstyle="round", fc="0.8"),
                       arrowprops=dict(arrowstyle="->"), fontsize=6)
          
#load markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for bus in myloadinfo:
     if bus[0] in busMark:
          plt.text(busMark[bus[0]][0]+2, busMark[bus[0]][1]-2.5, 'L',
                   fontsize=6)
          plt.text(busMark[bus[0]][0]+4, busMark[bus[0]][1]-2.5,
                   int(abs(bus[1])), fontsize=6)

#line markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
brnflow=[]
for key, group in groupby(branchinfo, lambda x: (x[0], x[1])):
     flow=0; fdir=0; ckt=0
     for brn in group:
          flow += brn[2]
          fdir += brn[3]
          ckt += 1
     brnflow.append((brn[0], brn[1], int(flow), ckt, int(fdir)))
#print brnflow

for j in brnflow:
     if j[0] in busMark and j[1] in busMark:
          if j[4] > 0:
               x1 = busMark[j[0]][0]
               y1 = busMark[j[0]][1]
               x2 = busMark[j[1]][0]
               y2 = busMark[j[1]][1]
          else:
               x1 = busMark[j[1]][0]
               y1 = busMark[j[1]][1]
               x2 = busMark[j[0]][0]
               y2 = busMark[j[0]][1]
          theta = math.atan2(y2-y1,x2-x1)
          dist = math.hypot(x2-x1,y2-y1)
          dx, dy = rect(dist/2.0, theta, deg=0)
          if theta > 0 and theta < math.pi:
               dxt, dyt = map(sum, zip((rect(dist/2.0, theta, deg=0)),
                                       (rect(1, theta-math.pi/2.0, deg=0))))
          else:
               dxt, dyt = map(sum, zip((rect(dist/2.0, theta, deg=0)),
                                       (rect(1, theta+math.pi/2.0, deg=0))))
          x, y = zip(*(busMark[j[0]], busMark[j[1]]) )
          idx = [k[0] for k in businfo].index(j[0])
          if businfo[idx][1] == 132.0:
               plt.plot(x, y, 'g-')
               ax.arrow(x1, y1, dx, dy, width=.5, color='g')
##               ax.annotate(j[2],
##                           xy=(x1, y1), xycoords='data',
##                           xytext=(x1+dx, y1+dy), textcoords='data',
##                           arrowprops=dict(arrowstyle="->", 
##                           color="0.5",
##                           shrinkA=5, shrinkB=5,
##                           patchA=None,
##                           patchB=None,
##                           connectionstyle="arc3")
               plt.text(x1+dxt, y1+dyt, j[2], fontsize=6)
          elif businfo[idx][1] == 220.0:
               plt.plot(x, y, 'b-')
               ax.arrow(x1, y1, dx, dy, width=.5, color='b')
               plt.text(x1+dxt, y1+dyt, j[2], fontsize=6)
          elif businfo[idx][1] == 400.0:
               plt.plot(x, y, 'r-')
               ax.arrow(x1, y1, dx, dy, width=.5, color='r')
               plt.text(x1+dxt, y1+dyt, j[2], fontsize=6)
          else: pass

# Find in-service, non-transformer branches
in_branches = psspy.abrnint(sid=1, string=["FROMNUMBER", "TONUMBER"],
                            flag=1, ties=3)
# Find all non-transformer branches
all_branches = psspy.abrnint(sid=1, string=["FROMNUMBER", "TONUMBER"],
                             flag=2, ties=3)
# Flatten a arbitrarily nested lists and return the result as a single list
def flatten(l):
     ret = []
     for i in l:
          if isinstance(i, (list, tuple)):
               ret.extend(flatten(i))
          else:
               ret.append(i)
     return ret
# Remove zeros
in_branches = filter(lambda a: a != 0, flatten(in_branches))
all_branches = filter(lambda a: a != 0, flatten(all_branches))
# Find all out of service branches
out_branches = list(set(all_branches) - set(in_branches))
#print out_branches

#transformer markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
trfflow=[]
for key, group in groupby(trfinfo, lambda x: (x[0], x[1])):
     flow=0; fdir=0; ckt=0
     for trf in group:
          flow += trf[2]
          fdir += trf[3]
          ckt += 1
     trfflow.append((trf[0], trf[1], int(flow), ckt, int(fdir)))
#print trfflow

for j in trfflow:
     if j[0] in busMark and j[1] in busMark:
          x1 = busMark[j[0]][0]
          y1 = busMark[j[0]][1]
          x2 = busMark[j[1]][0]
          y2 = busMark[j[1]][1]
          theta1 = np.arctan2(y2-y1,x2-x1)
          theta2 = np.arctan2(y1-y2,x1-x2)
          dist = math.hypot(x2-x1,y2-y1)
          dx1 = np.cos(theta1)*((dist/2.0)-1)
          dy1 = np.sin(theta1)*((dist/2.0)-1)
          dx2 = np.cos(theta2)*((dist/2.0)-1)
          dy2 = np.sin(theta2)*((dist/2.0)-1)
          trfbus = [tup for tup in businfo if tup[0] == j[0] ]
          if trfbus[0][1] == 132.0:
               plt.plot([x1,(x2+x1)/2.0], [y1,(y2+y1)/2.0], 'g-')
               circ = plt.Circle((x1+dx1,y1+dy1), 2, color='g', fill=False)
               ax.add_artist(circ)
               if j[4] > 0:
                    ax.arrow(x1, y1, dx1, dy1, width=.5, color='g')
                    plt.text(x1+dx1, y1+dy1, j[2], fontsize=6)
               else:
                    pass
          elif trfbus[0][1] == 220.0:
               plt.plot([x1,(x2+x1)/2.0], [y1,(y2+y1)/2.0], 'b-')
               circ = plt.Circle((x1+dx1,y1+dy1), 2, color='b', fill=False)
               ax.add_artist(circ)
               if j[4] > 0:
                    ax.arrow(x1, y1, dx1, dy1, width=.5, color='b')
                    plt.text(x1+dx1, y1+dy1, j[2], fontsize=6)
               else:
                    pass
          elif trfbus[0][1] == 400.0:
               plt.plot([x1,(x2+x1)/2.0], [y1,(y2+y1)/2.0], 'r-')
               circ = plt.Circle( (x1+dx1,y1+dy1), 2, color='r', fill=False)
               ax.add_artist(circ)
               if j[4] > 0:
                    ax.arrow(x1, y1, dx1, dy1, width=.5, color='r')
                    plt.text(x1+dx1, y1+dy1, j[2], fontsize=6)
               else:
                    pass
          else: pass
          trfbus = [tup for tup in businfo if tup[0] == j[1] ]
          if trfbus[0][1] == 132.0:
               plt.plot([(x2+x1)/2.0,x2], [(y2+y1)/2.0,y2], 'g-')
               circ = plt.Circle( (x2+dx2,y2+dy2), 2, color='g', fill=False)
               ax.add_artist(circ)
               if j[4] < 0:
                    ax.arrow(x2, y2, dx2, dy2, width=.5, color='g')
                    plt.text(x2+dx2, y2+dy2, j[2], fontsize=6)
               else:
                    pass
          elif trfbus[0][1] == 220.0:
               plt.plot([(x2+x1)/2.0,x2], [(y2+y1)/2.0,y2], 'b-')
               circ = plt.Circle( (x2+dx2,y2+dy2), 2, color='b', fill=False)
               ax.add_artist(circ)
               if j[4] < 0:
                    ax.arrow(x2, y2, dx2, dy2, width=.5, color='b')
                    plt.text(x2+dx2, y2+dy2, j[2], fontsize=6)
               else:
                    pass
          elif trfbus[0][1] == 400.0:
               plt.plot([(x2+x1)/2.0,x2], [(y2+y1)/2.0,y2], 'r-')
               circ = plt.Circle( (x2+dx2,y2+dy2), 2, color='r', fill=False)
               ax.add_artist(circ)
               if j[4] < 0:
                    ax.arrow(x2, y2, dx2, dy2, width=.5, color='r')
                    plt.text(x2+dx2, y2+dy2, j[2], fontsize=6)
               else:
                    pass
          else: pass
          

ax.set_xlim(0,410)
ax.set_ylim(0,287)
ax.axes.get_xaxis().set_visible(True)
ax.axes.get_yaxis().set_visible(True)
#ax.set_title('load flow plot')
plt.text(300, 270, 'Damodar Valley Corporation', fontsize=12)
plt.text(300, 265, 'Gen in MW,', fontsize=10)
plt.text(327, 265, 'Brnchflow in MVA,', fontsize=10)
plt.text(368, 265, 'Load in MVA', fontsize=10)
plt.text(300, 260, '--400KV', color='red', fontsize=10)
plt.text(320, 260, '--220KV', color='blue', fontsize=10)
plt.text(340, 260, '--132KV', color='green', fontsize=10)
plt.show()

fig.set_size_inches(16.5,11.7)
extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig("loadflow.pdf", bbox_inches=extent)

buslst=[44102,44103,44109,44111,44118,44119,44121,44203,44204,44205,44207,
        44217,44218,44134]
psspy.bsys(sid=9, numbus=len(buslst), buses=buslst)
pzonebrn = subsystem_info('brn',['FROMNAME','TONAME','ID','P'],sid=9)
pzonebus = subsystem_info('bus', ['NAME', 'PU'], sid=9)
from collections import defaultdict
d = defaultdict(list)
for k, v in pzonebus: d[k].append(round(v,3))

from prettytable import PrettyTable
def add_data(lst):
    x = PrettyTable(["FbusV in pu", "Frombus name", "TbusV in pu",
                     "Tobus name", "Ckt ID", "Flow in MW"])
    x.align["FbusV in pu"] = "r"
    x.align["Frombus name"] = "l"
    x.align["TbusV in pu"] = "r"
    x.align["Tobus name"] = "l"
    x.align["Ckt ID"] = "l"
    x.align["Flow in MW"] = "r"
    for tup in lst:
        x.add_row([d[tup[0]],tup[0],d[tup[1]],tup[1],tup[2],round(tup[3],2)])
    mystr = x.get_string()
    return (mystr)
print add_data(pzonebrn)

def add_gen_data(lst):
    x = PrettyTable(["Bus Name", "Gen (MW)"])
    x.align["Bus Name"] = "l"
    x.align["Gen (MW)"] = "l"
    for tup in lst:
        x.add_row([tup[2],round(abs(tup[1]),2)])
    mystr = x.get_string()
    return (mystr)
print add_gen_data(mygeninfo)

def add_load_data(lst):
    x = PrettyTable(["Bus Name", "Load (MVA)"])
    x.align["Bus Name"] = "l"
    x.align["Gen (MW)"] = "l"
    for tup in lst:
        x.add_row([tup[2],round(abs(tup[1]),2)])
    mystr = x.get_string()
    return (mystr)
print add_load_data(myloadinfo)
          
         


