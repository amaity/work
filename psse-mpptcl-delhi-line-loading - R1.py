from __future__ import with_statement
from contextlib import contextmanager
import os,sys
import operator
from itertools import chain

##PSSE_LOCATION = r"C:\Program Files\PTI\PSSE32\PSSBIN"
PSSE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION 

import psspy

import redirect
redirect.psse2py()
#--------------------------------
# PSS/E Saved case

##CASE = r"C:\Program Files\PTI\PSSE32\EXAMPLE\DVC_ACTUALR1.sav"
CASE = r"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\DVC_ACTUALR1.sav"
psspy.psseinit(8000)
psspy.case(CASE)

psspy.solution_parameters_3(intgar1=120, intgar2=20)

#--------------------------------
# Initialisation
# CD as on 31.3.2013
ierr = psspy.load_data_3(44100, realar1=44.6) #BOKARO
ierr = psspy.load_data_3(44101, realar1=24.4) #MOSABANI
ierr = psspy.load_data_3(44102, realar1=121.8) #BURDWAN
ierr = psspy.load_data_3(44103, realar1=41.0) #BELMURI
ierr = psspy.load_data_3(44104, realar1=15.0) #HOWRAH
ierr = psspy.load_data_3(44105, realar1=17.0) #KHARAGPUR
ierr = psspy.load_data_3(44106, realar1=351.0) #CHANDRAPURA
ierr = psspy.load_data_3(44107, realar1=10.0) #KOLAGHAT
ierr = psspy.load_data_3(44108, realar1=140.0) #JAMSHEDPUR
ierr = psspy.load_data_3(44101, realar1=42.2) #DTPS
ierr = psspy.load_data_3(44110, realar1=20.0) #BARHI
ierr = psspy.load_data_3(44111, realar1=57.4) #MAITHON HYDEL
ierr = psspy.load_data_3(44112, realar1=17.6) #PANCHET HYDEL
ierr = psspy.load_data_3(44113, realar1=88.15) #KODERMA
ierr = psspy.load_data_3(44114, realar1=30.0) #HAZARIBAGH
ierr = psspy.load_data_3(44115, realar1=36.35) #GOLA
ierr = psspy.load_data_3(44117, realar1=133.3) #PUTKI
ierr = psspy.load_data_3(44118, realar1=140.0) #KALIPAHARI
ierr = psspy.load_data_3(44119, realar1=55.3) #ASP
ierr = psspy.load_data_3(44120, realar1=111.0) #RAMGARH
ierr = psspy.load_data_3(44121, realar1=139.3) #KALYANESWARI
ierr = psspy.load_data_3(44122, realar1=89.6) #KUMARDUBI
ierr = psspy.load_data_3(44123, realar1=158.0) #PATHERDIH
ierr = psspy.load_data_3(44124, realar1=27.5) #NIMIAGHAT
ierr = psspy.load_data_3(44125, realar1=145.2) #GIRIDIH
ierr = psspy.load_data_3(44126, realar1=26.25) #SINDRI
ierr = psspy.load_data_3(44127, realar1=32.5) #RAMKANALI
ierr = psspy.load_data_3(44128, realar1=38.0) #PATRATU
ierr = psspy.load_data_3(44129, realar1=46.5) #NORTH KARANPURA
ierr = psspy.load_data_3(44133, realar1=15.0) #PURULIA
ierr = psspy.load_data_3(44134, realar1=57.0) #JAMURIA
ierr = psspy.load_data_3(44135, realar1=23.5) #KONAR
ierr = psspy.load_data_3(44205, realar1=167.35) #DURGAPUR
ierr = psspy.load_data_3(44206, realar1=36.0) #DHANBAD
ierr = psspy.load_data_3(44207, realar1=70.2) #MTPS
ierr = psspy.load_data_3(44208, realar1=93.0) #BURNPUR
ierr = psspy.load_data_3(44209, realar1=43.0) #RAMGARH2
ierr = psspy.load_data_3(44217, realar1=186.5) #BORJORA
ierr = psspy.load_data_3(44218, realar1=160.8) #PARULIA

ierr = psspy.machine_data_2(44004, realar1=180.0) #BTPSG1
ierr = psspy.machine_data_2(44005, realar1=180.0) #BTPSG2
ierr = psspy.machine_data_2(44006, realar1=180.0) #BTPSG3
ierr = psspy.machine_data_2(44008, realar1=180.0) #DTPSG4
ierr = psspy.machine_data_2(44009, realar1=110.0) #DTPSG3
ierr = psspy.machine_data_2(44015, realar1=100.0) #CTPSG1
ierr = psspy.machine_data_2(44016, realar1=100.0) #CTPSG2
ierr = psspy.machine_data_2(44017, realar1=100.0) #CTPSG3
ierr = psspy.machine_data_2(44020, realar1=180.0) #MTPSG1
ierr = psspy.machine_data_2(44021, realar1=180.0) #MTPSG2
ierr = psspy.machine_data_2(44022, realar1=180.0) #MTPSG3
ierr = psspy.machine_data_2(44023, realar1=180.0) #MTPSG4
ierr = psspy.machine_data_2(45201, realar1=0.0) #PARULIAPG
ierr = psspy.machine_data_2(45205, realar1=0.0) #MAITHONPG

ierr = psspy.bus_data_2(45201, intgar1=1)
ierr = psspy.bus_data_2(45205, intgar1=3)

#-------------------------------------------------
# Local functions

