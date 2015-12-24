import os,sys

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

# PSS/E Saved case
#CASE = r"C:\Program Files\PTI\PSSE32\EXAMPLE\12TH_PLAN_MAR_2017R1.sav"
#SAVFILE_LOCATION = r"C:\Program Files\PTI\PSSE33\EXAMPLE\\"
SAVFILE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\\"
CASE = r"12TH_PLAN_MAR_2017R1.sav"
psspy.psseinit(9000)
psspy.case(SAVFILE_LOCATION + CASE)

###------------------------
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
ierr = psspy.bus_data_2(44231, intgar1=4) #DSTPS2
ierr = psspy.bus_data_2(44232, intgar1=4) #KGP2
ierr = psspy.bus_data_2(44233, intgar1=4) #PANAG2
ierr = psspy.bus_data_2(44234, intgar1=4) #BDWN2
ierr = psspy.bus_data_2(44235, intgar1=4) #NKPURA2
ierr = psspy.bus_data_2(44236, intgar1=4) #PATR2
ierr = psspy.bus_data_2(44239, intgar1=4) #MEJIAB2
ierr = psspy.bus_data_2(44240, intgar1=4) #KALI2
ierr = psspy.bus_data_2(44241, intgar1=4) #JAMURIA2
ierr = psspy.bus_data_2(44305, intgar1=1, intgar2=4, intgar=44, realar1=33.) #DGPDVC2
ierr = psspy.bus_data_2(44409, intgar1=4) #MOSB4


#LOAD AS ON 31.8.2015
ierr = psspy.load_data_3(44100, realar1=68.) #BOKARO
ierr = psspy.load_data_3(44101, realar1=96.) #MOSABANI
ierr = psspy.load_data_3(44102, realar1=124.) #BURDWAN
ierr = psspy.load_data_3(44103, realar1=43.) #BELMURI
ierr = psspy.load_data_3(44104, realar1=15.) #HOWRAH
ierr = psspy.load_data_3(44105, realar1=17.) #KHARAGPUR
ierr = psspy.load_data_3(44106, realar1=359.) #CHANDRAPURA
ierr = psspy.load_data_3(44107, realar1=14.5) #KOLAGHAT
ierr = psspy.load_data_3(44108, realar1=140.) #JAMSHEDPUR
ierr = psspy.load_data_3(44109, realar1=42.2) #DTPS
ierr = psspy.load_data_3(44110, realar1=48.) #BARHI
ierr = psspy.load_data_3(44111, realar1=56.6+18.) #MAITHON HYDEL
ierr = psspy.load_data_3(44112, realar1=17.6) #PANCHET HYDEL
ierr = psspy.load_data_3(44137, realar1=93.) #KODERMAOLD
ierr = psspy.load_data_3(44114, realar1=80.) #HAZARIBAGH
ierr = psspy.load_data_3(44115, realar1=48.6) #GOLA
ierr = psspy.load_data_3(44116, realar1=60.) #CHANDIL
ierr = psspy.load_data_3(44117, realar1=185.7) #PUTKI
ierr = psspy.load_data_3(44118, realar1=141.3) #KALIPAHARI
ierr = psspy.load_data_3(44119, realar1=57.3) #ASP
ierr = psspy.load_data_3(44120, realar1=203.75-53.) #RAMGARH
ierr = psspy.load_data_3(44121, realar1=143.25) #KALYANESWARI
ierr = psspy.load_data_3(44122, realar1=105.23) #KUMARDUBI
ierr = psspy.load_data_3(44123, realar1=208.65-40.0) #PATHERDIH (minus GOVINDPUR)
ierr = psspy.load_data_3(44124, realar1=61.5) #NIMIAGHAT
ierr = psspy.load_data_3(44125, realar1=146.) #GIRIDIH
ierr = psspy.load_data_3(44126, realar1=27.5) #SINDRI
ierr = psspy.load_data_3(44127, realar1=34.) #RAMKANALI
ierr = psspy.load_data_3(44128, realar1=55.2) #PATRATU
ierr = psspy.load_data_3(44129, realar1=45.) #NORTH KARANPURA
ierr = psspy.load_data_3(44133, realar1=16.75) #PURULIA
ierr = psspy.load_data_3(44134, realar1=73.) #JAMURIA
ierr = psspy.load_data_3(44135, realar1=27.) #KONAR
ierr = psspy.load_data_3(44136, realar1=26.) #BORJORA1
ierr = psspy.load_data_3(44113, realar1=0.0) #KODRMANEW
ierr = psspy.load_data_3(44138, realar1=26.6) #BIADA
ierr = psspy.load_data_3(44139, realar1=20.) #MUGMA
ierr = psspy.load_data_3(44202, realar1=0.0) #CTPS2
ierr = psspy.load_data_3(44205, realar1=177.5) #DURGAPUR
ierr = psspy.load_data_3(44206, realar1=69.+40.) #DHANBAD
ierr = psspy.load_data_3(44207, realar1=46.9) #MTPS
ierr = psspy.load_data_3(44208, realar1=180.) #BURNPUR
ierr = psspy.load_data_3(44209, realar1=53.) #RAMGARH2
ierr = psspy.load_data_3(44217, realar1=203.-26.) #BORJORA
ierr = psspy.load_data_3(44218, realar1=179.1) #PARULIA
ierr = psspy.load_data_3(44219, realar1=0.) #GOLA2
ierr = psspy.load_data_3(44220, realar1=20.) #GIRIDIH2
ierr = psspy.load_data_3(44223, realar1=0.) #KODERMA2
ierr = psspy.load_data_3(44227, realar1=0.) #RTPS2
ierr = psspy.load_data_3(44230, realar1=0.) #CHAS2
ierr = psspy.load_data_3(44233, realar1=0.) #PANAGARH
ierr = psspy.load_data_3(44235, realar1=0.) #NKPURA2
ierr = psspy.load_data_3(44236, realar1=0.) #PATRATU
ierr = psspy.load_data_3(44239, realar1=0.) #MEJIAB


