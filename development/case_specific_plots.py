import os,sys
#PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
PSSE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION 
import psspy
import redirect
redirect.psse2py()

from psse_utils import run_psse
from plot_pdf import pdf_network
from functools import wraps
def modify_networkelements(f):
    def wrapper(*args, **kwargs):
        case_title = f()
        args = run_psse()
        #psspy.pout(sid=1, all=0)
        pdf_network(case_title,*args)
    return wraps(f)(wrapper)


@modify_networkelements
def case_existing_scenario():
    return "Existing scenario with one gen at KTPS, DSTPS"

#@modify_networkelements
def case_dtps_decom_1():
    psspy.bus_data_2(44231, intgar1=1) #DSTPS2
    psspy.machine_data_2(44009, intgar1=0) #DTPS gen3
    # LILO of DTPS - Parulia at DSTPS
    d, a3z = 10, (0.014313, 0.086133, 0.140196)# DTPS - DSTPS distance in km
    lc = [0.01*d*i for i in a3z]
    psspy.branch_data(44203, 44231, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #DTPS - DSTPS line
    psspy.branch_data(44203, 44231, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    psspy.branch_data(44218, 44231, "1", intgar1=1) #DSTPS - PARU line
    psspy.branch_data(44218, 44231, "2", intgar1=1)
    psspy.branch_data(44203, 44218, "1", intgar1=0) #DTPS - PARU line
    psspy.branch_data(44203, 44218, "2", intgar1=0)
    return "Case DTPS 3 decommisioning stage_1"

#@modify_networkelements
def case_dtps_decom_2():
    case_dtps_decom_1()
    # Burdwan voltage upgrade
    psspy.bus_data_2(44234, intgar1=1) #BDWN2
    d, a3z = 64, (0.014313, 0.086133, 0.140196)# PARU - BDWN distance in km
    lc = [0.01*d*i for i in a3z]
    psspy.branch_data(44218, 44234, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #PARU - BDWN line
    psspy.branch_data(44218, 44234, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    return "Case DTPS 3 decommisioning stage_2"

#@modify_networkelements
def case_dtps_decom_3(): 
    case_dtps_decom_2()
    # Kalipahari voltage upgrade case
    psspy.bus_data_2(44240, intgar1=1) #KALI2
    psspy.two_winding_data(44118, 44240, "1", intgar1=1) #KALI2 - KALI1 trf
    psspy.two_winding_data(44118, 44240, "2", intgar1=1) #KALI2 - KALI1 trf
    psspy.branch_data(44207, 44208, "1", intgar1=1) #MTPS - BURN2 line
    psspy.branch_data(44207, 44208, "2", intgar1=0)
    psspy.branch_data(44204, 44208, "1", intgar1=1) #KLYN - BURN2 line
    psspy.branch_data(44204, 44208, "2", intgar1=0)
    d, a3z = 51.23, (0.014313, 0.086133, 0.140196) # MTPS - KALI2 distance in km
    lc = [0.01*d*i for i in a3z]
    psspy.branch_data(44207, 44240, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #MTPS - KALI2 line
    d = 28 # KALI2 - KLYN distance in km
    lc = [0.01*d*i for i in a3z]
    psspy.branch_data(44240, 44204, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #KALI2 - KLYN line
    return "Case DTPS 3 decommisioning stage_3"

    
#@modify_networkelements
def case_ctps_decom_1():
    psspy.bus_data_2(44231, intgar1=0) #DSTPS2
    psspy.machine_data_2(44009, intgar1=0) #DTPS gen3
    psspy.load_data_3(44106, realar1=159.) #CTPS1
    psspy.load_data_3(44202, realar1=200.) #CTPS2
    # LILO of CTPS - Gola line at Biada
    psspy.branch_data(44106, 44115, "1", intgar1=0) #ctps - gola line
    psspy.branch_data(44106, 44115, "2", intgar1=0)
    sae3p = (0.079018, 0.246065, 0.050086)
    d = 16 # ctps biada line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44106, 44138, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44106, 44138, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    d = 60 # biada gola line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44115, 44138, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44115, 44138, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])    
    return "Case CTPS 1,2,3 decommissioning stage_1"


#@modify_networkelements
def case_ctps_decom_2():
    case_ctps_decom_1()
    # Patherdih load shifted to Dhanbad
    psspy.branch_data(44111, 44123, "1", intgar1=1) #maithon hydel - patherdih line
    psspy.branch_data(44111, 44123, "2", intgar1=1)
    psspy.branch_data(44123, 44130, "1", intgar1=1) #patherdih - dhanbad line
    psspy.branch_data(44123, 44130, "2", intgar1=1)
    return "Case CTPS 1,2,3 decommissioning stage_2"


#@modify_networkelements
def case_ctps_decom_3():
    case_ctps_decom_2()
    psspy.branch_data(44106, 44138, "1", intgar1=0) #ctps - biada line
    psspy.branch_data(44106, 44138, "2", intgar1=0)
    psspy.branch_data(44106, 44133, "1", intgar1=0) #ctps - purulia line
    psspy.branch_data(44106, 44133, "2", intgar1=0)
    # BokaroSt (BSL) GIS substation infrastructure 
    psspy.bus_data_2(44230, intgar1=1, intgar3=44, realar1=220.) #CHAS2
    psspy.bus_data_2(44140, intgar1=1, intgar3=44, realar1=132.) #CHAS1
    cea3z = (0.014313, 0.086133, 0.140196)
    d = 18 # CTPS2 - CHAS2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44202, 44230, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #CTPS2 - CHAS2 line
    psspy.branch_data(44202, 44230, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    psspy.two_winding_data_3(44140, 44230, "1", #CHAS_ATR1 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44230,     #WN1BUS
                         intgar10=44140,    #CONT1
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
    psspy.two_winding_data_3(44140, 44230, "2", #CHAS_ATR2 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44230,     #WN1BUS
                         intgar10=44140,    #CONT1
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
    psspy.branch_data(44106, 44140, "1", intgar1=0) #CTPS1 - CHAS1
    psspy.branch_data(44106, 44140, "2", intgar1=0)
    # CTPS - Purulia line terminated at Chas/BSL
    sae3p = (0.079018, 0.246065, 0.050086)
    d = 50 # purulia chas/bsl line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44133, 44140, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44133, 44140, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    # Chas/BSL - CTPS segment connected to CTPS - Biada outside CTPS
    d = 26 # chas/bsl biada line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44140, 44138, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44140, 44138, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    # Redistribution of loads
    psspy.load_data_3(44106, realar1=159.) #CTPS1
    psspy.load_data_3(44202, realar1=0.) #CTPS2
    psspy.load_data_3(44230, realar1=200.) #CHAS2
    psspy.machine_data_2(44017, intgar1=0) #CTPS gen3
    return "Case CTPS 1,2,3 decommissioning stage_3"


#@modify_networkelements
def case_ctps_decom_4():
    case_dtps_decom_3()
    case_ctps_decom_3()
    #psspy.machine_data_2(44015, realar1=80.) #CTPS gen1
    psspy.machine_data_2(44016, intgar1=0) #CTPS gen2
    # LILO of MTPS Gola2 at Chas/BSL
    psspy.bus_data_2(44219, intgar1=1) #GOLA2
    d, cea3z = 160, (0.014313, 0.086133, 0.140196) # MTPS - GOLA2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44207, 44219, "1", intgar1=0) #MTPS - GOLA2 line
    psspy.branch_data(44207, 44219, "2", intgar1=0)
    d, cea3z = 100, (0.014313, 0.086133, 0.140196) # MTPS - CHAS2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44207, 44230, "1", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2]) #MTPS - CHAS2 line
    psspy.branch_data(44207, 44230, "2", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2])
    d = 70 # GOLA2 - CHAS2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44219, 44230, "1", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2]) #GOLA2 - CHAS2 line
    psspy.branch_data(44219, 44230, "2", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2])
    d = 36 # GOLA2 - RMGH2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44219, 44209, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #GOLA2 - RMGH2 line
    psspy.branch_data(44219, 44209, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    return "Case CTPS 1,2,3 decommissioning stage_4"
    
#@modify_networkelements
def case_ctps_decom_5():
    case_ctps_decom_4()
    run_psse()
    psspy.load_data_3(44106, realar1=0.) #CTPS1
    psspy.load_data_3(44202, realar1=159.) #CTPS2
    psspy.load_data_3(44140, realar1=10.) #BSL1
    psspy.two_winding_data_3(44140, 44230, "3", #CHAS_ATR3 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44230,     #WN1BUS
                         intgar10=44140,    #CONT1
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
    # Connect CTPS end of CTPS Putki line to BSL
    psspy.branch_data(44106, 44117, "1", intgar1=0)
    psspy.branch_data(44106, 44117, "2", intgar1=0)
    psspy.branch_data(44106, 44117, "3", intgar1=0)
    psspy.branch_data(44106, 44117, "4", intgar1=0)
    sae3p = (0.079018, 0.246065, 0.050086)
    d = 40 # BSL Putki line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44117, 44140, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44117, 44140, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    #psspy.seq_fixed_shunt_data(44140, "1", realar2=100.0)
    psspy.machine_data_2(44015, intgar1=0) #CTPS gen1
    # Connect CTPS - DTPS line to BSL at CTPS end
    psspy.branch_data(44106, 44109, "1", intgar1=0)
    psspy.branch_data(44106, 44127, "1", intgar1=0)
    d = 16+135 # BSL Putki line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44109, 44140, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    d = 16+70 # BSL Putki line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44127, 44140, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])    
    # Enable Bkro-A gen and conect BTPS to BSL to obtain convergence
    psspy.machine_data_2(44010, intgar1=1) #BKROA gen1
##    psspy.branch_data(44200, 44202, "1", intgar1=0)
##    psspy.branch_data(44200, 44202, "2", intgar1=0)
##    d, cea3z = 20, (0.014313, 0.086133, 0.140196) #BTPS - BSL2 distance in km
##    lc = [0.01*d*i for i in cea3z]
##    psspy.branch_data(44200, 44230, "1", intgar1=1, realar1=lc[0],
##                             realar2=lc[1], realar3=lc[2]) #BTPS - BSL2 line
##    psspy.branch_data(44200, 44230, "2", intgar1=1, realar1=lc[0],
##                             realar2=lc[1], realar3=lc[2])
##    d, cea3z = 48, (0.014313, 0.086133, 0.140196) #CTPS - BSL2 distance in km
##    psspy.branch_data(44202, 44230, "1", intgar1=1, realar1=lc[0],
##                             realar2=lc[1], realar3=lc[2]) #CTPS - BSL2 line
##    psspy.branch_data(44202, 44230, "2", intgar1=1, realar1=lc[0],
##                             realar2=lc[1], realar3=lc[2])
    return "Case CTPS 1,2,3 decommissioning stage_5"
    
@modify_networkelements
def case_alt_ctps_decom_1():
    # BokaroSt (BSL) bus 
    psspy.bus_data_2(44230, intgar1=1, intgar3=44, realar1=220.) #CHAS2
    cea3z = (0.014313, 0.086133, 0.140196)
    d = 18 # CTPS2 - CHAS2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44202, 44230, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #CTPS2 - CHAS2 line
    psspy.branch_data(44202, 44230, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    # Redistribution of loads and decom. of units
    psspy.load_data_3(44106, realar1=159.) #CTPS1
    psspy.load_data_3(44202, realar1=0.) #CTPS2
    psspy.load_data_3(44230, realar1=200.) #CHAS2
    psspy.machine_data_2(44015, intgar1=0) #CTPS gen1
    psspy.machine_data_2(44016, intgar1=0) #CTPS gen2
    #psspy.branch_data(44200, 44202, "1", intgar1=0)
    #psspy.branch_data(44200, 44202, "2", intgar1=0)
    psspy.machine_data_2(44010, intgar1=1, realar1=400.) #BKROA gen1
    psspy.machine_data_2(44017, intgar1=0) #CTPS gen3
    psspy.machine_data_2(44004, intgar1=0) #BKROA gen1
    return "Alt. Case CTPS 1,2,3 decommissioning stage_1"

#@modify_networkelements
def case_alt_ctps_decom_2():
    case_alt_ctps_decom_1()
    # LILO of CTPS - Gola line at Biada
    psspy.branch_data(44106, 44115, "1", intgar1=0) #ctps - gola line
    psspy.branch_data(44106, 44115, "2", intgar1=0)
    sae3p = (0.079018, 0.246065, 0.050086)
    d = 16 # ctps biada line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44106, 44138, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44106, 44138, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    d = 60 # biada gola line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44115, 44138, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44115, 44138, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    # Redistribution of loads
    psspy.load_data_3(44106, realar1=159.) #CTPS1
    psspy.load_data_3(44202, realar1=0.) #CTPS2
    psspy.load_data_3(44230, realar1=200.) #CHAS2
    psspy.machine_data_2(44016, intgar1=0) #CTPS gen2
    return "Alt. Case CTPS 1,2,3 decommissioning stage_2"

#@modify_networkelements
def case_alt_ctps_decom_3():
    case_alt_ctps_decom_2()
    # BokaroSt (BSL) GIS substation infrastructure 
    psspy.bus_data_2(44230, intgar1=1, intgar3=44, realar1=220.) #CHAS2
    psspy.bus_data_2(44140, intgar1=1, intgar3=44, realar1=132.) #CHAS1
    psspy.two_winding_data_3(44140, 44230, "1", #CHAS_ATR1 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44230,     #WN1BUS
                         intgar10=44140,    #CONT1
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
    psspy.two_winding_data_3(44140, 44230, "2", #CHAS_ATR2 (BBL)
                         intgar1=1,         #STAT
                         intgar7=17,        #NTP1
                         intgar9=44230,     #WN1BUS
                         intgar10=44140,    #CONT1
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
    psspy.branch_data(44106, 44140, "1", intgar1=0) #CTPS1 - CHAS1
    psspy.branch_data(44106, 44140, "2", intgar1=0)
    psspy.branch_data(44106, 44133, "1", intgar1=0) #CTPS1 - PURULIA
    psspy.branch_data(44106, 44133, "2", intgar1=0)
    psspy.branch_data(44106, 44138, "1", intgar1=0) #CTPS1 - BIADA
    psspy.branch_data(44106, 44138, "2", intgar1=0)
    # CTPS - Purulia line terminated at Chas/BSL
    sae3p = (0.079018, 0.246065, 0.050086)
    d = 45 # purulia chas/bsl line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44133, 44140, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44133, 44140, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    # Chas/BSL - CTPS segment connected to CTPS - Biada outside CTPS
    d = 31 # chas/bsl biada line distance in km
    lc = [0.01*d*i for i in sae3p]
    psspy.branch_data(44140, 44138, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
    psspy.branch_data(44140, 44138, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    # Redistribution of loads
    psspy.load_data_3(44106, realar1=159.) #CTPS1
    psspy.load_data_3(44202, realar1=0.) #CTPS2
    psspy.load_data_3(44230, realar1=200.) #CHAS2
    psspy.machine_data_2(44010, intgar1=1) #BKROA gen1
    psspy.machine_data_2(44017, intgar1=0) #CTPS gen3
    return "Alt. Case CTPS 1,2,3 decommissioning stage_3"

#@modify_networkelements
def case_alt_ctps_decom_4():
    case_alt_ctps_decom_3()
    # LILO of MTPS Gola2 at Chas/BSL
    psspy.bus_data_2(44219, intgar1=1) #GOLA2
    d, cea3z = 160, (0.014313, 0.086133, 0.140196) # MTPS - GOLA2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44207, 44219, "1", intgar1=0) #MTPS - GOLA2 line
    psspy.branch_data(44207, 44219, "2", intgar1=0)
    d, cea3z = 100, (0.014313, 0.086133, 0.140196) # MTPS - CHAS2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44207, 44230, "1", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2]) #MTPS - CHAS2 line
    psspy.branch_data(44207, 44230, "2", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2])
    d = 70 # GOLA2 - CHAS2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44219, 44230, "1", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2]) #GOLA2 - CHAS2 line
    psspy.branch_data(44219, 44230, "2", intgar1=1, realar1=lc[0],
                             realar2=lc[1], realar3=lc[2])
    d = 36 # GOLA2 - RMGH2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44219, 44209, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) #GOLA2 - RMGH2 line
    psspy.branch_data(44219, 44209, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    return "Alt. Case CTPS 1,2,3 decommissioning stage_4"

#@modify_networkelements
def case_btps_decom_1():
    case_ctps_decom_5()
    psspy.machine_data_2(44005, intgar1=0) #BKROA gen2
    #psspy.machine_data_2(44006, intgar1=0) #BKROA gen3
    return "Case BTPS 1,2,3 decommisioning stage_1"

@modify_networkelements
def case_btps_decom_2():
    case_btps_decom_1()
    psspy.bus_data_2(44410, intgar1=1, intgar3=44, realar1=400.) #RAGHU4
    psspy.bus_data_2(44241, intgar1=1, intgar3=44, realar1=220.) #RAGHU2
    ierr, realaro = psspy.two_winding_data(44410, 44242, "1", intgar1=1,
                                           intgar7=17, intgar10=44242,
                                           intgar12=1, intgar13=1,
                                           realar1=.00097, realar2=.03497,
                                           realar3=315., realar4=1.0,
                                           realar5=132., realar6=15., realar8=132., realar9=150.,
                                           realar20=70., realar21=0.) #JMU1 - JMUPST1 trf

    d, cea3z = 160, (0.014313, 0.086133, 0.140196) # MTPS - GOLA2 distance in km
    lc = [0.01*d*i for i in cea3z]
    psspy.branch_data(44207, 44219, "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    psspy.branch_data(44207, 44219, "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
    psspy.machine_data_2(44004, intgar1=0) #BKROA gen1
    return "Case BTPS 1,2,3 decommisioning stage_2"
    

if __name__ == '__main__':
    case_existing_scenario()
    #case_dtps_decom_1()
    #case_dtps_decom_2()
    #case_dtps_decom_3()
    #case_ctps_decom_1()
    #case_ctps_decom_2()
    #case_ctps_decom_3()
    #case_ctps_decom_4()
    #case_ctps_decom_5()
    #case_alt_ctps_decom_1()
    #case_alt_ctps_decom_2()
    #case_alt_ctps_decom_3()
    #case_alt_ctps_decom_4()
    #case_btps_decom_1()
    #case_btps_decom_2()

