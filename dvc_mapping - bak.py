kx, ky = 70, 260
m, n = 15, 15

#{bus_key: ((bus_coords),(buslabel_offsets),(gendata_offsets),(loadlabel_offsets)) }
busMark = {
     44400 : {'buloc':(kx+m*10,ky-n)}, #maithonRB
     44402 : {'buloc':(kx,ky)},        #KTPS
     44403 : {'buloc':(kx+m*9,ky-n*9)}, #RTPS
     44404 : {'buloc':(kx+m*14,ky-n*4)}, #DSTPS
     44405 : {'buloc':(kx+m,ky-n*4)}, #bokaroA
     44406 : {'buloc':(kx+m*11,ky-n*9)}, #MTPS-B
     44407 : {'buloc':(kx+m*4,ky-n*13)}, #jamshedpurBPRS
     44409 : {'buloc':(189,70)}, #mosabani
     45400 : {'buloc':(kx-m,ky-n*9)}, #ranchiPG
     45403 : {'buloc':(kx+m*9,ky-n)}, #maithonPG
     45404 : {'buloc':(333,164)}, #durgapurPG
     45405 : {'buloc':(kx+m*3,ky-n*13)}, #jamshdepurPG
     45416 : {'buloc':(kx+m*4,ky-n*15)}, #baripadaPG
     45413 : {'buloc':(50,275)}, #biharsharifPG
     45435 : {'buloc':(38,268)}, #gayaPG
     
     42212 : {'buloc':(kx-m,ky-n*13)}, #JodaIS
     44200 : {'buloc':(kx+m*2,ky-n*5)}, #BTPS
     44202 : {'buloc':(kx+m*4,ky-n*5)}, #Chandrapura
     44203 : {'buloc':(kx+m*14,ky-n*6)}, #DTPS
     44204 : {'buloc':(kx+m*7,ky-n*5./3.)}, #kalyaneswari
     44205 : {'buloc':(kx+m*16,ky-n*3)}, #durgapur
     44206 : {'buloc':(kx+m*4,ky-n*4)}, #dhanbad
     44207 : {'buloc':(kx+m*13,ky-n*3)}, #mejia(A)
     44208 : {'buloc':(kx+m*9,ky-n*5./3.)}, #burnpur
     44209 : {'buloc':(kx+m,ky-n*5),'buoffset':(-19,0,0)}, #ramgarh
     44210 : {'buloc':(kx+m*2,ky-n*13)}, #jamshedpur 
     44214 : {'buloc':(296,190)}, #ranigunj
     44217 : {'buloc':(kx+m*13,ky-n*10)}, #borjora
     44218 : {'buloc':(kx+m*16,ky-n*5)}, #parulia
     44219 : {'buloc':(102,160)}, #gola
     44220 : {'buloc':(kx+m*4,ky-n*3)}, #giridih
     44223 : {'buloc':(kx,ky-n)}, #koderma
     44227 : {'buloc':(190,160)}, #raghunathpur
     44228 : {'buloc':(200,55)}, #mosabani
     44230 : {'buloc':(154,160)}, #chas
     44231 : {'buloc':(kx+m*14,ky-n*5)}, #dstps2
     44232 : {'buloc':(305,40)}, #kharagpur
     44233 : {'buloc':(kx+m*16,ky-n*10)}, #panagarh
     44234 : {'buloc':(kx+m*17,ky-n*10)}, #burdwan
     44235 : {'buloc':(40,189)}, #northkaranpura
     44236 : {'buloc':(70,187)}, #patratu
     44239 : {'buloc':(kx+m*11,ky-n*10)}, #Mejia(B)
     44240 : {'buloc':(kx+m*11,ky-n*5./3.)}, #Kalipahari
     44241 : {'buloc':(kx+m*15,ky-n*5)}, #jamuria
     45201 : {'buloc':(kx+m*18,ky-n*5)}, #paruliaPG
     45205 : {'buloc':(kx+m*7,ky-n)}, #maithonPG
     46201 : {'buloc':(49, 125)}, #hatiaJHKD
     
     44100 : {'buloc':(kx+m*2,ky-n*4)}, #bokaro
     44101 : {'buloc':(kx+m*7,ky-n*14)}, #mosabani
     44102 : {'buloc':(kx+m*17,ky-n*11)}, #burdwan
     44103 : {'buloc':(kx+m*17,ky-n*12)}, #belmuri
     44104 : {'buloc':(kx+m*17,ky-n*13)}, #howrah
     44105 : {'buloc':(kx+m*16,ky-n*14)}, #kharagpur
     44106 : {'buloc':(kx+m*4,ky-n*6)}, #chandrapura
     44107 : {'buloc':(kx+m*17,ky-n*14)}, #kolaghat
     44108 : {'buloc':(kx+m*2,ky-n*14)}, #jamshedpur 
     44109 : {'buloc':(kx+m*14,ky-n*7)}, #DTPS
     44110 : {'buloc':(kx,ky-n*3)}, #barhi 
     44111 : {'buloc':(kx+m*7,ky-n*4),'buoffset':(-5,6,90)}, #maithon
     44112 : {'buloc':(kx+m*8,ky-n*5)}, #panchet
     44113 : {'buloc':(kx,ky-n*2),'buoffset':(-22,0,0)}, #koderma(new)
     44114 : {'buloc':(kx-m,ky-n*3),'buoffset':(-9,0,0)}, #hazaribagh
     44115 : {'buloc':(kx+m,ky-n*8)}, #gola
     44116 : {'buloc':(kx+m,ky-n*14)}, #chandil
     44117 : {'buloc':(kx+m*6,ky-n*6)}, #putki
     44118 : {'buloc':(kx+m*11,ky-n*3)}, #kalipahari
     44119 : {'buloc':(kx+m*14,ky-n*8)}, #asp
     44120 : {'buloc':(kx+m,ky-n*6)}, #ramgarh
     44121 : {'buloc':(kx+m*7,ky-n*3)}, #kalyaneswari
     44122 : {'buloc':(kx+m*8,ky-n*4)}, #kumardubi
     44123 : {'buloc':(kx+m*7,ky-n*6)}, #patherdih
     44124 : {'buloc':(kx+m*6,ky-n*2)}, #nimiaghat
     44125 : {'buloc':(kx+m*4,ky-n*2)}, #giridih
     44126 : {'buloc':(kx+m*7,ky-n*7)}, #sindri
     44127 : {'buloc':(kx+m*8,ky-n*8)}, #ramkanali
     44128 : {'buloc':(kx,ky-n*6)}, #patratu
     44129 : {'buloc':(kx-m,ky-n*6)}, #northkaranpura
     44130 : {'buloc':(kx+m*5,ky-n*4)}, #dhanbad
     44133 : {'buloc':(kx+m*4,ky-n*10)}, #purulia
     44134 : {'buloc':(kx+m*15,ky-n*6)}, #jamuria
     44135 : {'buloc':(kx+m*2,ky-n*3)}, #konar
     44136 : {'buloc':(kx+m*13,ky-n*11)}, #borjora
     44137 : {'buloc':(kx+m,ky-n*2)}, #koderma(old)
     44138 : {'buloc':(kx+m*3,ky-n*6)}, #biada
     44139 : {'buloc':(209,208)}, #mugma
     44140 : {'buloc':(154,176)}, #chas
     44141 : {'buloc':(280,200)}, #ranigunj
     44142 : {'buloc':(277,192)}, #JamuriaPST
     }

