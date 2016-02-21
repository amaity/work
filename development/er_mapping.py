k = 10
x, y = 7, 5
m, n = 15, 15

#{bus_key: ((bus_lat_long),(buslabel_offsets),(gendata_offsets),(loadlabel_offsets)) }
# lat, long in decimal degrees
busMark = {
    40400 : {'buloc':(25.594095, 85.137565)}, #PATNA
    40409 : {'buloc':(25.753343, 87.48103)}, #PURNEA
    45400 : {'buloc':(23.3441, 85.309562)}, #RANCHI
    45405 : {'buloc':(22.804567, 86.202875)}, #JAMSHEDPUR
    45413 : {'buloc':(25.163041, 85.513264)}, #BIHARSHARIFPG
    45415 : {'buloc':(25.753343, 87.48103)}, #NEW PURNEA
    45424 : {'buloc':(26.120888, 85.36472)}, #MUZAFFARPUR
    45425 : {'buloc':(24.775701, 86.822034)}, #BARH
    45435 : {'buloc':(24.624509, 84.946933)}, #GAYA
    45436 : {'buloc':(22.547436, 85.802537)}, #CHAIBASA
    45702 : {'buloc':(24.949036, 84.03143)}, #SASARAM7
    45704 : {'buloc':(23.305271, 85.409238)}, #RANCHI7
    45900 : {'buloc':(24.949036, 84.03143)}, #SASARAM4

    41224 : {'buloc':(26.486378, 89.500203)}, #BIRPARA
    40222 : {'buloc':(25.556044, 84.660331)}, #ARRAH
    }



# {branch_key: ((branch_segs_intermediate_pts),(pfdata_offsets)) }
branchMark = {
    (44111, 44123) : {'poffset':(0,0)}, #MHS - PATHERDIH

    }

