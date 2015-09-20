kx, ky = 70, 260
m, n = 15, 15

busMark = {
     44400 : (kx+m*10,ky-n*5./3.), #maithonRB
     44402 : (kx,ky), #KTPS
     44403 : (kx+m*9,ky-n*9), #RTPS
     44404 : (kx+m*14,ky-n*4), #DSTPS
     44405 : (kx+m,ky-n*4), #bokaroA
     44406 : (kx+m*11,ky-n*9), #MTPS-B
     44407 : (kx+m*4,ky-n*13), #jamshedpurBPRS
     44409 : (189,70), #mosabani
     45400 : (kx-m,ky-n*9), #ranchiPG
     45403 : (kx+m*9,ky-n*5./3.), #maithonPG
     45404 : (333,164), #durgapurPG
     45405 : (kx+m*3,ky-n*13), #jamshdepurPG
     45416 : (kx+m*4,ky-n*15), #baripadaPG
     45413 : (50,275), #biharsharifPG
     45435 : (38,268), #gayaPG
     
     42212 : (kx-m,ky-n*13), #JodaIS
     44200 : (kx+m*2,ky-n*5), #BTPS
     44202 : (kx+m*4,ky-n*5), #Chandrapura
     44203 : (kx+m*14,ky-n*6), #DTPS
     44204 : (kx+m*7,ky-n*5./3.), #kalyaneswari
     44205 : (320,153), #durgapur
     44206 : (kx+m*4,ky-n*4), #dhanbad
     44207 : (kx+m*13,ky-n*3), #mejia(A)
     44208 : (kx+m*9,ky-n*5./3.), #burnpur
     44209 : (kx+m,ky-n*5), #ramgarh
     44210 : (kx+m*2,ky-n*13), #jamshedpur 
     44214 : (296,190), #ranigunj
     44217 : (kx+m*13,ky-n*10), #borjora
     44218 : (330,178), #parulia
     44219 : (102,160), #gola
     44220 : (kx+m*4,ky-n*3), #giridih
     44223 : (kx,ky-n), #koderma
     44227 : (190,160), #raghunathpur
     44228 : (200,55), #mosabani
     44230 : (154,160), #chas
     44231 : (kx+m*14,ky-n*5), #dstps2
     44232 : (305,40), #kharagpur
     44233 : (340,125), #panagarh
     44234 : (365,109), #burdwan
     44235 : (40,189), #northkaranpura
     44236 : (70,187), #patratu
     44239 : (kx+m*11,ky-n*10), #Mejia(B)
     44240 : (kx+m*11,ky-n*5./3.), #Kalipahari
     45201 : (350,190), #paruliaPG
     45205 : (kx+m*7,ky-n), #maithonPG
     46201 : (49, 125), #hatiaJHKD
     
     44100 : (kx+m*2,ky-n*4), #bokaro
     44101 : (kx+m*7,ky-n*14), #mosabani
     44102 : (373,124), #burdwan
     44103 : (388,88), #belmuri
     44104 : (390,63), #howrah
     44105 : (301,28), #kharagpur
     44106 : (kx+m*4,ky-n*6), #chandrapura
     44107 : (378,38), #kolaghat
     44108 : (kx+m*2,ky-n*14), #jamshedpur 
     44109 : (kx+m*14,ky-n*7), #DTPS
     44110 : (kx,ky-n*3), #barhi 
     44111 : (kx+m*7,ky-n*4), #maithon
     44112 : (kx+m*8,ky-n*5), #panchet
     44113 : (kx,ky-n*2), #koderma(new)
     44114 : (kx-m,ky-n*3), #hazaribagh
     44115 : (kx+m,ky-n*8), #gola
     44116 : (kx+m,ky-n*14), #chandil
     44117 : (kx+m*6,ky-n*6), #putki
     44118 : (kx+m*11,ky-n*3), #kalipahari
     44119 : (kx+m*14,ky-n*8), #asp
     44120 : (kx+m,ky-n*6), #ramgarh
     44121 : (kx+m*7,ky-n*3), #kalyaneswari
     44122 : (kx+m*8,ky-n*4), #kumardubi
     44123 : (kx+m*7,ky-n*6), #patherdih
     44124 : (kx+m*6,ky-n*2), #nimiaghat
     44125 : (kx+m*4,ky-n*2), #giridih
     44126 : (kx+m*7,ky-n*7), #sindri
     44127 : (kx+m*8,ky-n*8), #ramkanali
     44128 : (kx,ky-n*6), #patratu
     44129 : (kx-m,ky-n*6), #northkaranpura
     44130 : (kx+m*5,ky-n*4), #dhanbad
     44133 : (kx+m*4,ky-n*10), #purulia
     44134 : (280,175), #jamuria
     44135 : (kx+m*2,ky-n*3), #konar
     44136 : (kx+m*13,ky-n*11), #borjora
     44137 : (kx+m,ky-n*2), #koderma(old)
     44138 : (kx+m*3,ky-n*6), #biada
     44139 : (209,208), #mugma
     44140 : (154,176), #chas
     44141 : (280,200), #ranigunj
     44142 : (277,192), #JamuriaPST
     }

pfOffset = {
    (44406, 45405) : (0, -3), #mejiaB - jsrPG
    (44204, 44121) : (-7, -1), # Klyn2 - Klyn1 transf
    (44223, 44113) : (0, 2), # Kodr2 - Kodr1n ATR
    (44402, 44223) : (-8, 0), # Kodr4 - Kodr2 ICT
    (44202, 44106) : (-7,0), # CNDP2 - CTPS1 ATR
    (44203, 44109) : (0,3), # DTPS2 - DTPS1 ATR
    }

connecTrace = {
     
     }
