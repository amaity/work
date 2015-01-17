import os,sys
import operator

#PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
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
        ierr, res = func(sid, flag, ties=3 if name=='brn' else None,
                          string=strings)
        result.extend(res)
    return zip(*result)

#---------------------------------------------------------------------
import numpy as np
import math
from itertools import groupby

# PSS/E Saved case
#CASE = r"C:\Program Files\PTI\PSSE32\EXAMPLE\12TH_PLAN_MAR_2017R1.sav"
#SAVFILE_LOCATION = r"C:\Program Files\PTI\PSSE33\EXAMPLE\\"
SAVFILE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\\"
CASE = r"12TH_PLAN_MAR_2017R1.sav"
psspy.psseinit(9000)
psspy.case(SAVFILE_LOCATION + CASE)

###------------------------
ierr = psspy.bus_data_2(44009, intgar1=4) #DTPSG3
#ierr = psspy.bus_data_2(44010, intgar1=4) #BkroA
ierr = psspy.bus_data_2(44031, intgar1=4) #RTPSG2
ierr = psspy.bus_data_2(44034, intgar1=4) #RTPSG3
ierr = psspy.bus_data_2(44035, intgar1=4) #RTPSG4
ierr = psspy.bus_data_2(44036, intgar1=4) #KODRG3
ierr = psspy.bus_data_2(44037, intgar1=4) #KODRG4
ierr = psspy.bus_data_2(44139, intgar1=4) #MUGMA1
ierr = psspy.bus_data_2(44140, intgar1=4) #CHAS1
ierr = psspy.bus_data_2(44141, intgar1=4) #RNIGNJ1
ierr = psspy.bus_data_2(44214, intgar1=4) #RNIGNJ2
ierr = psspy.bus_data_2(44219, intgar1=4) #GOLA2
ierr = psspy.bus_data_2(44227, intgar1=4) #RTPS2
ierr = psspy.bus_data_2(44228, intgar1=4) #MOSB2
ierr = psspy.bus_data_2(44230, intgar1=4) #CHAS2
ierr = psspy.bus_data_2(44232, intgar1=4) #KGP2
ierr = psspy.bus_data_2(44235, intgar1=4) #NKPURA2
ierr = psspy.bus_data_2(44236, intgar1=4) #PATR2
ierr = psspy.bus_data_2(44239, intgar1=4) #MEJIAB2
ierr = psspy.bus_data_2(44409, intgar1=4) #MOSB4
#ierr = psspy.bus_data_2(44405, intgar1=4) #BkroA