# {branch_key: ((branch_segs_intermediate_pts),(pfdata_offsets)) }
branchMark = {
    (44402, 44405) : {'interpts':((kx-2*m,ky),(kx-2*m,ky-n*4)),'poffset':(0,0)}, #KODR4 - BKROA4
    (44406, 45405) : {'poffset':(0,-3)}, #MEJIAB - JSRPG
    (44204, 44202) : {'interpts':((kx+m*3,ky-n*5./3.),(kx+m*3,ky-n*4))}, #KLYN2 - CNDP2
    (44204, 44121) : {'poffset':(-7,-1)}, # Klyn2 - Klyn1 transf
    (45205, 44206) : {'interpts':((kx+m*3.5,ky-n),(kx+m*3.5,ky-n*4))}, #MTHNPG2 - DHN2
    (44402, 44223) : {'poffset':(-8,0)}, # Kodr4 - Kodr2 ICT
    (44202, 44106) : {'poffset':(-7,0)}, # CNDP2 - CTPS1 ATR
    (44203, 44109) : {'poffset':(0,3)}, # DTPS2 - DTPS1 ATR
    (44210, 42212) : {'poffset':(0,0)}, # JSRDVC2 - JODA2
    (44223, 44113) : {'poffset':(0,2)}, # Kodr2 - Kodr1n ATR
    }

