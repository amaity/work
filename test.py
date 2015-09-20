import numpy as np
import matplotlib.pyplot as plt 


busMark = {
     44400 : (21,13), #maithonRB
     44402 : (9,16), #KTPS
     44403 : (20,14), #RTPS
     44404 : (29,11), #DSTPS
     44405 : (13,2), #bokaroA
     44406 : (26,12), #MTPS-B
     44407 : (12,6), #jamshedpurDVC
     44409 : (18,7), #mosabani
     45400 : (29,13), #ranchiPG
     45403 : (23,12), #maithonPG
     45404 : (33,17), #durgapurPG
     45405 : (10,9), #jamshdepurPG
     45416 : (14,3), #baripadaPG
     45413 : (5,10), #biharsharifPG
     45435 : (3,16), #gayaPG
     
     # 42212 : (9,30), #JodaIS
     # 44200 : (11,19), #BTPS
     # 44202 : (15,18), #chandrapura
     # 44203 : (31,16), #DTPS
     # 44204 : (27,21), #kalyaneswari
     # 44205 : (320,153), #durgapur
     # 44206 : (183,210), #dhanbad
     # 44207 : (286,127), #mejia(A)
     # 44208 : (252,185), #burnpur
     # 44209 : (88,184), #ramgarh
     # 44210 : (127,83), #jamshedpur 
     # 44214 : (296,190), #ranigunj
     # 44217 : (308,118), #borjora
     # 44218 : (330,178), #parulia
     # 44219 : (102,160), #gola
     # 44220 : (164,232), #giridih
     # 44223 : (55,250), #koderma
     # 44227 : (190,160), #raghunathpur
     # 44228 : (200,55), #mosabani
     # 44230 : (154,160), #chas
     # 44231 : (295,175), #dstps2
     # 44232 : (305,40), #kharagpur
     # 44233 : (340,125), #panagarh
     # 44234 : (365,109), #burdwan
     # 44235 : (40,189), #northkaranpura
     # 44236 : (70,187), #patratu
     # 44239 : (265,115), #Mejia(B)
     # 44240 : (269,195), #Kalipahari
     # 45201 : (350,190), #paruliaPG
     # 45205 : (250,227), #maithonPG
     # 46201 : (49, 125), #hatiaJHKD
     
     # 44100 : (108,205), #bokaro
     # 44101 : (195,45), #mosabani
     # 44102 : (373,124), #burdwan
     # 44103 : (388,88), #belmuri
     # 44104 : (390,63), #howrah
     # 44105 : (301,28), #kharagpur
     # 44106 : (135,175), #chandrapura
     # 44107 : (378,38), #kolaghat
     # 44108 : (127,69), #jamshedpur 
     # 44109 : (290,156), #DTPS
     # 44110 : (65,240), #barhi 
     # 44111 : (234,215), #maithon
     # 44112 : (226,180), #panchet
     # 44113 : (102,266), #koderma(new)
     # 44114 : (56,212), #hazaribagh
     # 44115 : (98,148), #gola
     # 44116 : (112,92), #chandil
     # 44117 : (179,187), #putki
     # 44118 : (262,177), #kalipahari
     # 44119 : (290,148), #asp
     # 44120 : (78,171), #ramgarh
     # 44121 : (249,200), #kalyaneswari
     # 44122 : (235,194), #kumardubi
     # 44123 : (190,177), #patherdih
     # 44124 : (155,215), #nimiaghat
     # 44125 : (188,244), #giridih
     # 44126 : (190,170), #sindri
     # 44127 : (223,158), #ramkanali
     # 44128 : (46,177), #patratu
     # 44129 : (20,176), #northkaranpura
     # 44130 : (195,197), #dhanbad
     # 44133 : (176,138), #purulia
     # 44134 : (280,175), #jamuria
     # 44135 : (107,215), #konar
     # 44136 : (308,128), #borjora
     # 44137 : (118,275), #koderma(old)
     # 44138 : (130,165), #biada
     # 44139 : (209,208), #mugma
     # 44140 : (15,17), #chas
     # 44141 : (28,20), #ranigunj
     # 44142 : (27,19), #JamuriaPST
     }

lx = list(set([tup[0] for tup in busMark.values()]))
ly = list(set([tup[1] for tup in busMark.values()]))

xpaper, xpoints = 410, 36
ypaper, ypoints = 280, 18

# def set_grid_cross(ax, in_back=True):
#     xticks = ax.get_xticks()
#     yticks = ax.get_yticks()
#     xgrid, ygrid = np.meshgrid(xticks, yticks)
#     kywds = dict()
#     if in_back:
#         kywds['zorder'] = 0
#     grid_lines = ax.plot(xgrid, ygrid, 'yo', **kywds)

xvals = np.linspace(0,xpaper,xpoints)
#mx = np.ma.array(xvals, mask=False)
#mx.mask[lx] = True
yvals = np.linspace(0,ypaper,ypoints)
#my = np.ma.array(yvals, mask=False)
#my.mask[ly] = True
xgrid, ygrid = np.meshgrid(xvals, yvals)
positions = np.vstack([xgrid.ravel(), ygrid.ravel()])

mx = xvals[[tup[0] for tup in busMark.values()]]
my = yvals[[tup[1] for tup in busMark.values()]]
ax1 = plt.subplot(111)
ax1.plot(mx, my, 'yo')
#set_grid_cross(ax1)
ax1.set_xlim([0,xpaper])
ax1.set_ylim([0,ypaper])
plt.show()