@contextmanager
def silence(file_object=None):
    """
    Discard stdout (i.e. write to null device) or
    optionally write to given file-like object.
    """
    if file_object is None:
        file_object = open(os.devnull, 'w')

    old_stdout = sys.stdout
    try:
        sys.stdout = file_object
        yield
    finally:
        sys.stdout = old_stdout

def scaleLoadGen(sid, percentLoad, powerfactor, percentGen):
#    if not psspy.bsysdef(sid):
#        return False
    scalingMethodFlag = 2
    enforceMachineLimitsFlag = 1
    reactiveLoadScalingFlag = 4
    scaledBusesFlag = 0
    status = [scalingMethodFlag, enforceMachineLimitsFlag, reactiveLoadScalingFlag, 0]

    apiopt = 1
    scalval = []
    ierr, totals, moto = psspy.scal(sid, scaledBusesFlag, apiopt, status, scalval)
    if ierr<>0:
        return ierr

    scalval.append(percentLoad)
    scalval.append(percentGen)
    scalval.append(totals[2])
    scalval.append(totals[3])
    scalval.append(totals[4])
    scalval.append(totals[5])
    scalval.append(powerfactor)
    apiopt = 2
    ierr, totals, moto = psspy.scal(sid, scaledBusesFlag, apiopt, status, scalval)
    if ierr<>0:
        return ierr
    return True

