from settings import *

SAVFILE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\EXAMPLE\\"
CASE = r"Basic Network_Q3_2015-16_Rev0_ER Updates.sav" 
psspy.case(SAVFILE_LOCATION + CASE)

AREA, DVC_ZONE, OWNER = 2003, 2031, 2301


busMap = {
    'MPL4'          : 224001,
    'KTPS4'         : 244002,
    'RTPS4'         : 234000,
    'DSTPS4'        : 234001,
    'BTPSA4'        : 244001,
    'MTPSB4'        : 234002,
    'JSRBPRS4'      : 244000,
    'RANCHIPG4'     : 224004,
    'MAITHONPG4'    : 244003,
    'PARULIAPG4'    : 264009,
    'JAMSHEDPURPG4' : 244004,
    'CHAIBASA4'     : 244005,
    'BARIPADAPG4'   : 254012,
    'BIHARSHRIFPG4' : 214000,
    'GAYAPG4'       : 214005,

    'BTPSBG1'       : 44004,
    'BTPSBG2'       : 44005,
    'BTPSBG3'       : 44006,
    'DTPSG4'        : 44008,
    'DTPSG3'        : 44009,
    'BTPSAG1'       : 44010,
    'MTPSBG1'       : 44013,
    'MTPSBG2'       : 44014,
    'CTPSG1'        : 44015,
    'CTPSG2'        : 44016,
    'CTPSG3'        : 44017,
    'CTPSG7'        : 44018,
    'CTPSG8'        : 44019,
    'MTPSG1'        : 44020,
    'MTPSG2'        : 44021,
    'MTPSG3'        : 44022,
    'MTPSG4'        : 44023,
    'MTPSG5'        : 44024,
    'MTPSG6'        : 44025,
    'KTPSG1'        : 44026,
    'KTPSG2'        : 44027,
    'RTPSG1'        : 44030,
    'RTPSG2'        : 44031,
    'DSTPSG1'       : 44032,
    'DSTPSG2'       : 44033,
    'RTPSG3'        : 44034,
    'RTPSG4'        : 44035,
    'KTPSG3'        : 44036,
    'KTPSG4'        : 44037,

    'BIDHANNG2'     : 262005,
    'JODAIS2'       : 252029,
    'BTPSB2'        : 242000,
    'CTPS2'         : 242001,
    'DTPS2'         : 232000,
    'KALYANESWARI2' : 242003,
    'MUCHIPARA2'    : 232005,
    'DHANBAD2'      : 242004,
    'MTPS2'         : 232001,
    'BURNPUR2'      : 232004,
    'RAMGARH2'      : 242007,
    'JAMSHEDPUR2'   : 242002,
    # 'RANIGUNJ2'     : 44214,
    'BARJORA2'      : 232003,
    'PARULIA2'      : 232002,
    'GOLA2'         : 242008,
    'GIRIDIH2'      : 242005,
    'KODERMA2'      : 242006,
    # 'RTPS2'         : 44227,
    # 'MOSABANI2'     : 44228,
    # 'CHAS2'         : 44230,
    # 'DSTPS2'        : 44231,
    # 'KHARAGPUR2'    : 44232,
    # 'PANAGARH2'     : 44233,
    # 'BURDWAN2'      : 44234,
    # 'NKPURA2'       : 44235,
    # 'PATRATU2'      : 44236,
    # 'MEJIAB2'       : 44239,
    # 'KALIPAHARI2'   : 44240,
    # 'JAMURIA2'      : 44241,
    'PARULIAPG2'    : 262028,
    'MAITHONPG2'    : 242009,
    'RANCHIPG2'     : 222007,

    'BTPSB1'        : 241001,
    'MOSABANI1'     : 241011,
    'BURDWAN1'      : 231006,
    'BELMURI1'      : 231005,
    'HOWRAH1'       : 231004,
    'KHARAGPUR1'    : 231002,
    'CTPS1'         : 241002,
    'KOLAGHAT1'     : 231003,
    'JAMSHEDPUR1'   : 241005,
    'DTPS1'         : 231000,
    'BARHI1'        : 241000,
    'MAITHONHYDL1'  : 241006,
    'MAITHONGT1'    : 241008,
    'PANCHETHYDL1'  : 231007,
    'HAZARIBAGH1'   : 241019,
    'GOLA1'         : 241003,
    'CHANDIL1'      : 241004,
    'PUTKI1'        : 241015,
    'KALIPAHARI1'   : 231008,
    'ASP1'          : 231009,
    'RAMGARH1'      : 241013,
    'KALYANESWARI1' : 241009,
    'KUMARDUBI1'    : 241010,
    'PATHERDIH1'    : 241007,
    'NIMIAGHAT1'    : 241021,
    'GIRIDIHO1'     : 241023,
    'GIRIDIHN1'     : 241029,
    'SINDRI1'       : 241022,
    'RAMKANALI1'    : 241012,
    'PATRATU1'      : 241014,
    'NKPURA1'       : 241020,
    'DHANBAD1'      : 241030,
    'PURULIA1'      : 231001,
    'JAMURIA1'      : 231011,
    'KONAR1'        : 241017,
    'BARJORA1'      : 231010,
    'KODERMAO1'     : 241032,
    'KODERMAN1'     : 241018,
    'BIADA1'        : 241033,  
    # 'MUGMA1'        : 44139,
    # 'CHAS1'         : 44140,
    # 'RANIGUNJ1'     : 44141,     

    'MUCHIPARA3'    : 233000,
}