# Case specific branch interconnection changes to be indicated here
ierr = psspy.branch_data(44118, 44121, "1", intgar1=1) #KLYN1 - KALI1 line
ierr = psspy.branch_data(44118, 44121, "2", intgar1=1)
ierr = psspy.branch_data(44123, 44130, "1", intgar1=0) #patherdih - dhanbad line
ierr = psspy.branch_data(44123, 44130, "2", intgar1=0) 
ierr = psspy.branch_data(44111, 44123, "1", intgar1=1) #maithon hydel - patherdih line
ierr = psspy.branch_data(44111, 44123, "2", intgar1=1) 
ierr = psspy.branch_data(44109, 44106, "1", intgar1=1) #dtps-ctps line
ierr = psspy.branch_data(44109, 44134, "1", intgar1=1) #dtps-jamuria line
ierr = psspy.branch_data(44109, 44134, "2", intgar1=0)
ierr = psspy.branch_data(44127, 44134, "1", intgar1=1) #jamuria-ramkanali line 
ierr = psspy.branch_data(44115, 44138, "1", intgar1=0) #gola-biada line
ierr = psspy.branch_data(44115, 44138, "2", intgar1=0)

ierr = psspy.branch_data(44220, 44223, "1", intgar1=1) #giridih - koderma line
ierr = psspy.branch_data(44220, 44223, "2", intgar1=1)
ierr = psspy.branch_data(44218, 44231, "1", intgar1=0) #DSTPS - PARU line
ierr = psspy.branch_data(44218, 44231, "2", intgar1=0)
ierr = psspy.branch_data(44207, 44219, "1", intgar1=0) #MTPS - GOLA line
ierr = psspy.branch_data(44207, 44219, "2", intgar1=0)