from prettytable import PrettyTable
def add_data():
    x = PrettyTable(["Line name", "Flow in MW", "% Loading"])
    x.align["Line name"] = "l"
    x.align["% Loading"] = "r"
    x.align["Flow in MW"] = "r"
    ierr, cmpval = psspy.brnflo(44204, 45205, '1')
    x.add_row(["Kalyaneswari - MaithonPG line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44204, 45205, '2')
    x.add_row(["Kalyaneswari - MaithonPG line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44206, 45205, '1')
    x.add_row(["Dhanbad - MaithonPG line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44206, 45205, '2')
    x.add_row(["Dhanbad - MaithonPG line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44202, 44206, '1')
    x.add_row(["Chandrapura - Dhanbad line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44202, 44206, '2')
    x.add_row(["Chandrapura - Dhanbad line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44202, 44204, '3')
    x.add_row(["Chandrapura - Kalyaneswari line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44202, 44204, '4')
    x.add_row(["Chandrapura - Kalyaneswari line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44207, 44208, '1')
    x.add_row(["Mejia - Burnpur line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44204, 44208, '1')
    x.add_row(["Kalyaneswari - Burnpur line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44204, 44207, '1')
    x.add_row(["Kalyaneswari - Mejia line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44204, 44207, '2')
    x.add_row(["Kalyaneswari - Mejia line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44204, 44207, '3')
    x.add_row(["Kalyaneswari - Mejia line3", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44218, 45201, '1')
    x.add_row(["ParuliaDVC - ParuliaPG line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44218, 45201, '2')
    x.add_row(["ParuliaDVC - ParuliaPG line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44205, 44218, '1')
    x.add_row(["Durgapur - Parulia line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44205, 44218, '2')
    x.add_row(["Durgapur - Parulia line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44203, 44218, '1')
    x.add_row(["DTPS - Parulia line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44203, 44218, '2')
    x.add_row(["DTPS - Parulia line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44207, 44205, '1')
    x.add_row(["Mejia - Durgapur line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44207, 44205, '2')
    x.add_row(["Mejia - Durgapur line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44207, 44203, '1')
    x.add_row(["Mejia - DTPS line1", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    ierr, cmpval = psspy.brnflo(44207, 44203, '2')
    x.add_row(["Mejia - DTPS line2", round(cmpval.real, 3), round(cmpval.real*100.0/186.0, 3)])
    mystr = x.get_string()
    return(mystr)

def flattened(l):
    return reduce(lambda x,y: x+[y] if type(y) != list else x+flattened(y), l,[])

def add_load_data():
    x = PrettyTable(["Bus name", "Load (MW)", "Load (MVar)"])
    x.align["Bus name"] = "l"
    x.align["Load (MW)"] = "r"
    x.align["Load (MVar)"] = "r"
    ierr, xarray = psspy.alodbuscplx(flag=1, string='TOTALACT')
    ierr, carray = psspy.alodbuschar(flag=1, string='NAME')
    for i in zip(flattened(carray),flattened(xarray)):
        x.add_row([i[0],round(i[1].real,1),round(i[1].imag,1)])
    mystr = x.get_string()
    return(mystr)

def trans_chrgs_calc():
    x = PrettyTable(["Line name", "Line length", "Base case", "With Exp. Load", "Diff.", "Tr. Chrgs.", "Prop. chrgs." ,"Losses", "Prop. losses"] )
    x.align["Line name"] = "l"
    x.align["Line length"] = "r"
    x.align["Base case"] = "r"
    x.align["With Exp. Load"] = "r"
    x.align["Diff."] = "r"
    x.align["Tr. Chrgs."] = "r"
    x.align["Prop. chrgs."] = "r"
    x.align["Losses"] = "r"
    x.align["Prop. losses"] = "r"
    tott = 0
    totl = 0
    for i in flowarr:
        if i[2]>0 and i[3]>0 and i[3]>i[2]:
            diff = i[3]-i[2]
        elif i[2]<0 and i[3]<0 and abs(i[3])>abs(i[2]):
            diff = abs(i[3])-abs(i[2])
        elif i[2]<0 and i[3]<0 and abs(i[2])>abs(i[3]):
            diff = abs(i[3])-abs(i[2])
        elif i[2]<0 and i[3]>0 and abs(i[2])>i[3]:
            diff = abs(i[3])-abs(i[2])
        elif i[2]<0 and i[3]>0 and abs(i[2])<i[3]:
            diff = i[3]-abs(i[2])
        elif i[2]>0 and i[3]<0 and i[2]<abs(i[3]):
            diff = abs(i[3])-i[2]
        prtr = 13.49*i[1]*100/(2*50*1000.0) 
        prlo = i[1]*0.5/50.0
        x.add_row([i[0],i[1],i[2],i[3],diff,prtr,round(diff*prtr/100.0,4),prlo,round(diff*prlo/100.0,4)])
        tott = tott+(diff*prtr/100.0)
        totl = totl+(diff*prlo/100.0)
    x.add_row(['','','','','','Total',round(tott,4),'Total',round(totl,4)])
    mystr = x.get_string()
    return mystr
    
print 'Scenario-0 ----------------------------'
with open('output.txt','w') as fout:
    fout.write('Scenario-0\n')
    fout.write('----------\n')

psspy.fnsl()
ierr = psspy.bsys(sid=1, numzone=1, zones=44)
##ierr, loads = psspy.aloadreal(sid=1, flag=1, string='MVAACT')
##print loads
##ierr, gens = psspy.amachreal(sid=1, flag=1, string='PGEN')
##print gens
with silence(open('output.txt','a')):
    scaleLoadGen(1, -30.0, 0.9, -0.0)
with open('output.txt','a') as fout:
    fout.write('\n\n')


psspy.solv()
psspy.fnsl()
psspy.area_2(0,1,1)

with open('output.txt','a') as fout:
    fout.write(add_load_data())
    fout.write('\n\n')
    

ierr, ctpsg7 = psspy.gendat(44025)
ierr, ctpsg8 = psspy.gendat(44026)
ierr, mtpsg5 = psspy.gendat(44024)
ierr, mtpsg6 = psspy.gendat(44027)
with open('output.txt','a') as fout:
    fout.write('CTPS Gen7 loaded to %s \n' % round(ctpsg7.real, 3))
    fout.write('CTPS Gen8 loaded to %s \n' % round(ctpsg8.real, 3))
    fout.write('MTPS Gen5 loaded to %s \n' % round(mtpsg5.real, 3))
    fout.write('MTPS Gen6 loaded to %s \n' % round(mtpsg6.real, 3))
    fout.write('\n')

with open('output.txt','a') as fout:
    fout.write(add_data())
    fout.write('\n\n')

psspy.report_output(islct=2, filarg="./output.txt", options=[2])
psspy.asys(sid=1,num=1,areas=4)
psspy.ties(1,0)
psspy.report_output(islct=2, options=[0])
with open('output.txt','a') as fout:
    fout.write('\n\n')


flowarr=[['KLYN-MTHNPG L1',7.6],['KLYN-MTHNPG L2',7.6],['DHN-MTHNPG L1',45],['DHN-MTHNPG L2',45],
         ['CTPS-DHN L1',45.6],['CTPS-DHN L2',45.6],['CTPS-KLYN L1',141.8],['CTPS-KLYN L2',141.8],
         ['MTPS-BRNPR L1',58.23],['KLYN-BRNPR L1',22],['KLYN-MTPS L1',55],['KLYN-MTPS L2',79.2],
         ['KLYN-MTPS L3',79.2],['PARU-DGPPG L1',1],['PARU-DGPPG L2',1],['DGPDVC-PARU L1',16.5],
         ['DGPDVC-PARU L2',16.5],['DTPS-PARU L1',22],['DTPS-PARU L2',22],['MTPS-DGPDVC L1',31.45],
         ['MTPS-DGPDVC L2',31.45],['MTPS-DTPS L1',42],['MTPS-DTPS L2',42]]


ierr, rval = psspy.brnmsc(44204, 45205, '1', 'MVA')
ierr, cmpval1 = psspy.brnflo(44204, 45205, '1')
print 'Kalyaneswari - MaithonPG line1 loading in MW & MVar = ', cmpval1
print 'Kalyaneswari - MaithonPG line1 loading in % = ', cmpval1.real*100.0/186.0
flowarr[0].append(cmpval1.real*100.0/186.0)
ierr, cmpval2 = psspy.brnflo(44204, 45205, '2')
print 'Kalyaneswari - MaithonPG line2 loading in MW & MVar = ', cmpval2
print 'Kalyaneswari - MaithonPG line2 loading in % = ', cmpval2.real*100.0/186.0
flowarr[1].append(cmpval2.real*100.0/186.0)
ierr, cmpval3 = psspy.brnflo(44206, 45205, '1')
print 'Dhanbad - MaithonPG line1 loading in MW & MVar = ', cmpval3
print 'Dhanbad - MaithonPG line1 loading in % = ', cmpval3.real*100.0/186.0
flowarr[2].append(cmpval3.real*100.0/186.0)
ierr, cmpval4 = psspy.brnflo(44206, 45205, '2')
print 'Dhanbad - MaithonPG line2 loading in MW & MVar = ', cmpval4
print 'Dhanbad - MaithonPG line2 loading in % = ', cmpval4.real*100.0/186.0
flowarr[3].append(cmpval4.real*100.0/186.0)
ierr, cmpval5 = psspy.brnflo(44202, 44206, '1')
print 'Chandrapura - Dhanbad line1 loading in MW & MVar = ', cmpval5
print 'Chandrapura - Dhanbad line1 loading in % = ', cmpval5.real*100.0/186.0
flowarr[4].append(cmpval5.real*100.0/186.0)
ierr, cmpval6 = psspy.brnflo(44202, 44206, '2')
print 'Chandrapura - Dhanbad line2 loading in MW & MVar = ', cmpval6
print 'Chandrapura - Dhanbad line2 loading in % = ', cmpval6.real*100.0/186.0
flowarr[5].append(cmpval6.real*100.0/186.0)
ierr, cmpval7 = psspy.brnflo(44202, 44204, '3')
print 'Chandrapura - Kalyaneswari line1 loading in MW & MVar = ', cmpval7
print 'Chandrapura - Kalyaneswari line1 loading in % = ', cmpval7.real*100.0/186.0
flowarr[6].append(cmpval7.real*100.0/186.0)
ierr, cmpval8 = psspy.brnflo(44202, 44204, '4')
print 'Chandrapura - Kalyaneswari line2 loading in MW & MVar = ', cmpval8
print 'Chandrapura - Kalyaneswari line2 loading in % = ', cmpval8.real*100.0/186.0
flowarr[7].append(cmpval8.real*100.0/186.0)
ierr, cmpval9 = psspy.brnflo(44207, 44208, '1')
print 'Mejia - Burnpur line1 loading in MW & MVar = ', cmpval9
print 'Mejia - Burnpur line1 loading in % = ', cmpval9.real*100.0/186.0
flowarr[8].append(cmpval9.real*100.0/186.0)
ierr, cmpval11 = psspy.brnflo(44204, 44208, '1')
print 'Kalyaneswari - Burnpur line1 loading in MW & MVar = ', cmpval11
print 'Kalyaneswari - Burnpur line1 loading in % = ', cmpval11.real*100.0/186.0
flowarr[9].append(cmpval11.real*100.0/186.0)
ierr, cmpval13 = psspy.brnflo(44204, 44207, '1')
print 'Kalyaneswari - Mejia line1 loading in MW & MVar = ', cmpval13
print 'Kalyaneswari - Mejia line1 loading in % = ', cmpval13.real*100.0/186.0
flowarr[10].append(cmpval13.real*100.0/186.0)
ierr, cmpval14 = psspy.brnflo(44204, 44207, '2')
print 'Kalyaneswari - Mejia line2 loading in MW & MVar = ', cmpval14
print 'Kalyaneswari - Mejia line2 loading in % = ', cmpval14.real*100.0/186.0
flowarr[11].append(cmpval14.real*100.0/186.0)
ierr, cmpval15 = psspy.brnflo(44204, 44207, '3')
print 'Kalyaneswari - Mejia line3 loading in MW & MVar = ', cmpval15
print 'Kalyaneswari - Mejia line3 loading in % = ', cmpval15.real*100.0/186.0
flowarr[12].append(cmpval15.real*100.0/186.0)
print '\n'

ierr, cmpval16 = psspy.brnflo(44218, 45201, '1')
print 'ParuliaDVC - ParuliaPG line1 loading in MW & MVar = ', cmpval16
print 'ParuliaDVC - ParuliaPG line1 loading in % = ', cmpval16.real*100.0/186.0
flowarr[13].append(cmpval16.real*100.0/186.0)
ierr, cmpval17 = psspy.brnflo(44218, 45201, '2')
print 'ParuliaDVC - ParuliaPG line2 loading in MW & MVar = ', cmpval17
print 'ParuliaDVC - ParuliaPG line2 loading in % = ', cmpval17.real*100.0/186.0
flowarr[14].append(cmpval17.real*100.0/186.0)
ierr, cmpval18 = psspy.brnflo(44205, 44218, '1')
print 'Durgapur - Parulia line1 loading in MW & MVar = ', cmpval18
print 'Durgapur - Parulia line1 loading in % = ', cmpval18.real*100.0/186.0
flowarr[15].append(cmpval18.real*100.0/186.0)
ierr, cmpval19 = psspy.brnflo(44205, 44218, '2')
print 'Durgapur - Parulia line2 loading in MW & MVar = ', cmpval19
print 'Durgapur - Parulia line2 loading in % = ', cmpval19.real*100.0/186.0
flowarr[16].append(cmpval19.real*100.0/186.0)
ierr, cmpval20 = psspy.brnflo(44203, 44218, '1')
print 'DTPS - Parulia line1 loading in MW & MVar = ', cmpval20
print 'DTPS - Parulia line1 loading in % = ', cmpval20.real*100.0/186.0
flowarr[17].append(cmpval20.real*100.0/186.0)
ierr, cmpval21 = psspy.brnflo(44203, 44218, '2')
print 'DTPS - Parulia line2 loading in MW & MVar = ', cmpval21
print 'DTPS - Parulia line2 loading in % = ', cmpval21.real*100.0/186.0
flowarr[18].append(cmpval21.real*100.0/186.0)
ierr, cmpval22 = psspy.brnflo(44207, 44205, '1')
print 'Mejia - Durgapur line1 loading in MW & MVar = ', cmpval22
print 'Mejia - Durgapur line1 loading in % = ', cmpval22.real*100.0/186.0
flowarr[19].append(cmpval22.real*100.0/186.0)
ierr, cmpval23 = psspy.brnflo(44207, 44205, '2')
print 'Mejia - Durgapur line2 loading in MW & MVar = ', cmpval23
print 'Mejia - Durgapur line2 loading in % = ', cmpval23.real*100.0/186.0
flowarr[20].append(cmpval23.real*100.0/186.0)
ierr, cmpval24 = psspy.brnflo(44207, 44203, '1')
print 'Mejia - DTPS line1 loading in MW & MVar = ', cmpval24
print 'Mejia - DTPS line1 loading in % = ', cmpval24.real*100.0/186.0
flowarr[21].append(cmpval24.real*100.0/186.0)
ierr, cmpval25 = psspy.brnflo(44207, 44203, '2')
print 'Mejia - DTPS line2 loading in MW & MVar = ', cmpval25
print 'Mejia - DTPS line2 loading in % = ', cmpval25.real*100.0/186.0
flowarr[22].append(cmpval25.real*100.0/186.0)
print '\n'
print 'flowarr =', flowarr

##psspy.report_output(islct=2, filarg="./output.txt", options=[2])
##psspy.pout()
##psspy.report_output(islct=2, options=[0])
##with open('output.txt','a') as fout:
##    fout.write('\n\n')

    
print 'Scenario-1 ----------------------------'
with open('output.txt','a') as fout:
    fout.write('Scenario-1\n')
    fout.write('----------\n')
    
ierr = psspy.load_data_3(45201, realar1=200.0)
ierr = psspy.load_data_3(45205, realar1=200.0)
##ierr = psspy.machine_data_2(44025, realar1=100.0) #CTPS gen7
##ierr = psspy.machine_data_2(44026, realar1=100.0) #CTPS gen8
##ierr = psspy.machine_data_2(44024, realar1=100.0) #MTPS gen5
##ierr = psspy.machine_data_2(44027, realar1=100.0) #MTPS gen6
ierr = psspy.machine_data_2(44025, realar1=150.0) #CTPS gen7
ierr = psspy.machine_data_2(44026, realar1=150.0) #CTPS gen8
ierr = psspy.machine_data_2(44024, realar1=0.0) #MTPS gen5
ierr = psspy.machine_data_2(44027, realar1=100.0) #MTPS gen6

ierr, loddurgpg = psspy.loddt2(45201,'1','MVA','ACT')
ierr, lodmthnpg = psspy.loddt2(45205,'1','MVA','ACT')
ierr, ctpsg7 = psspy.gendat(44025)
ierr, ctpsg8 = psspy.gendat(44026)
ierr, mtpsg5 = psspy.gendat(44024)
ierr, mtpsg6 = psspy.gendat(44027)
with open('output.txt','a') as fout:
    fout.write('MVA load added to DurgapurPG %s \n' % loddurgpg)
    fout.write('MVA load added to MaithonPG %s \n' % lodmthnpg)
    fout.write('CTPS Gen7 load in MW is %s \n' % round(ctpsg7.real, 3))
    fout.write('CTPS Gen8 load in MW is %s \n' % round(ctpsg8.real, 3))
    fout.write('MTPS Gen5 load in MW is %s \n' % round(mtpsg5.real, 3))
    fout.write('MTPS Gen6 load in MW is %s \n' % round(mtpsg6.real, 3))
    fout.write('\n\n')


psspy.fnsl()
psspy.area_2(0,1,1)


cmpvalarr2=[]
ierr, rval = psspy.brnmsc(44204, 45205, '1', 'MVA')
ierr, cmpval1 = psspy.brnflo(44204, 45205, '1')
print 'Kalyaneswari - MaithonPG line1 loading in MW & MVar = ', cmpval1
print 'Kalyaneswari - MaithonPG line1 loading in % = ', cmpval1.real*100.0/186.0
cmpvalarr2.append(cmpval1.real)
ierr, cmpval2 = psspy.brnflo(44204, 45205, '2')
print 'Kalyaneswari - MaithonPG line2 loading in MW & MVar = ', cmpval2
print 'Kalyaneswari - MaithonPG line2 loading in % = ', cmpval2.real*100.0/186.0
cmpvalarr2.append(cmpval2.real)
ierr, cmpval3 = psspy.brnflo(44206, 45205, '1')
print 'Dhanbad - MaithonPG line1 loading in MW & MVar = ', cmpval3
print 'Dhanbad - MaithonPG line1 loading in % = ', cmpval3.real*100.0/186.0
cmpvalarr2.append(cmpval3.real)
ierr, cmpval4 = psspy.brnflo(44206, 45205, '2')
print 'Dhanbad - MaithonPG line2 loading in MW & MVar = ', cmpval4
print 'Dhanbad - MaithonPG line2 loading in % = ', cmpval4.real*100.0/186.0
cmpvalarr2.append(cmpval4.real)
ierr, cmpval5 = psspy.brnflo(44202, 44206, '1')
print 'Chandrapura - Dhanbad line1 loading in MW & MVar = ', cmpval5
print 'Chandrapura - Dhanbad line1 loading in % = ', cmpval5.real*100.0/186.0
cmpvalarr2.append(cmpval5.real)
ierr, cmpval6 = psspy.brnflo(44202, 44206, '2')
print 'Chandrapura - Dhanbad line2 loading in MW & MVar = ', cmpval6
print 'Chandrapura - Dhanbad line2 loading in % = ', cmpval6.real*100.0/186.0
cmpvalarr2.append(cmpval6.real)
ierr, cmpval7 = psspy.brnflo(44202, 44204, '3')
print 'Chandrapura - Kalyaneswari line1 loading in MW & MVar = ', cmpval7
print 'Chandrapura - Kalyaneswari line1 loading in % = ', cmpval7.real*100.0/186.0
cmpvalarr2.append(cmpval7.real)
ierr, cmpval8 = psspy.brnflo(44202, 44204, '4')
print 'Chandrapura - Kalyaneswari line2 loading in MW & MVar = ', cmpval8
print 'Chandrapura - Kalyaneswari line2 loading in % = ', cmpval8.real*100.0/186.0
cmpvalarr2.append(cmpval8.real)
ierr, cmpval9 = psspy.brnflo(44207, 44208, '1')
print 'Mejia - Burnpur line1 loading in MW & MVar = ', cmpval9
print 'Mejia - Burnpur line1 loading in % = ', cmpval9.real*100.0/186.0
cmpvalarr2.append(cmpval9.real)
ierr, cmpval11 = psspy.brnflo(44204, 44208, '1')
print 'Kalyaneswari - Burnpur line1 loading in MW & MVar = ', cmpval11
print 'Kalyaneswari - Burnpur line1 loading in % = ', cmpval11.real*100.0/186.0
cmpvalarr2.append(cmpval11.real)
ierr, cmpval13 = psspy.brnflo(44204, 44207, '1')
print 'Kalyaneswari - Mejia line1 loading in MW & MVar = ', cmpval13
print 'Kalyaneswari - Mejia line1 loading in % = ', cmpval13.real*100.0/186.0
cmpvalarr2.append(cmpval13.real)
ierr, cmpval14 = psspy.brnflo(44204, 44207, '2')
print 'Kalyaneswari - Mejia line2 loading in MW & MVar = ', cmpval14
print 'Kalyaneswari - Mejia line2 loading in % = ', cmpval14.real*100.0/186.0
cmpvalarr2.append(cmpval14.real)
ierr, cmpval15 = psspy.brnflo(44204, 44207, '3')
print 'Kalyaneswari - Mejia line3 loading in MW & MVar = ', cmpval15
print 'Kalyaneswari - Mejia line3 loading in % = ', cmpval15.real*100.0/186.0
cmpvalarr2.append(cmpval15.real)
print '\n'

ierr, cmpval16 = psspy.brnflo(44218, 45201, '1')
print 'ParuliaDVC - ParuliaPG line1 loading in MW & MVar = ', cmpval16
print 'ParuliaDVC - ParuliaPG line1 loading in % = ', cmpval16.real*100.0/186.0
cmpvalarr2.append(cmpval16.real)
ierr, cmpval17 = psspy.brnflo(44218, 45201, '2')
print 'ParuliaDVC - ParuliaPG line2 loading in MW & MVar = ', cmpval17
print 'ParuliaDVC - ParuliaPG line2 loading in % = ', cmpval17.real*100.0/186.0
cmpvalarr2.append(cmpval17.real)
ierr, cmpval18 = psspy.brnflo(44205, 44218, '1')
print 'Durgapur - Parulia line1 loading in MW & MVar = ', cmpval18
print 'Durgapur - Parulia line1 loading in % = ', cmpval18.real*100.0/186.0
cmpvalarr2.append(cmpval18.real)
ierr, cmpval19 = psspy.brnflo(44205, 44218, '2')
print 'Durgapur - Parulia line2 loading in MW & MVar = ', cmpval19
print 'Durgapur - Parulia line2 loading in % = ', cmpval19.real*100.0/186.0
cmpvalarr2.append(cmpval19.real)
ierr, cmpval20 = psspy.brnflo(44203, 44218, '1')
print 'DTPS - Parulia line1 loading in MW & MVar = ', cmpval20
print 'DTPS - Parulia line1 loading in % = ', cmpval20.real*100.0/186.0
cmpvalarr2.append(cmpval20.real)
ierr, cmpval21 = psspy.brnflo(44203, 44218, '2')
print 'DTPS - Parulia line2 loading in MW & MVar = ', cmpval21
print 'DTPS - Parulia line2 loading in % = ', cmpval21.real*100.0/186.0
cmpvalarr2.append(cmpval21.real)
ierr, cmpval22 = psspy.brnflo(44207, 44205, '1')
print 'Mejia - Durgapur line1 loading in MW & MVar = ', cmpval22
print 'Mejia - Durgapur line1 loading in % = ', cmpval22.real*100.0/186.0
cmpvalarr2.append(cmpval22.real)
ierr, cmpval23 = psspy.brnflo(44207, 44205, '2')
print 'Mejia - Durgapur line2 loading in MW & MVar = ', cmpval23
print 'Mejia - Durgapur line2 loading in % = ', cmpval23.real*100.0/186.0
cmpvalarr2.append(cmpval23.real)
ierr, cmpval24 = psspy.brnflo(44207, 44203, '1')
print 'Mejia - DTPS line1 loading in MW & MVar = ', cmpval24
print 'Mejia - DTPS line1 loading in % = ', cmpval24.real*100.0/186.0
cmpvalarr2.append(cmpval24.real)
ierr, cmpval25 = psspy.brnflo(44207, 44203, '2')
print 'Mejia - DTPS line2 loading in MW & MVar = ', cmpval25
print 'Mejia - DTPS line2 loading in % = ', cmpval25.real*100.0/186.0
cmpvalarr2.append(cmpval25.real)
print '\n'


with open('output.txt','a') as fout:
    fout.write(add_data())
    fout.write('\n\n')


psspy.report_output(islct=2, filarg="./output.txt", options=[2])
psspy.asys(sid=1,num=1,areas=4)
psspy.ties(1,0)
psspy.report_output(islct=2, options=[0])
with open('output.txt','a') as fout:
    fout.write('\n\n')

    
##psspy.report_output(islct=2, filarg="./output.txt", options=[2])
##psspy.pout()
##psspy.report_output(islct=2, options=[0])
##with open('output.txt','a') as fout:
##    fout.write('\n\n')


print 'Scenario-2 ----------------------------'
with open('output.txt','a') as fout:
    fout.write('Scenario-2\n')
    fout.write('----------\n')

ierr = psspy.load_data_3(45201, realar1=300.0)
ierr = psspy.load_data_3(45205, realar1=500.0)
ierr = psspy.machine_data_2(44025, realar1=250.0) #CTPS gen7
ierr = psspy.machine_data_2(44026, realar1=250.0) #CTPS gen8
ierr = psspy.machine_data_2(44024, realar1=100.0) #MTPS gen5
ierr = psspy.machine_data_2(44027, realar1=200.0) #MTPS gen6
ierr, loddurgpg = psspy.loddt2(45201,'1','MVA','ACT')
ierr, lodmthnpg = psspy.loddt2(45205,'1','MVA','ACT')
ierr, ctpsg7 = psspy.gendat(44025)
ierr, ctpsg8 = psspy.gendat(44026)
ierr, mtpsg5 = psspy.gendat(44024)
ierr, mtpsg6 = psspy.gendat(44027)

with open('output.txt','a') as fout:
    fout.write('MVA load added to DurgapurPG %s \n' % loddurgpg)
    fout.write('MVA load added to MaithonPG %s \n' % lodmthnpg)
    fout.write('CTPS Gen7 load in MW is %s \n' % round(ctpsg7.real, 3))
    fout.write('CTPS Gen8 load in MW is %s \n' % round(ctpsg8.real, 3))
    fout.write('MTPS Gen5 load in MW is %s \n' % round(mtpsg5.real, 3))
    fout.write('MTPS Gen6 load in MW is %s \n' % round(mtpsg6.real, 3))
    fout.write('\n\n')

ierr = psspy.bus_data_2(45201, intgar1=1)
ierr = psspy.bus_data_2(45205, intgar1=3)


psspy.fnsl()
psspy.area_2(0,1,1)



ierr, rval = psspy.brnmsc(44204, 45205, '1', 'MVA')
ierr, cmpval1 = psspy.brnflo(44204, 45205, '1')
print 'Kalyaneswari - MaithonPG line1 loading in MW & MVar = ', cmpval1
print 'Kalyaneswari - MaithonPG line1 loading in % = ', cmpval1.real*100.0/186.0
flowarr[0].append(cmpval1.real*100.0/186.0)
ierr, cmpval2 = psspy.brnflo(44204, 45205, '2')
print 'Kalyaneswari - MaithonPG line2 loading in MW & MVar = ', cmpval2
print 'Kalyaneswari - MaithonPG line2 loading in % = ', cmpval2.real*100.0/186.0
flowarr[1].append(cmpval2.real*100.0/186.0)
ierr, cmpval3 = psspy.brnflo(44206, 45205, '1')
print 'Dhanbad - MaithonPG line1 loading in MW & MVar = ', cmpval3
print 'Dhanbad - MaithonPG line1 loading in % = ', cmpval3.real*100.0/186.0
flowarr[2].append(cmpval3.real*100.0/186.0)
ierr, cmpval4 = psspy.brnflo(44206, 45205, '2')
print 'Dhanbad - MaithonPG line2 loading in MW & MVar = ', cmpval4
print 'Dhanbad - MaithonPG line2 loading in % = ', cmpval4.real*100.0/186.0
flowarr[3].append(cmpval4.real*100.0/186.0)
ierr, cmpval5 = psspy.brnflo(44202, 44206, '1')
print 'Chandrapura -Dhanbad line1 loading in MW & MVar = ', cmpval5
print 'Chandrapura - Dhanbad line1 loading in % = ', cmpval5.real*100.0/186.0
flowarr[4].append(cmpval5.real*100.0/186.0)
ierr, cmpval6 = psspy.brnflo(44202, 44206, '2')
print 'Chandrapura - Dhanbad line2 loading in MW & MVar = ', cmpval6
print 'Chandrapura - Dhanbad line2 loading in % = ', cmpval6.real*100.0/186.0
flowarr[5].append(cmpval6.real*100.0/186.0)
ierr, cmpval7 = psspy.brnflo(44202, 44204, '3')
print 'Chandrapura - Kalyaneswari line1 loading in MW & MVar = ', cmpval7
print 'Chandrapura - Kalyaneswari line1 loading in % = ', cmpval7.real*100.0/186.0
flowarr[6].append(cmpval7.real*100.0/186.0)
ierr, cmpval8 = psspy.brnflo(44202, 44204, '4')
print 'Chandrapura - Kalyaneswari line2 loading in MW & MVar = ', cmpval8
print 'Chandrapura - Kalyaneswari line2 loading in % = ', cmpval8.real*100.0/186.0
flowarr[7].append(cmpval8.real*100.0/186.0)
ierr, cmpval9 = psspy.brnflo(44207, 44208, '1')
print 'Mejia - Burnpur line1 loading in MW & MVar = ', cmpval9
print 'Mejia - Burnpur line1 loading in % = ', cmpval9.real*100.0/186.0
flowarr[8].append(cmpval9.real*100.0/186.0)
ierr, cmpval11 = psspy.brnflo(44204, 44208, '1')
print 'Kalyaneswari - Burnpur line1 loading in MW & MVar = ', cmpval11
print 'Kalyaneswari - Burnpur line1 loading in % = ', cmpval11.real*100.0/186.0
flowarr[9].append(cmpval11.real*100.0/186.0)
ierr, cmpval13 = psspy.brnflo(44204, 44207, '1')
print 'Kalyaneswari - Mejia line1 loading in MW & MVar = ', cmpval13
print 'Kalyaneswari - Mejia line1 loading in % = ', cmpval13.real*100.0/186.0
flowarr[10].append(cmpval13.real*100.0/186.0)
ierr, cmpval14 = psspy.brnflo(44204, 44207, '2')
print 'Kalyaneswari - Mejia line2 loading in MW & MVar = ', cmpval14
print 'Kalyaneswari - Mejia line2 loading in % = ', cmpval14.real*100.0/186.0
flowarr[11].append(cmpval14.real*100.0/186.0)
ierr, cmpval15 = psspy.brnflo(44204, 44207, '3')
print 'Kalyaneswari - Mejia line3 loading in MW & MVar = ', cmpval15
print 'Kalyaneswari - Mejia line3 loading in % = ', cmpval15.real*100.0/186.0
flowarr[12].append(cmpval15.real*100.0/186.0)
print '\n'

ierr, cmpval16 = psspy.brnflo(44218, 45201, '1')
print 'ParuliaDVC - ParuliaPG line1 loading in MW & MVar = ', cmpval16
print 'ParuliaDVC - ParuliaPG line1 loading in % = ', cmpval16.real*100.0/186.0
flowarr[13].append(cmpval16.real*100.0/186.0)
ierr, cmpval17 = psspy.brnflo(44218, 45201, '2')

print 'ParuliaDVC - ParuliaPG line2 loading in % = ', cmpval17.real*100.0/186.0
flowarr[14].append(cmpval17.real*100.0/186.0)
ierr, cmpval18 = psspy.brnflo(44205, 44218, '1')
print 'Durgapur - Parulia line1 loading in MW & MVar = ', cmpval18
print 'Durgapur - Parulia line1 loading in % = ', cmpval18.real*100.0/186.0
flowarr[15].append(cmpval18.real*100.0/186.0)
ierr, cmpval19 = psspy.brnflo(44205, 44218, '2')
print 'Durgapur - Parulia line2 loading in MW & MVar = ', cmpval19
print 'Durgapur - Parulia line2 loading in % = ', cmpval19.real*100.0/186.0
flowarr[16].append(cmpval19.real*100.0/186.0)
ierr, cmpval20 = psspy.brnflo(44203, 44218, '1')
print 'DTPS - Parulia line1 loading in MW & MVar = ', cmpval20
print 'DTPS - Parulia line1 loading in % = ', cmpval20.real*100.0/186.0
flowarr[17].append(cmpval20.real*100.0/186.0)
ierr, cmpval21 = psspy.brnflo(44203, 44218, '2')
print 'DTPS - Parulia line2 loading in MW & MVar = ', cmpval21
print 'DTPS - Parulia line2 loading in % = ', cmpval21.real*100.0/186.0
flowarr[18].append(cmpval21.real*100.0/186.0)
ierr, cmpval22 = psspy.brnflo(44207, 44205, '1')
print 'Mejia - Durgapur line1 loading in MW & MVar = ', cmpval22
print 'Mejia - Durgapur line1 loading in % = ', cmpval22.real*100.0/186.0
flowarr[19].append(cmpval22.real*100.0/186.0)
ierr, cmpval23 = psspy.brnflo(44207, 44205, '2')
print 'Mejia - Durgapur line2 loading in MW & MVar = ', cmpval23
print 'Mejia - Durgapur line2 loading in % = ', cmpval23.real*100.0/186.0
flowarr[20].append(cmpval23.real*100.0/186.0)
ierr, cmpval24 = psspy.brnflo(44207, 44203, '1')
print 'Mejia - DTPS line1 loading in MW & MVar = ', cmpval24
print 'Mejia - DTPS line1 loading in % = ', cmpval24.real*100.0/186.0
flowarr[21].append(cmpval24.real*100.0/186.0)
ierr, cmpval25 = psspy.brnflo(44207, 44203, '2')
print 'Mejia - DTPS line2 loading in MW & MVar = ', cmpval25
print 'Mejia - DTPS line2 loading in % = ', cmpval25.real*100.0/186.0
flowarr[22].append(cmpval25.real*100.0/186.0)
print '\n'
print flowarr
##print '\n'
##print sum(map(operator.sub, map(abs, cmpvalarr3), map(abs, cmpvalarr2)))

with open('output.txt','a') as fout:
    fout.write(add_data())
    fout.write('\n\n')

psspy.report_output(islct=2, filarg="./output.txt", options=[2])
psspy.asys(sid=1,num=1,areas=4)
psspy.ties(1,0)
#psspy.ties()
psspy.report_output(islct=2, options=[0])
with open('output.txt','a') as fout:
    fout.write('\n\n')

    
##psspy.report_output(islct=2, filarg="./output.txt", options=[2])
##psspy.pout()
##psspy.report_output(islct=2, options=[0])
##with open('output.txt','a') as fout:
##    fout.write('\n\n')


with open('output.txt','a') as fout:
    fout.write(trans_chrgs_calc())
    fout.write('\n\n')