#LOAD AS ON 30.11.2014
ierr = psspy.load_data_3(44100, realar1=48., realar2=22.3) #BOKARO
ierr = psspy.load_data_3(44101, realar1=24.4, realar2=8.) #MOSABANI
ierr = psspy.load_data_3(44102, realar1=123.7, realar2=47.2) #BURDWAN
ierr = psspy.load_data_3(44103, realar1=43., realar2=20.7) #BELMURI
ierr = psspy.load_data_3(44104, realar1=15., realar2=18.8) #HOWRAH
ierr = psspy.load_data_3(44105, realar1=17., realar2=18.6) #KHARAGPUR
ierr = psspy.load_data_3(44106, realar1=370., realar2=100.3) #CHANDRAPURA
ierr = psspy.load_data_3(44107, realar1=15., realar2=7.4) #KOLAGHAT
ierr = psspy.load_data_3(44108, realar1=140., realar2=46.) #JAMSHEDPUR
ierr = psspy.load_data_3(44109, realar1=42.2, realar2=13.8) #DTPS
ierr = psspy.load_data_3(44110, realar1=20., realar2=11.5) #BARHI
ierr = psspy.load_data_3(44111, realar1=57., realar2=13.6) #MAITHON HYDEL
ierr = psspy.load_data_3(44112, realar1=17.6, realar2=5.7) #PANCHET HYDEL
ierr = psspy.load_data_3(44137, realar1=87.5, realar2=30.1) #KODERMAOLD
ierr = psspy.load_data_3(44114, realar1=45., realar2=19.7) #HAZARIBAGH
ierr = psspy.load_data_3(44115, realar1=31.6, realar2=11.9) #GOLA
ierr = psspy.load_data_3(44116, realar1=60., realar2=19.7) #CHANDIL
ierr = psspy.load_data_3(44117, realar1=134.7, realar2=52.) #PUTKI
ierr = psspy.load_data_3(44118, realar1=141., realar2=50.9) #KALIPAHARI
ierr = psspy.load_data_3(44119, realar1=57.3, realar2=38.2) #ASP
ierr = psspy.load_data_3(44120, realar1=162., realar2=41.) #RAMGARH
ierr = psspy.load_data_3(44121, realar1=140., realar2=52.2) #KALYANESWARI
ierr = psspy.load_data_3(44122, realar1=90., realar2=35.9) #KUMARDUBI
ierr = psspy.load_data_3(44123, realar1=171., realar2=50.9) #PATHERDIH
ierr = psspy.load_data_3(44124, realar1=46.5, realar2=26.4) #NIMIAGHAT
ierr = psspy.load_data_3(44125, realar1=139., realar2=50.1) #GIRIDIH
ierr = psspy.load_data_3(44126, realar1=28.25, realar2=9.2) #SINDRI
ierr = psspy.load_data_3(44127, realar1=32.5, realar2=15.6) #RAMKANALI
ierr = psspy.load_data_3(44128, realar1=48., realar2=22.1) #PATRATU
ierr = psspy.load_data_3(44129, realar1=45., realar2=14.7) #NORTH KARANPURA
ierr = psspy.load_data_3(44133, realar1=18., realar2=4.9) #PURULIA
ierr = psspy.load_data_3(44134, realar1=72., realar2=39.4) #JAMURIA
ierr = psspy.load_data_3(44135, realar1=25., realar2=8.2) #KONAR
ierr = psspy.load_data_3(44136, realar1=69.2, realar2=22.7) #BORJORA1
ierr = psspy.load_data_3(44113, realar1=0.0, realar2=0.0) #KODRMANEW
ierr = psspy.load_data_3(44139, realar1=20., realar2=6.5) #MUGMA
ierr = psspy.load_data_3(44202, realar1=100., realar2=32.8) #CTPS2
ierr = psspy.load_data_3(44205, realar1=191.5, realar2=13.2) #DURGAPUR
ierr = psspy.load_data_3(44206, realar1=74., realar2=10.) #DHANBAD
ierr = psspy.load_data_3(44207, realar1=63.7, realar2=23) #MTPS
ierr = psspy.load_data_3(44208, realar1=150., realar2=34.5) #BURNPUR
ierr = psspy.load_data_3(44209, realar1=53., realar2=17.4) #RAMGARH2
ierr = psspy.load_data_3(44217, realar1=200., realar2=70.4) #BORJORA
ierr = psspy.load_data_3(44218, realar1=182.3, realar2=46.3) #PARULIA
ierr = psspy.load_data_3(44219, realar1=0., realar2=0.) #GOLA2
ierr = psspy.load_data_3(44220, realar1=20., realar2=9.6) #GIRIDIH2
ierr = psspy.load_data_3(44223, realar1=40., realar2=9.3) #KODERMA2
ierr = psspy.load_data_3(44227, realar1=50., realar2=14.2) #RTPS2
ierr = psspy.load_data_3(44230, realar1=30., realar2=10.5) #CHAS2
ierr = psspy.load_data_3(44233, realar1=20., realar2=3.6) #PANAGARH
ierr = psspy.load_data_3(44235, realar1=25., realar2=8.1) #NKPURA2
ierr = psspy.load_data_3(44236, realar1=50., realar2=8.2) #PATRATU
ierr = psspy.load_data_3(44239, realar1=0., realar2=0.) #MEJIAB


# Case specific branch interconnection changes to be indicated here
ierr = psspy.branch_data(44220, 44223, "1", intgar1=0) #giridih - koderma line
ierr = psspy.branch_data(44220, 44223, "2", intgar1=0) 
ierr = psspy.branch_data(44123, 44130, "1", intgar1=0) #patherdih - dhanbad line
ierr = psspy.branch_data(44123, 44130, "2", intgar1=0) 
ierr = psspy.branch_data(44111, 44123, "1", intgar1=0) #maithon hydel - patherdih line
ierr = psspy.branch_data(44111, 44123, "2", intgar1=0) 
ierr = psspy.branch_data(44109, 44118, "1", intgar1=1) #dtps-kalipahari line
ierr = psspy.branch_data(44109, 44118, "2", intgar1=1)
ierr = psspy.branch_data(44403, 45400, "1", intgar1=0) #RTPS - Ranchi line
ierr = psspy.branch_data(44403, 45400, "2", intgar1=0) 
ierr = psspy.branch_data(44404, 45404, "1", intgar1=0) #DSTPS - paruliaPG line
ierr = psspy.branch_data(44404, 45404, "2", intgar1=0) 
ierr = psspy.branch_data(44218, 44231, "1", intgar1=1) #DSTPS - PARU line
ierr = psspy.branch_data(44218, 44231, "2", intgar1=1)