#psspy.branch_data(44402, 45413, "1", intgar1=0) #KTPS - BIHARSRF line
#psspy.branch_data(44402, 45413, "2", intgar1=0) 
ierr = psspy.branch_data(44403, 45400, "1", intgar1=0) #RTPS - Ranchi line
ierr = psspy.branch_data(44403, 45400, "2", intgar1=0) 
ierr = psspy.branch_data(44404, 45404, "1", intgar1=0) #DSTPS - paruliaPG line
ierr = psspy.branch_data(44404, 45404, "2", intgar1=0) 


d, a3p = 63, (0.079018, 0.246065, 0.050086) # CTPS - Gola distance in km
lc = [0.01*d*i for i in a3p]
ierr = psspy.branch_data(44106, 44115, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #CTPS - Gola line
ierr = psspy.branch_data(44106, 44115, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])

###### Case: D/C LILO of DSTPS - PARULIA at JAMURIA
##d, a3z = 10, (0.014313, 0.086133, 0.140196) # DTPS - DSTPS distance in km
##lc = [0.01*d*i for i in a3z]
##ierr = psspy.branch_data(44203, 44231, "1", intgar1=1, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2]) #DTPS - DSTPS line
##ierr = psspy.branch_data(44203, 44231, "2", intgar1=1, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2])
##d = 32 # DSTPS - JAMU distance in km
##lc = [0.01*d*i for i in a3z]
##ierr = psspy.branch_data(44231, 44241, "1", intgar1=0, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2]) #DSTPS - JAMU line
##ierr = psspy.branch_data(44231, 44241, "2", intgar1=0, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2])
##d = 42 # JAMU2 - PARU2 distance in km
##lc = [0.01*d*i for i in a3z]
##ierr = psspy.branch_data(44241, 44218, "1", intgar1=0, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2]) #JAMU2 - PARU line
##ierr = psspy.branch_data(44241, 44218, "2", intgar1=0, realar1=lc[0],
##                         realar2=lc[1], realar3=lc[2])
##ierr = psspy.branch_data(44203, 44218, "1", intgar1=1) #DTPS - PARU line
##ierr = psspy.branch_data(44203, 44218, "2", intgar1=1)
##ierr = psspy.branch_data(44231, 44218, "1", intgar1=0) #DSTPS - PARU line
##ierr = psspy.branch_data(44231, 44218, "2", intgar1=0)

# Case specific transformer interconnections to be indicated here
psspy.two_winding_data_3(44109, 44203, "1", #DTPS_ATR1 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44203,     #WN1BUS
                         intgar10=44109,    #CONT1
                         intgar12=0,        #COD1
                         intgar13=1,        #CW
                         intgar14=3,        #CZ
                         intgar15=2,        #CM
                         realari1=190248.,   #R1-2
                         realari2=0.143545,    #X1-2
                         realari3=160.,      #SBS1-2
                         realari4=218.5/220., #WINDV1
                         realari5=230.,      #NOMV1
                         realari6=0.,        #ANG1
                         realari7=138./132.,  #WINDV2 
                         realari8=138.,       #NOMV2
                         realari16=30727.,    #MAG1
                         realari17=6.9*3.455/(230*401.63)  #MAG2
                         )
psspy.two_winding_data_3(44109, 44203, "2", #DTPS_ATR1 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44203,     #WN1BUS
                         intgar10=44109,    #CONT1
                         intgar12=0,        #COD1
                         intgar13=1,        #CW
                         intgar14=3,        #CZ
                         intgar15=2,        #CM
                         realari1=190248.,   #R1-2
                         realari2=0.143545,    #X1-2
                         realari3=160.,      #SBS1-2
                         realari4=218.5/220., #WINDV1
                         realari5=230.,      #NOMV1
                         realari6=0.,        #ANG1
                         realari7=138./132.,  #WINDV2 
                         realari8=138.,       #NOMV2
                         realari16=30727.,    #MAG1
                         realari17=6.9*3.455/(230*401.63)  #MAG2
                         )