###------------------------
psspy.bus_data_2(busMap['JAMURIA1'], intgar1=1, intgar2=AREA, intgar3=DVC_ZONE, intgar4=OWNER, realar1=132.,
     name="JAMUR1") 
psspy.bus_data_2(busMap['KODERMAN1'], intgar1=1, intgar2=AREA, intgar3=DVC_ZONE, intgar4=OWNER, realar1=132.,
     name="KODRN1") 
psspy.bus_data_2(busMap['BIADA1'], intgar1=1, intgar2=AREA, intgar3=DVC_ZONE, intgar4=OWNER, realar1=132.,
     name="BIADA1") 
# psspy.bus_data_2(busMap['KTPSG3'], intgar1=4) #KODRG3
# psspy.bus_data_2(busMap['KTPSG4'], intgar1=4) #KODRG4
# psspy.bus_data_2(busMap['MUGMA1'], intgar1=4) #MUGMA1
# psspy.bus_data_2(busMap['CHAS1'], intgar1=4) #CHAS1
# psspy.bus_data_2(busMap['RANIGUNJ1'], intgar1=4) #RNIGNJ1
# psspy.bus_data_2(busMap['RANIGUNJ2'], intgar1=4) #RNIGNJ2
# psspy.bus_data_2(busMap['GOLA2'], intgar1=4) #GOLA2
# psspy.bus_data_2(busMap['RTPS2'], intgar1=4) #RTPS2
# psspy.bus_data_2(busMap['MOSABANI2'], intgar1=4) #MOSB2
# psspy.bus_data_2(busMap['CHAS2'], intgar1=4) #CHAS2
# psspy.bus_data_2(busMap['DSTPS2'], intgar1=4) #DSTPS2
# psspy.bus_data_2(busMap['KHARAGPUR2'], intgar1=4) #KGP2
# psspy.bus_data_2(busMap['PANAGARH2'], intgar1=4) #PANAG2
# psspy.bus_data_2(busMap['BURDWAN2'], intgar1=4) #BDWN2
# psspy.bus_data_2(busMap['NKPURA2'], intgar1=4) #NKPURA2
# psspy.bus_data_2(busMap['PATRATU2'], intgar1=4) #PATR2
# psspy.bus_data_2(busMap['MEJIAB2'], intgar1=4) #MEJIAB2
# psspy.bus_data_2(busMap['KALIPAHARI2'], intgar1=4) #KALI2
# psspy.bus_data_2(busMap['JAMURIA2'], intgar1=4) #JAMURIA2
#psspy.bus_data_2(busMap['MUCHIPARA3'], intgar1=1, intgar2=AREA, intgar3=DVC_ZONE, intgar4=OWNER, realar1=33., 
#     name='MUCHI3') 
# psspy.bus_data_2(busMap['MOSABANI4'], intgar1=4) #MOSB4


