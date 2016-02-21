kx, ky = 70, 260
m, n = 15, 15

busMap = {
    'MAITHONRB4'    : 44400,
    'KTPS4'         : 44402,  #244002
    'RTPS4'         : 44403,  #234000
    'DSTPS4'        : 44404,  #234001
    'BTPSA4'        : 44405,  #244001
    'MTPSB4'        : 44406,  #234002
    'JSRBPRS4'      : 44407,  #244000
    'MOSABANI4'     : 44409,
    'RANCHIPG4'     : 45400,
    'MAITHONPG4'    : 45403,  #244003
    'PARULIAPG4'    : 45404,
    'JAMSHEDPURPG4' : 45405,  #244004
    'BARIPADAPG4'   : 45416,
    'BIHARSHRIFPG4' : 45413,
    'GAYAPG4'       : 45435,

    'BTPSBG1' : 44004,
    'BTPSBG2' : 44005,
    'BTPSBG3' : 44006,
    'DTPSG4'  : 44008,
    'DTPSG3'  : 44009,
    'BTPSAG1' : 44010,
    'MTPSBG1' : 44013,
    'MTPSBG2' : 44014,
    'CTPSG1'  : 44015,
    'CTPSG2'  : 44016,
    'CTPSG3'  : 44017,
    'CTPSG7'  : 44018,
    'CTPSG8'  : 44019,
    'MTPSG1'  : 44020,
    'MTPSG2'  : 44021,
    'MTPSG3'  : 44022,
    'MTPSG4'  : 44023,
    'MTPSG5'  : 44024,
    'MTPSG6'  : 44025,
    'KTPSG1'  : 44026,
    'KTPSG2'  : 44027,
    'RTPSG1'  : 44030,
    'RTPSG2'  : 44031,
    'DSTPSG1' : 44032,
    'DSTPSG2' : 44033,
    'RTPSG3'  : 44034,
    'RTPSG4'  : 44035,
    'KTPSG3'  : 44036,
    'KTPSG4'  : 44037,

    'BIDHANNG2'     : 41206,
    'JODAIS2'       : 42212,
    'BTPSB2'        : 44200,  #242000
    'CTPS2'         : 44202,  #242001
    'DTPS2'         : 44203,  #232000
    'KALYANESWARI2' : 44204,  #242003
    'MUCHIPARA2'    : 44205,  #232005
    'DHANBAD2'      : 44206,  #242004
    'MTPS2'         : 44207,  #232001
    'BURNPUR2'      : 44208,  #232004
    'RAMGARH2'      : 44209,  #242007
    'JAMSHEDPUR2'   : 44210,  #242002
    'RANIGUNJ2'     : 44214,
    'BARJORA2'      : 44217,  #232003
    'PARULIA2'      : 44218,  #232002
    'GOLA2'         : 44219,  #242008
    'GIRIDIH2'      : 44220,  #242005
    'KODERMA2'      : 44223,  #242006
    'RTPS2'         : 44227,
    'MOSABANI2'     : 44228,
    'CHAS2'         : 44230,
    'DSTPS2'        : 44231,
    'KHARAGPUR2'    : 44232,
    'PANAGARH2'     : 44233,
    'BURDWAN2'      : 44234,
    'NKPURA2'       : 44235,
    'PATRATU2'      : 44236,
    'MEJIAB2'       : 44239,
    'KALIPAHARI2'   : 44240,
    'JAMURIA2'      : 44241,
    'PARULIAPG2'    : 45201,
    'MAITHONPG2'    : 45205,  #242009
    'RANCHIPG2'     : 46201,

    'BTPSB1'        : 44100,  #241001
    'MOSABANI1'     : 44101,  #241011
    'BURDWAN1'      : 44102,  #231006
    'BELMURI1'      : 44103,  #231005
    'HOWRAH1'       : 44104,  #231004
    'KHARAGPUR1'    : 44105,  #231002
    'CTPS1'         : 44106,  #241002
    'KOLAGHAT1'     : 44107,  #231003
    'JAMSHEDPUR1'   : 44108,  #241005
    'DTPS1'         : 44109,  #231000
    'BARHI1'        : 44110,  #241000
    'MAITHONHYDL1'  : 44111,  #241006
    'PANCHETHYDL1'  : 44112,  #231007
    'KODERMAN1'     : 44113,
    'HAZARIBAGH1'   : 44114,  #241019
    'GOLA1'         : 44115,  #241003
    'CHANDIL1'      : 44116,  #241004
    'PUTKI1'        : 44117,  #241015
    'KALIPAHARI1'   : 44118,  #231008
    'ASP1'          : 44119,  #231009
    'RAMGARH1'      : 44120,  #241013
    'KALYANESWARI1' : 44121,  #241009
    'KUMARDUBI1'    : 44122,  #241010
    'PATHERDIH1'    : 44123,  #241007
    'NIMIAGHAT1'    : 44124,  #241021
    'GIRIDIH1'      : 44125,  #241023
    'SINDRI1'       : 44126,  #241022
    'RAMKANALI1'    : 44127,  #241012
    'PATRATU1'      : 44128,
    'NKPURA1'       : 44129,  #241020
    'DHANBAD1'      : 44130,  #241030
    'PURULIA1'      : 44133,  #231001
    'JAMURIA1'      : 44134,
    'KONAR1'        : 44135,  #241017
    'BARJORA1'      : 44136,  #231010
    'KODERMAO1'     : 44137,  #241018
    'BIADA1'        : 44138,  #
    'MUGMA1'        : 44139,
    'CHAS1'         : 44140,
    'RANIGUNJ1'     : 44141,     

    'MUCHIPARA3'    : 44305,
}
#{bus_key: ((bus_coords),(buslabel_offsets),(gendata_offsets),(loadlabel_offsets)) }
busMark = {
    busMap['MAITHONRB4'] : {'buloc':(kx+m*10,ky-n)}, 
    busMap['KTPS4'] : {'buloc':(kx,ky)},        
    busMap['RTPS4'] : {'buloc':(kx+m*9,ky-n*9)}, #RTPS
    busMap['DSTPS4'] : {'buloc':(kx+m*15,ky-n*4)}, #DSTPS
    busMap['BTPSA4'] : {'buloc':(kx,ky-n*4)}, #BokaroA
    busMap['MTPSB4'] : {'buloc':(kx+m*12,ky-n*9)}, #MTPS-B
    busMap['JSRBPRS4'] : {'buloc':(kx+m*4,ky-n*13)}, #JamshedpurBPRS
    busMap['MOSABANI4'] : {'buloc':(189,70)}, #Mosabani
    busMap['RANCHIPG4'] : {'buloc':(kx-m,ky-n*9)}, #RanchiPG
    busMap['MAITHONPG4'] : {'buloc':(kx+m*9,ky-n),'buoffset':(-3,12,90)}, #MaithonPG
    busMap['PARULIAPG4'] : {'buloc':(333,164)}, #DurgapurPG
    busMap['JAMSHEDPURPG4'] : {'buloc':(kx+m*4,ky-n*12)}, #JamshdepurPG
    busMap['BARIPADAPG4'] : {'buloc':(kx+m*4,ky-n*15)}, #BaripadaPG
    busMap['BIHARSHRIFPG4'] : {'buloc':(50,275)}, #BiharsharifPG
    busMap['GAYAPG4'] : {'buloc':(38,268)}, #GayaPG
     
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
    busMap['RANIGUNJ2'] : {'buloc':(296,190)}, 
    busMap['BARJORA2'] : {'buloc':(kx+m*13,ky-n*10)}, 
    busMap['PARULIA2'] : {'buloc':(kx+m*16,ky-n*5)}, 
    busMap['GOLA2'] : {'buloc':(kx+m*2.5,ky-n*8)}, 
    busMap['GIRIDIH2'] : {'buloc':(kx+m*4,ky-n*3)}, 
    busMap['KODERMA2'] : {'buloc':(kx,ky-n)}, 
    busMap['RTPS2'] : {'buloc':(190,160)}, 
    busMap['MOSABANI2'] : {'buloc':(200,55)}, 
    busMap['CHAS2'] : {'buloc':(kx+m*3,ky-n*6)}, 
    busMap['DSTPS2'] : {'buloc':(kx+m*15,ky-n*5)}, 
    busMap['KHARAGPUR2'] : {'buloc':(305,40)}, 
    busMap['PANAGARH2'] : {'buloc':(kx+m*16,ky-n*10)}, 
    busMap['BURDWAN2'] : {'buloc':(kx+m*18,ky-n*10)}, 
    busMap['NKPURA2'] : {'buloc':(40,189)}, 
    busMap['PATRATU2'] : {'buloc':(70,187)}, 
    busMap['MEJIAB2'] : {'buloc':(kx+m*12,ky-n*10)}, 
    busMap['KALIPAHARI2'] : {'buloc':(kx+m*11,ky-n*5./3.)}, 
    busMap['JAMURIA2'] : {'buloc':(kx+m*15,ky-n*5)}, 
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
    busMap['GIRIDIH1'] : {'buloc':(kx+m*4,ky-n*2)},
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
    busMap['MUGMA1'] : {'buloc':(209,208)}, 
    busMap['CHAS1'] : {'buloc':(kx+m*4,ky-n*7)}, 
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
    (busMap['KALYANESWARI2'], busMap['KALIPAHARI2']) : {'interpts':((kx+m*7.5,ky-n*5./3.5),(kx+m*10.5,ky-n*5./3.5))}, 
    (busMap['JAMSHEDPUR2'], busMap['JODAIS2']) : {'poffset':(0,0)}, 
    (busMap['KODERMA2'], busMap['KODERMAN1']) : {'poffset':(1,0)}, 
    (busMap['GIRIDIH2'], busMap['KODERMA2']) : {'poffset':(2,-2)}, 
    #(44207, 44219) : {'interpts':((kx+m*5,ky-n*8),)}, #MTPS - GOLA
    #(44207, 44230) : {'interpts':((kx+m*5,ky-n*8),(kx+m*3.5,ky-n*8))}, #MTPS - BSL GIS
    (busMap['MTPS2'], busMap['BURNPUR2']) : {'interpts':((kx+m*13,ky-n*5./4.),(kx+m*9.5,ky-n*5./4.))}, 
    (busMap['PARULIA2'], busMap['DSTPS2']) : {'poffset':(-1,-4)}, 
    #(44219, 46201) : {'interpts':((kx+m*1.75,ky-n*8.5),(kx-m*0.15,ky-n*8.5))}, #GOLA2 - HATIAPG
    (busMap['MAITHONRB4'], busMap['RANCHIPG4']) : {'interpts':((kx+m*10,ky-n*9.3),(kx-m*0.8,ky-n*9.3))}, 
    (busMap['MTPSB4'], busMap['MAITHONPG4']) : {'interpts':((kx+m*12,ky-n*0.7),(kx+m*9.2,ky-n*0.7))}, 
    (busMap['KTPS4'], busMap['BTPSA4']) : {'interpts':((kx-2*m,ky),(kx-2*m,ky-n*4)),'poffset':(0,0)}, 
    (busMap['MTPSB4'], busMap['JAMSHEDPURPG4']) : {'poffset':(0,-3)}, 
    }