psspy.two_winding_data_3(44109, 44203, "3", #DTPS_ATR1 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44203,     #WN1BUS
                         intgar10=44109,    #CONT1
                         intgar12=0,        #COD1
                         intgar13=1,        #CW
                         intgar14=3,        #CZ
                         intgar15=2,        #CM
                         realari1=190248.,   #R1-2
                         realari2=0.143545,    #X1-2
                         realari3=160.,      #SBS1-2
                         realari4=218.5/220., #WINDV1
                         realari5=230.,      #NOMV1
                         realari6=0.,        #ANG1
                         realari7=138./132.,  #WINDV2 
                         realari8=138.,       #NOMV2
                         realari16=30727.,    #MAG1
                         realari17=6.9*3.455/(230*401.63)  #MAG2
                         )

psspy.two_winding_data_3(44305, 44205, "1", #DGP_STR1 (EMCO-11733)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44205,     #WN1BUS
                         intgar10=44305,    #CONT1
                         intgar12=1,        #COD1
                         intgar13=1,        #CW
                         intgar14=3,        #CZ
                         intgar15=2,        #CM
                         realari1=152096.,   #R1-2
                         realari2=0.15965,    #X1-2
                         realari3=50.,      #SBS1-2
                         realari4=230./220., #WINDV1
                         realari5=230.,      #NOMV1
                         realari6=-30.,        #ANG1
                         realari7=36./33.,  #WINDV2
                         realari8=36.,       #NOMV2
                         realari16=22730.,    #MAG1
                         realari17=36.3*0.906/(230*125.51)  #MAG2
                         )
SBS12 = 50.0 #in MVA
z1 = 0.15965*(100./SBS12) #in pu
Pi2r = 137.196 #in kW
r1 = Pi2r/(10*SBS12) #in pu
x1 = math.sqrt(z1**2 - r1**2)
z0 = 0.13712*2 #in pu
r0 = z0/np.sqrt(1+(x1/r1)**2)
x0 = r0*(x1/r1)
psspy.seq_two_winding_data_3(44305, 44205, "1", #DGP_STR1 (EMCO-11733)
                             intgar1=12, intgar2=2, intgar3=2,
                             realar3=r0, realar4=x0)

# Base Generation ---------------------------------
ierr = psspy.machine_data_2(44004, realar1=180.) #BTPSB gen1
ierr = psspy.machine_data_2(44005, realar1=180.) #BTPSB gen2
ierr = psspy.machine_data_2(44006, realar1=180.) #BTPSB gen3
ierr = psspy.machine_data_2(44008, realar1=180.) #DTPS gen4
ierr = psspy.machine_data_2(44009, realar1=98.) #DTPS gen3
ierr = psspy.machine_data_2(44010, intgar1=0) #BKROA gen1
ierr = psspy.machine_data_2(44013, realar1=450.) #MTPSB gen1
ierr = psspy.machine_data_2(44014, realar1=450.) #MTPSB gen2
ierr = psspy.machine_data_2(44015, realar1=100.) #CTPS gen1
ierr = psspy.machine_data_2(44016, realar1=100.) #CTPS gen2
ierr = psspy.machine_data_2(44017, realar1=100.) #CTPS gen3
ierr = psspy.machine_data_2(44018, realar1=225.) #CTPS gen7
ierr = psspy.machine_data_2(44019, realar1=225.) #CTPS gen8
ierr = psspy.machine_data_2(44020, realar1=180.) #MTPS gen1
ierr = psspy.machine_data_2(44021, realar1=180.) #MTPS gen2
ierr = psspy.machine_data_2(44022, realar1=180.) #MTPS gen3
ierr = psspy.machine_data_2(44023, realar1=180.) #MTPS gen4
ierr = psspy.machine_data_2(44024, realar1=225.) #MTPS gen5
ierr = psspy.machine_data_2(44025, realar1=225.) #MTPS gen6
ierr = psspy.machine_data_2(44026, realar1=400.) #KTPS gen1
ierr = psspy.machine_data_2(44027, intgar1=0) #KTPS gen2
ierr = psspy.machine_data_2(44032, realar1=450.) #DSTPS gen1
ierr = psspy.machine_data_2(44033, intgar1=0) #DSTPS gen2
psspy.machine_data_2(44030, intgar1=0) #RTPS gen1
psspy.machine_data_2(44031, intgar1=0) #RTPS gen2
psspy.machine_data_2(44034, intgar1=0) #RTPS gen3
psspy.machine_data_2(44035, intgar1=0) #RTPS gen4
###-------------------------------

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