# Kalipahari voltage upgrade case
ierr = psspy.bus_data_2(44240, intgar1=1) #KALI2
ierr, realaro = psspy.two_winding_data(44118, 44240, "1", intgar1=1) #KALI2 - KALI1 trf
ierr, realaro = psspy.two_winding_data(44118, 44240, "2", intgar1=1) #KALI2 - KALI1 trf
ierr = psspy.branch_data(44118, 44121, "1", intgar1=1) #KLYN1 - KALI1 line
ierr = psspy.branch_data(44118, 44121, "2", intgar1=1)
ierr = psspy.branch_data(44204, 44240, "1", intgar1=0) #KLYN2 - KALI2 line
ierr = psspy.branch_data(44204, 44240, "2", intgar1=0)
ierr = psspy.branch_data(44207, 44208, "1", intgar1=0) #MTPS - BURN2 line
ierr = psspy.branch_data(44207, 44208, "2", intgar1=0)
a3z =  (0.014313, 0.086133, 0.140196) # 3AZ
d = 51.23 # MTPS - KALI distance in km
lc = [0.01*d*i for i in a3z]
ierr = psspy.branch_data(44207, 44240, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #MTPS - KALI2 line
ierr = psspy.branch_data(44207, 44240, "2", intgar1=0, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
d = 7 # KALI - BURN distance in km
lc = [0.01*d*i for i in a3z]
ierr = psspy.branch_data(44240, 44208, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #KALI2 - BURN line
ierr = psspy.branch_data(44240, 44208, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
ierr = psspy.load_data_3(44208, realar1=168.) #Burnpur

#### Case: D/C LILO of DSTPS - PARULIA at JAMURIA
d = 10 # DTPS - DSTPS distance in km
lc = [0.01*d*i for i in a3z]
ierr = psspy.branch_data(44203, 44231, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #DTPS - DSTPS line
ierr = psspy.branch_data(44203, 44231, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
d = 32 # DSTPS - JAMU distance in km
lc = [0.01*d*i for i in a3z]
ierr = psspy.branch_data(44231, 44241, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #DSTPS - JAMU line
ierr = psspy.branch_data(44231, 44241, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
d = 42 # JAMU2 - PARU2 distance in km
lc = [0.01*d*i for i in a3z]
ierr = psspy.branch_data(44241, 44218, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #JAMU2 - PARU line
ierr = psspy.branch_data(44241, 44218, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
ierr = psspy.branch_data(44203, 44218, "1", intgar1=0) #DTPS - PARU line
ierr = psspy.branch_data(44203, 44218, "2", intgar1=0)
ierr = psspy.branch_data(44231, 44218, "1", intgar1=0) #DSTPS - PARU line
ierr = psspy.branch_data(44231, 44218, "2", intgar1=0)

#### Case: D/C LILO of DTPS - DSTPS at JAMURIA
##d = 38 # DTPS - JAMU2 distance in km
##lc = [0.01*d*i for i in a3z]
##ierr = psspy.branch_data(44203, 44241, "1", intgar1=1, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2]) #DTPS - JAMU2 line
##ierr = psspy.branch_data(44203, 44241, "2", intgar1=1, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2])
##d = 32 # JAMU2 - DSTPS distance in km
##lc = [0.01*d*i for i in a3z]
##ierr = psspy.branch_data(44203, 44241, "1", intgar1=1, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2]) #JAMU2 - DSTPS line
##ierr = psspy.branch_data(44203, 44241, "2", intgar1=1, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2])
##ierr = psspy.branch_data(44203, 44218, "1", intgar1=0) #DTPS - PARU line
##ierr = psspy.branch_data(44203, 44218, "2", intgar1=0)
##ierr = psspy.branch_data(44231, 44218, "1", intgar1=1) #DSTPS - PARU line
##ierr = psspy.branch_data(44231, 44218, "2", intgar1=1)
#--------------------------------

### PST placement at Jamuria
##ierr = psspy.bus_data_2(44142, intgar1=1) #JMUPST1
##ierr = psspy.movebrn(44127, 44134, '1', 44142, '1')
##ierr, realaro = psspy.two_winding_data(44142, 44134, "1", intgar1=1)

##ierr, realaro = psspy.two_winding_data(44134, 44142, "1", intgar1=1,
##                                       intgar7=32, intgar12=3, intgar13=1,
##                                       realar1=.00097, realar2=.03497,
##                                       realar3=150., realar4=1.0, realar5=132.,
##                                       realar6=15., realar8=132., realar9=150.,
##                                       realar20=70., realar21=0.) #JMU1 - JMUPST1 trf
#----------------------------------
### Additional ASP lines
##ierr = psspy.branch_data(44109, 44119, "3", intgar1=1, realar1=0.002781434,
##                         realar2=0.008661488, realar3=0.001763027)
##ierr = psspy.seq_branch_data(44109, 44119, "3", realar1=0.007021062,
##                             realar2=0.028150285, realar3=0.001087962)
##ierr = psspy.branch_data(44109, 44119, "4", intgar1=1, realar1=0.002781434,
##                         realar2=0.008661488, realar3=0.001763027)
##ierr = psspy.seq_branch_data(44109, 44119, "4", realar1=0.007021062,
##                             realar2=0.028150285, realar3=0.001087962)


ierr, realaro = psspy.two_winding_data_3(44108, 44210, "1", #JSR_ATR1 (AREVA)
                                       intgar1=1,         #STAT
                                       intgar7=17,        #NTP1
                                       intgar10=44108,    #CONT1
                                       intgar12=1,        #COD1
                                       intgar13=1,        #CW
                                       intgar14=3,        #CZ
                                       intgar15=2,        #CM
                                       realari1=299550.,   #R1-2
                                       realari2=0.1529,    #X1-2
                                       realari3=160.,      #SBS1-2
                                       realari4=138./132., #WINDV1
                                       realari5=138.,      #NOMV1
                                       realari6=0.,        #ANG1
                                       realari7=230./220.,   #WINDV2
                                       realari8=230.,       #NOMV2
                                       realari9=160.,      #RATA1
                                       realari16=26200.,     #MAG1
                                       realari17=0.0808,     #MAG2
                                       realari26=0.        #CNXA1
                                       )     
ierr, realaro = psspy.two_winding_data_3(44108, 44210, "2", #JSR_ATR2 (AREVA)
                                       intgar1=1,         #STAT
                                       intgar7=17,        #NTP1
                                       intgar10=44108,    #CONT1
                                       intgar12=1,        #COD1
                                       intgar13=1,        #CW
                                       intgar14=3,        #CZ
                                       intgar15=2,        #CM
                                       realari1=299550.,   #R1-2
                                       realari2=0.1529,    #X1-2
                                       realari3=160.,      #SBS1-2
                                       realari4=138./132., #WINDV1
                                       realari5=138.,      #NOMV1
                                       realari6=0.,        #ANG1
                                       realari7=230./220.,   #WINDV2
                                       realari8=230.,       #NOMV2
                                       realari9=0.,      #RATA1
                                       realari16=26200.,     #MAG1
                                       realari17=0.000808,     #MAG2
                                       realari26=0.        #CNXA1
                                       )     
ierr, realaro = psspy.two_winding_data_3(44121, 44204, "1", #KLYN_STR2 (BB, 5127/1)
                                       intgar1=1,         #STAT
                                       intgar7=15,        #NTP1
                                       intgar10=44121,    #CONT1
                                       intgar12=1,        #COD1
                                       intgar13=1,        #CW
                                       intgar14=3,        #CZ
                                       intgar15=2,        #CM
                                       realari1=171720.,   #R1-2
                                       realari2=0.15428,    #X1-2
                                       realari3=50.,      #SBS1-2
                                       realari4=34.5/33., #WINDV1
                                       realari5=34.5,      #NOMV1
                                       realari6=0.,        #ANG1
                                       realari7=132./132.,   #WINDV2
                                       realari8=132.,       #NOMV2
                                       realari9=0.,      #RATA1
                                       realari16=21163.2,     #MAG1
                                       realari17=0.61/836.7, #MAG2
                                       realari26=0.        #CNXA1
                                       )     

#---------------------------------
# CTPS1 generation off
##ierr = psspy.machine_data_2(44015, intgar1=0) #CTPS gen1
##ierr = psspy.machine_data_2(44016, intgar1=0) #CTPS gen2
##ierr = psspy.machine_data_2(44017, intgar1=0) #CTPS gen3
##ierr = psspy.load_data_3(44106, realar1=184.5) #CHANDRAPURA
##ierr = psspy.load_data_3(44202, realar1=300.) #CTPS2

###-------------------------------
ierr = psspy.bsys(sid=1, numzone=1, zones=44)
ierr, all_buses = psspy.abusint(sid=1, string=["NUMBER"], flag=2)
all_buses = all_buses[0]
ierr, in_buses = psspy.abusint(sid=1, string=['NUMBER'], flag=1)
in_buses = in_buses[0]
out_buses = list(set(all_buses)-set(in_buses))
print out_buses
ierr = psspy.bsys(sid=2, numbus=len(out_buses), buses=out_buses)
ierr = psspy.extr(sid=2, all=0, status2=0)

##for i in range(len(out_buses)):
##     psspy.load_data_3(i, intgar1=0)
##
##ierr = psspy.bsys(sid=2, numbus=len(out_buses), buses=out_buses)
##ierr, in_branches = psspy.abrnint(sid=2, string=['FROMNUMBER', 'TONUMBER'],
##                                  flag=1)
##for i in range(len(in_branches[0])):
##     psspy.branch_data(in_branches[0][i], in_branches[1][i], intgar1=0)
##ierr, in_trfs = psspy.atrnint(sid=2, string=['FROMNUMBER', 'TONUMBER'],
##                                  flag=1)
##for i in range(len(in_trfs[0])):
##     psspy.two_winding_data(in_trfs[0][i], in_trfs[1][i], intgar1=0)

###------------------------
status, scalval = [0,1,4,0], []
ierr, totals, moto = psspy.scal(sid=1, all=0, apiopt=1, status=status,
                                scalval=scalval)
scalval = [0.,0.,totals[2],totals[3],totals[4],totals[5],0.98]
ierr, totals, moto = psspy.scal(sid=1, all=0, apiopt=2, status=status,
                                scalval=scalval)


def run_psse():
    psspy.solution_parameters_3(intgar2=70)
    #psspy.fdns()
    psspy.fnsl((1,0,1,0,0,0,99,1))
    psspy.inibus(0)
    #ierr = psspy.pout(sid=1, all=0)
    #n = psspy.totbus()

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

    a = list(reduce(tuple.__add__,[x[:2] for x in branchinfo])) 
    b = [x[0] for x in mybuslst]
    mybusdat = list(set(a+b))
    #mybusdat = [i for i in businfo for j in mybus if i[0]==j]
    tiebusdat = list(set(a)-set(b))
    #print mybusdat
    rbus=[]; rgenbus=[]
    for gen in mygeninfo:
        temp = [tup[1:] for tup in trfinfo if tup[0] == gen[0]]
        rbus.append(temp[0])
    #print rbus
    rbus.sort()
    for key, group in groupby(rbus, lambda x:x[0]):
        gentot=0
        for rgen in group:
            gentot += rgen[1]
        rgenbus.append((rgen[0], gentot))
    #print rgenbus
    brnflow=[]
    for key, group in groupby(branchinfo, lambda x: (x[0], x[1])):
        flow=0; fdir=0; ckt=0
        for brn in group:
            flow += brn[2]
            fdir += brn[3]
            ckt  += 1
        brnflow.append((brn[0], brn[1], int(flow), ckt, round(fdir,2) ))
    #print brnflow
    trfflow=[]
    for key, group in groupby(trfinfo, lambda x: (x[0], x[1])):
        flow=0; fdir=0; ckt=0
        for trf in group:
            flow += trf[2]
            fdir += trf[3]
            ckt  += 1
        trfflow.append((trf[0], trf[1], int(flow), ckt, int(fdir)))
    #print trfflow
    return businfo, mybusdat, rgenbus, myloadinfo, brnflow, trfflow