#LOAD AS ON 31.8.2015
psspy.load_data_3(busMap['BTPSB1'], realar1=68.) #BOKARO
psspy.load_data_3(busMap['MOSABANI1'], realar1=96.) #MOSABANI
psspy.load_data_3(busMap['BURDWAN1'], realar1=124.) #BURDWAN
psspy.load_data_3(busMap['BELMURI1'], realar1=43.) #BELMURI
psspy.load_data_3(busMap['HOWRAH1'], realar1=15.) #HOWRAH
psspy.load_data_3(busMap['KHARAGPUR1'], realar1=17.) #KHARAGPUR
psspy.load_data_3(busMap['CTPS1'], realar1=359.) #CHANDRAPURA
psspy.load_data_3(busMap['KOLAGHAT1'], realar1=14.5) #KOLAGHAT
psspy.load_data_3(busMap['JAMSHEDPUR1'], realar1=140.) #JAMSHEDPUR
psspy.load_data_3(busMap['DTPS1'], realar1=42.2) #DTPS
psspy.load_data_3(busMap['BARHI1'], realar1=48.) #BARHI
psspy.load_data_3(busMap['MAITHONHYDL1'], realar1=56.6+18.) #MAITHON HYDEL
psspy.load_data_3(busMap['PANCHETHYDL1'], realar1=17.6) #PANCHET HYDEL
psspy.load_data_3(busMap['KODERMAO1'], realar1=93.) #KODERMAOLD
psspy.load_data_3(busMap['HAZARIBAGH1'], realar1=80.) #HAZARIBAGH
psspy.load_data_3(busMap['GOLA1'], realar1=48.6) #GOLA
psspy.load_data_3(busMap['CHANDIL1'], realar1=60.) #CHANDIL
psspy.load_data_3(busMap['PUTKI1'], realar1=185.7) #PUTKI
psspy.load_data_3(busMap['KALIPAHARI1'], realar1=141.3) #KALIPAHARI
psspy.load_data_3(busMap['ASP1'], realar1=57.3) #ASP
psspy.load_data_3(busMap['RAMGARH1'], realar1=203.75-53.) #RAMGARH
psspy.load_data_3(busMap['KALYANESWARI1'], realar1=143.25) #KALYANESWARI
psspy.load_data_3(busMap['KUMARDUBI1'], realar1=105.23) #KUMARDUBI
psspy.load_data_3(busMap['PATHERDIH1'], realar1=208.65-40.0) #PATHERDIH (minus GOVINDPUR)
psspy.load_data_3(busMap['NIMIAGHAT1'], realar1=61.5) #NIMIAGHAT
psspy.load_data_3(busMap['GIRIDIHO1'], realar1=146.) #GIRIDIH
psspy.load_data_3(busMap['SINDRI1'], realar1=27.5) #SINDRI
psspy.load_data_3(busMap['RAMKANALI1'], realar1=34.) #RAMKANALI
psspy.load_data_3(busMap['PATRATU1'], realar1=55.2) #PATRATU
psspy.load_data_3(busMap['NKPURA1'], realar1=45.) #NORTH KARANPURA
psspy.load_data_3(busMap['PURULIA1'], realar1=16.75) #PURULIA
psspy.load_data_3(busMap['JAMURIA1'], realar1=73.) #JAMURIA
psspy.load_data_3(busMap['KONAR1'], realar1=27.) #KONAR
psspy.load_data_3(busMap['BARJORA1'], realar1=26.) #BORJORA1
psspy.load_data_3(busMap['KODERMAN1'], realar1=0.0) #KODRMANEW
psspy.load_data_3(busMap['BIADA1'], realar1=26.6) #BIADA
#psspy.load_data_3(busMap['MUGMA1'], realar1=20.) #MUGMA
psspy.load_data_3(busMap['CTPS2'], realar1=0.0) #CTPS2
psspy.load_data_3(busMap['MUCHIPARA2'], realar1=177.5) #DURGAPUR
psspy.load_data_3(busMap['DHANBAD2'], realar1=69.+40.) #DHANBAD
psspy.load_data_3(busMap['MTPS2'], realar1=46.9) #MTPS
psspy.load_data_3(busMap['BURNPUR2'], realar1=180.) #BURNPUR
psspy.load_data_3(busMap['RAMGARH2'], realar1=53.) #RAMGARH2
psspy.load_data_3(busMap['BARJORA2'], realar1=203.-26.) #BORJORA
psspy.load_data_3(busMap['PARULIA2'], realar1=179.1) #PARULIA
psspy.load_data_3(busMap['GOLA2'], realar1=0.) #GOLA2
psspy.load_data_3(busMap['GIRIDIH2'], realar1=20.) #GIRIDIH2
psspy.load_data_3(busMap['KODERMA2'], realar1=0.) #KODERMA2
#psspy.load_data_3(busMap['RTPS2'], realar1=0.) #RTPS2
#psspy.load_data_3(busMap['CHAS2'], realar1=0.) #CHAS2
#psspy.load_data_3(busMap['PANAGARH2'], realar1=0.) #PANAGARH
#psspy.load_data_3(busMap['NKPURA2'], realar1=0.) #NKPURA2
#psspy.load_data_3(busMap['PATRATU2'], realar1=0.) #PATRATU
#psspy.load_data_3(busMap['MEJIAB2'], realar1=0.) #MEJIAB