def run_psse():
    ierr = psspy.bsys(sid=1, numzone=1, zones=44)
    ierr, all_buses = psspy.abusint(sid=1, string=["NUMBER"], flag=2)
    all_buses = all_buses[0]
    ierr, in_buses = psspy.abusint(sid=1, string=['NUMBER'], flag=1)
    in_buses = in_buses[0]
    out_buses = list(set(all_buses)-set(in_buses))
    ierr = psspy.bsys(sid=2, numbus=len(out_buses), buses=out_buses)
    ierr = psspy.extr(sid=2, all=0, status2=0)
    
    status, scalval = [0,1,4,0], []
    ierr, totals, moto = psspy.scal(sid=1, all=0, apiopt=1, status=status,
                                    scalval=scalval)
    scalval = [0.,0.,totals[2],totals[3],totals[4],totals[5],0.95]
    ierr, totals, moto = psspy.scal(sid=1, all=0, apiopt=2, status=status,
                                    scalval=scalval)

    psspy.solution_parameters_3(intgar2=150, realar6=1.0) #, realar17=10.1, realar18=10.00001)
    #psspy.solv((1,0,0,0,0,0))
    psspy.fdns(options6=0) # 1 = flat start
    psspy.fnsl((1,0,0,0,0,0,99,1))
    #psspy.solv((1,0,0,0,0,0))
    #psspy.fnsl((1,0,0,0,0,0,99,1))
    #psspy.pout(sid=1, all=0)
    #n = psspy.totbus()
    #psspy.ascc_3(sid=1, all=0, status1=1, status11=1, scfile="scfile.sc")
    #psspy.ascc_scfile("scfile.sc")

    businfo = subsystem_info('bus', ['NUMBER', 'BASE', 'NAME'], sid=-1) #get list of all busses in the study file
    mybusinfo = subsystem_info('bus', ['NUMBER', 'BASE', 'NAME'], sid=1)
    mygeninfo = subsystem_info('mach', ['NUMBER', 'PGEN', 'NAME'], sid=1)
    myloadinfo = subsystem_info('load', ['NUMBER', 'MVAACT', 'NAME'], sid=1)
    branchinfo = subsystem_info('brn', ['FROMNUMBER', 'TONUMBER', 'MVA', 'P'], sid=1)
    trfinfo = subsystem_info('trn', ['FROMNUMBER', 'TONUMBER', 'MVA', 'P'], sid=1)

    a = list(reduce(tuple.__add__,[x[:2] for x in branchinfo])) #get all the bus info from the in service branches in my zone
    b = list(reduce(tuple.__add__,[x[:2] for x in trfinfo])) #get all the bus info from the in service transfomers in my zone
    c = [x[0] for x in mybusinfo]
    d = [x[0] for x in mygeninfo]
    mybusdat = list(set(a+b+c))
    rbusdat = list(set(mybusdat).difference(d)) #my bus list sans my gen busses
    rbusinfo = [i for i in businfo for j in rbusdat if i[0]==j] #get the full details of each bus
    tiebusdat = list(set(a)-set(c)) 
    #print mybusinfo
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

    totgen = psspy.zndat(44, "GEN")
    totload = psspy.zndat(44, "LOAD")
    
    args = (businfo, mybusdat, rbusinfo, rgenbus, myloadinfo, brnflow,
            trfflow, totgen, totload, tiebusdat)
    return  args

if __name__ == '__main__':
    args = run_psse()
    