#BRANCH DATA -----------------------------------------------
a3p = (0.079018, 0.246065, 0.050086)
psspy.branch_data(busMap['DTPS1'], busMap['RAMKANALI1'], "1", intgar1=0)
d = 25  # distance in km
lc = [0.01*d*i for i in a3p]
psspy.branch_data(busMap['DTPS1'], busMap['JAMURIA1'], "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
d = 45  # distance in km
lc = [0.01*d*i for i in a3p]
psspy.branch_data(busMap['JAMURIA1'], busMap['RAMKANALI1'], "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])

psspy.branch_data(busMap['BARHI1'], busMap['KODERMAO1'], "1", intgar1=0)
psspy.branch_data(busMap['BARHI1'], busMap['KODERMAO1'], "2", intgar1=0)
d = 11 # distance in km
lc = [0.01*d*i for i in a3p]
psspy.branch_data(busMap['BARHI1'], busMap['KODERMAN1'], "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
psspy.branch_data(busMap['BARHI1'], busMap['KODERMAN1'], "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])
d = 9 # distance in km
lc = [0.01*d*i for i in a3p]
psspy.branch_data(busMap['KODERMAN1'], busMap['KODERMAO1'], "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
psspy.branch_data(busMap['KODERMAN1'], busMap['KODERMAO1'], "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])

d = 28 # CTPS - BIADA distance in km
lc = [0.01*d*i for i in a3p]
psspy.branch_data(busMap['CTPS1'], busMap['BIADA1'], "1", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2]) 
psspy.branch_data(busMap['CTPS1'], busMap['BIADA1'], "2", intgar1=1, realar1=lc[0],
                         realar2=lc[1], realar3=lc[2])

psspy.branch_data(busMap['BTPSB1'], busMap['CTPS1'], "1", intgar1=0)
psspy.branch_data(busMap['BTPSB1'], busMap['CTPS1'], "2", intgar1=0)

# psspy.movebrn(frmbus=busMap['GIRIDIH2'], tobus=busMap['GIRIDIHN1'], ckt='2', newtobus=busMap['GIRIDIHO1'], 
#     newckt='1')
d = 1 # distance in km
lc = [0.01*d*i for i in a3p]
psspy.branch_data(busMap['GIRIDIHO1'], busMap['GIRIDIHN1'], "1", intgar1=1, realar1=lc[0], realar2=lc[1], 
    realar3=lc[2]) 
psspy.branch_data(busMap['GIRIDIHO1'], busMap['GIRIDIHN1'], "2", intgar1=1, realar1=lc[0], realar2=lc[1], 
    realar3=lc[2]) 

d, cea3z = 58, (0.014313, 0.086133, 0.140196) 
lc = [0.01*d*i for i in cea3z]
psspy.branch_data(busMap['GOLA2'], busMap['RANCHIPG2'], "1", intgar1=1, realar1=lc[0], realar2=lc[1], 
    realar3=lc[2]) 
psspy.branch_data(busMap['GOLA2'], busMap['RANCHIPG2'], "2", intgar1=1, realar1=lc[0], realar2=lc[1], 
    realar3=lc[2])

# Co-ordinate mapping --------------
kx, ky = 70, 260
m, n = 15, 15
#{bus_key: ((bus_coords),(buslabel_offsets),(gendata_offsets),(loadlabel_offsets)) }
busMark = {
    busMap['MPL4'] : {'buloc':(kx+m*10,ky-n)}, 
    busMap['KTPS4'] : {'buloc':(kx,ky)},        
    busMap['RTPS4'] : {'buloc':(kx+m*9,ky-n*9)}, #RTPS
    busMap['DSTPS4'] : {'buloc':(kx+m*15,ky-n*4)}, #DSTPS
    busMap['BTPSA4'] : {'buloc':(kx,ky-n*4)}, #BokaroA
    busMap['MTPSB4'] : {'buloc':(kx+m*12,ky-n*9)}, #MTPS-B
    busMap['JSRBPRS4'] : {'buloc':(kx+m*4,ky-n*13)}, #JamshedpurBPRS
    #busMap['MOSABANI4'] : {'buloc':(189,70)}, #Mosabani
    busMap['RANCHIPG4'] : {'buloc':(kx-m,ky-n*9)}, #RanchiPG
    busMap['MAITHONPG4'] : {'buloc':(kx+m*9,ky-n),'buoffset':(-3,12,90)}, #MaithonPG
    busMap['PARULIAPG4'] : {'buloc':(kx+m*18,ky-n*3)}, #DurgapurPG
    busMap['JAMSHEDPURPG4'] : {'buloc':(kx+m*4,ky-n*12)}, #JamshdepurPG
    busMap['BARIPADAPG4'] : {'buloc':(kx+m*4,ky-n*15)}, #BaripadaPG
    busMap['BIHARSHRIFPG4'] : {'buloc':(50,275)}, #BiharsharifPG
    busMap['GAYAPG4'] : {'buloc':(kx,ky+n)}, #GayaPG
     
    busMap['BIDHANNG2'] : {'buloc':(kx+m*18,ky-n*6)}, 
    busMap['JODAIS2'] : {'buloc':(kx-m,ky-n*13)}, 
    busMap['BTPSB2'] : {'buloc':(kx+m*2,ky-n*5)}, 
    busMap['CTPS2'] : {'buloc':(kx+m*4,ky-n*5)}, 
    busMap['DTPS2'] : {'buloc':(kx+m*15,ky-n*6)}, 
    busMap['KALYANESWARI2'] : {'buloc':(kx+m*7,ky-n*5./3.)}, 
    busMap['MUCHIPARA2'] : {'buloc':(kx+m*16,ky-n*3)}, 
    busMap['DHANBAD2'] : {'buloc':(kx+m*4,ky-n*4),'buoffset':(0,9,45)}, 
    busMap['MTPS2'] : {'buloc':(kx+m*13,ky-n*3)}, 
    busMap['BURNPUR2'] : {'buloc':(kx+m*9,ky-n*5./3.)}, 
    busMap['RAMGARH2'] : {'buloc':(kx+m,ky-n*5),'buoffset':(-19,0,0)}, 
    busMap['JAMSHEDPUR2'] : {'buloc':(kx+m*2,ky-n*13)}, 
    #busMap['RANIGUNJ2'] : {'buloc':(296,190)}, 
    busMap['BARJORA2'] : {'buloc':(kx+m*13,ky-n*10)}, 
    busMap['PARULIA2'] : {'buloc':(kx+m*16,ky-n*5)}, 
    busMap['GOLA2'] : {'buloc':(kx+m*2.5,ky-n*8)}, 
    busMap['GIRIDIH2'] : {'buloc':(kx+m*4,ky-n*3)}, 
    busMap['KODERMA2'] : {'buloc':(kx,ky-n)}, 
    #busMap['RTPS2'] : {'buloc':(190,160)}, 
    #busMap['MOSABANI2'] : {'buloc':(200,55)}, 
    #busMap['CHAS2'] : {'buloc':(kx+m*3,ky-n*6)}, 
    #busMap['DSTPS2'] : {'buloc':(kx+m*15,ky-n*5)}, 
    #busMap['KHARAGPUR2'] : {'buloc':(305,40)}, 
    #busMap['PANAGARH2'] : {'buloc':(kx+m*16,ky-n*10)}, 
    #busMap['BURDWAN2'] : {'buloc':(kx+m*18,ky-n*10)}, 
    #busMap['NKPURA2'] : {'buloc':(40,189)}, 
    #busMap['PATRATU2'] : {'buloc':(70,187)}, 
    #busMap['MEJIAB2'] : {'buloc':(kx+m*12,ky-n*10)}, 
    #busMap['KALIPAHARI2'] : {'buloc':(kx+m*11,ky-n*5./3.)}, 
    #busMap['JAMURIA2'] : {'buloc':(kx+m*15,ky-n*5)}, 
    busMap['PARULIAPG2'] : {'buloc':(kx+m*18,ky-n*5)}, 
    busMap['MAITHONPG2'] : {'buloc':(kx+m*7,ky-n)}, 
    busMap['RANCHIPG2'] : {'buloc':(kx-m, ky-n*8)}, 
     
    busMap['BTPSB1'] : {'buloc':(kx+m*2,ky-n*4)}, 
    busMap['MOSABANI1'] : {'buloc':(kx+m*7,ky-n*14)}, 
    busMap['BURDWAN1'] : {'buloc':(kx+m*18,ky-n*11)}, 
    busMap['BELMURI1'] : {'buloc':(kx+m*18,ky-n*12)}, 
    busMap['HOWRAH1'] : {'buloc':(kx+m*18,ky-n*13)}, 
    busMap['KHARAGPUR1'] : {'buloc':(kx+m*16,ky-n*14),'buoffset':(-12,0,0)}, 
    busMap['CTPS1'] : {'buloc':(kx+m*4,ky-n*6)}, 
    busMap['KOLAGHAT1'] : {'buloc':(kx+m*18,ky-n*14)}, 
    busMap['JAMSHEDPUR1'] : {'buloc':(kx+m*2,ky-n*14)}, 
    busMap['DTPS1'] : {'buloc':(kx+m*15,ky-n*7)}, 
    busMap['BARHI1'] : {'buloc':(kx,ky-n*3)}, 
    busMap['MAITHONHYDL1'] : {'buloc':(kx+m*7,ky-n*4),'buoffset':(-5,6,90)}, 
    busMap['MAITHONGT1'] : {'buloc':(kx+m*7,ky-n*5),'buoffset':(-5,6,90)}, 
    busMap['PANCHETHYDL1'] : {'buloc':(kx+m*8,ky-n*5)}, 
    busMap['KODERMAN1'] : {'buloc':(kx,ky-n*2),'buoffset':(-18,0,0)}, 
    busMap['HAZARIBAGH1'] : {'buloc':(kx-m,ky-n*3),'buoffset':(-9,0,0)}, 
    busMap['GOLA1'] : {'buloc':(kx+m,ky-n*7)}, 
    busMap['CHANDIL1'] : {'buloc':(kx+m,ky-n*14),'buoffset':(-20,0,0)}, 
    busMap['PUTKI1'] : {'buloc':(kx+m*6,ky-n*6),'buoffset':(-4,-4,90)}, 
    busMap['KALIPAHARI1'] : {'buloc':(kx+m*11,ky-n*3)}, 
    busMap['ASP1'] : {'buloc':(kx+m*15,ky-n*8)}, 
    busMap['RAMGARH1'] : {'buloc':(kx+m,ky-n*6)}, 
    busMap['KALYANESWARI1'] : {'buloc':(kx+m*7,ky-n*3)}, 
    busMap['KUMARDUBI1'] : {'buloc':(kx+m*8,ky-n*4)}, 
    busMap['PATHERDIH1'] : {'buloc':(kx+m*7,ky-n*6)}, 
    busMap['NIMIAGHAT1'] : {'buloc':(kx+m*6,ky-n*2)}, 
    busMap['GIRIDIHN1'] : {'buloc':(kx+m*4,ky-n*2)},
    busMap['GIRIDIHO1'] : {'buloc':(kx+m*5,ky-n*2)},
    busMap['SINDRI1'] : {'buloc':(kx+m*7,ky-n*7)}, 
    busMap['RAMKANALI1'] : {'buloc':(kx+m*8,ky-n*8)}, 
    busMap['PATRATU1'] : {'buloc':(kx,ky-n*6),'buoffset':(-2,-6,90)}, 
    busMap['NKPURA1'] : {'buloc':(kx-m,ky-n*6),'buoffset':(-15,0,0)}, 
    busMap['DHANBAD1'] : {'buloc':(kx+m*5,ky-n*4),'buoffset':(1,-4,90)}, 
    busMap['PURULIA1'] : {'buloc':(kx+m*4,ky-n*10)}, 
    busMap['JAMURIA1'] : {'buloc':(kx+m*14,ky-n*8)}, 
    busMap['KONAR1'] : {'buloc':(kx+m*2,ky-n*3)}, 
    busMap['BARJORA1'] : {'buloc':(kx+m*13,ky-n*11)}, 
    busMap['KODERMAO1'] : {'buloc':(kx+m,ky-n*2)}, 
    busMap['BIADA1'] : {'buloc':(kx+m*3,ky-n*7),'buoffset':(-4,-4,90)}, 
    #busMap['MUGMA1'] : {'buloc':(209,208)}, 
    #busMap['CHAS1'] : {'buloc':(kx+m*4,ky-n*7)}, 
}

# {branch_key: ((branch_segs_intermediate_pts),(pfdata_offsets)) }
branchMark = {
    (busMap['MAITHONHYDL1'], busMap['PATHERDIH1']) : {'poffset':(0,0)}, 
    (busMap['KALYANESWARI1'], busMap['KALIPAHARI1']) : {'poffset':(0,0)}, 
    (busMap['JAMURIA1'], busMap['RAMKANALI1']) : {'poffset':(0,0)}, 
    (busMap['HOWRAH1'], busMap['BELMURI1']) : {'poffset':(0,0)}, 
    #(44106, 44115) : {'poffset':(1,-2)}, #CTPS - GOLA
    (busMap['PARULIAPG2'], busMap['PARULIA2']) : {'poffset':(-1,-4)}, 
    (busMap['KALYANESWARI2'], busMap['CTPS2']) : {'interpts':((kx+m*3,ky-n*5./3.),(kx+m*3,ky-n*4))}, 
    (busMap['KALYANESWARI2'], busMap['KALYANESWARI1']) : {'poffset':(-8,-1)}, 
    (busMap['MAITHONPG2'], busMap['DHANBAD2']) : {'interpts':((kx+m*3.5,ky-n),(kx+m*3.5,ky-n*4))}, 
    (busMap['KTPS4'], busMap['KODERMA2']) : {'poffset':(1,0)}, 
    (busMap['CTPS2'], busMap['CTPS1']) : {'poffset':(1,0)}, 
    (busMap['DTPS2'], busMap['DTPS1']) : {'poffset':(1,1)}, 
    #(busMap['KALYANESWARI2'], busMap['KALIPAHARI2']) : {'interpts':((kx+m*7.5,ky-n*5./3.5),(kx+m*10.5,ky-n*5./3.5))}, 
    (busMap['JAMSHEDPUR2'], busMap['JODAIS2']) : {'poffset':(0,0)}, 
    (busMap['KODERMA2'], busMap['KODERMAN1']) : {'poffset':(1,0)}, 
    (busMap['GIRIDIH2'], busMap['KODERMA2']) : {'poffset':(2,-2)}, 
    (busMap['MTPS2'], busMap['GOLA2']) : {'interpts':((kx+m*5,ky-n*8),)}, 
    #(44207, 44230) : {'interpts':((kx+m*5,ky-n*8),(kx+m*3.5,ky-n*8))}, #MTPS - BSL GIS
    (busMap['MTPS2'], busMap['BURNPUR2']) : {'interpts':((kx+m*13,ky-n*5./4.),(kx+m*9.5,ky-n*5./4.))}, 
    #(busMap['PARULIA2'], busMap['DSTPS2']) : {'poffset':(-1,-4)}, 
    #(44219, 46201) : {'interpts':((kx+m*1.75,ky-n*8.5),(kx-m*0.15,ky-n*8.5))}, #GOLA2 - HATIAPG
    (busMap['MPL4'], busMap['RANCHIPG4']) : {'interpts':((kx+m*10,ky-n*9.3),(kx-m*0.8,ky-n*9.3))}, 
    (busMap['MTPSB4'], busMap['MAITHONPG4']) : {'interpts':((kx+m*12,ky-n*0.7),(kx+m*9.2,ky-n*0.7))}, 
    (busMap['KTPS4'], busMap['BTPSA4']) : {'interpts':((kx-2*m,ky),(kx-2*m,ky-n*4)),'poffset':(0,0)}, 
    (busMap['MTPSB4'], busMap['JAMSHEDPURPG4']) : {'poffset':(0,-3)}, 
    }

