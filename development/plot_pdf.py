import math
import numpy as np
import matplotlib.pyplot as plt
from dvc_mapping import busMark, branchMark
from psse_utils import run_psse
from plot_utils import get_buscoords, get_busdetails, get_buoffsets

businfo, mybusdat, rgenbus, myloadinfo, brnflow, trfflow = run_psse()

#bus markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig, ax = plt.subplots()

def bus_trace(bdat):
    for bus in bdat:
        if bus in busMark:
            dot, busname = get_busdetails(businfo,bus)
            x, y = get_buscoords(bus)
            ax.plot(x, y, color=dot, marker='o')
            dx, dy, ang = get_buoffsets(bus)
            plt.text(x+1+dx, y+1+dy, busname, fontsize=8, rotation=ang)

#generation markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for bus in rgenbus:
    if bus[0] in busMark:
        x, y = get_buscoords(bus[0])
        plt.annotate(int(bus[1]), xy=(x, y),
                    xytext=(x, y+4),
                    bbox=dict(boxstyle="round", fc="0.8"),
                    arrowprops=dict(arrowstyle="->"), fontsize=6)

#load markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for bus in myloadinfo:
    if bus[0] in busMark:
        x, y = get_buscoords(bus[0])
        plt.text(x+2, y-2.5, 'L', fontsize=6)
        plt.text(x+4, y-2.5, int(abs(bus[1])), fontsize=6)

#helper functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# radian if deg=0; degree if deg=1
def rect(r, w, deg=0):
    from math import cos, sin, pi
    if deg:
        w = pi*w/180.0
    return r*cos(w), r*sin(w)

# radian if deg=0; degree if deg=1
def polar(x, y, deg=0):
    from math import hypot, atan2, pi
    if deg:
        return hypot(x, y), 180.0*atan2(y, x)/pi
    else:
        return hypot(x, y), atan2(y, x)

def calc_segs(x,y,dec=0):
    theta1 = np.arctan2(y[1]-y[0],x[1]-x[0])
    theta2 = np.arctan2(y[0]-y[1],x[0]-x[1])
    dist = math.hypot(x[1]-x[0],y[1]-y[0])
    dx1, dy1 = rect((dist/2.)-dec,theta1,deg=0)
    dx2, dy2 = rect((dist/2.)-dec,theta2,deg=0)
    return dx1, dy1, dx2, dy2


def get_intermediate_points(key):
    rkey = tuple(reversed(key)) # reverse key
    if key in branchMark and 'interpts' in branchMark[key]:
        arg = key
    elif rkey in branchMark and 'interpts' in branchMark[rkey]:
        arg = rkey
    else:
        arg = None
    x,y=(get_buscoords(key) if arg == None else get_buscoords(arg) )
    xt, yt = ( ((),()) if arg == None else zip(*branchMark[arg]['interpts']))
    xar, yar = (x[0],)+xt+(x[1],), (y[0],)+yt+(y[1],)
    return xar, yar

def get_poffsets(key):
    rkey = tuple(reversed(key)) # reverse key
    if key in branchMark and 'poffset' in branchMark[key]:
        dxt, dyt = branchMark[key]['poffset'] # data location offsets
    elif rkey in branchMark and 'poffset' in branchMark[rkey]:
        dxt, dyt = branchMark[rkey]['poffset']
    else:
        dxt, dyt = 0, 0
    return dxt, dyt

    
def place_lines(key,mode,colr):
    xar, yar = get_intermediate_points(key)
    #import pdb; pdb.set_trace()
    if mode == 'brn':
        plt.plot(xar,yar,color=colr,zorder=1)
    elif mode == 'trn':
        mxar, myar = (xar[0]+xar[1])/2., (yar[0]+yar[1])/2.
        plt.plot([xar[0],mxar],[yar[0],myar],color=colr,zorder=1)

def place_arrows_pfdata(key,wid,fnt,colr,pdat):
    xtr, ytr = get_intermediate_points(key)
    dxt, dyt = get_poffsets(key)
    dxtr, dytr = calc_segs(xtr,ytr)[:2]
    ax.arrow(xtr[0],ytr[0],dxtr,dytr,width=wid,color=colr)
    plt.text(xtr[0]+dxt+dxtr+1, ytr[0]+dyt+dytr+1, int(pdat), fontsize=fnt)

def place_circles(key,rad,colr,fill=False):
    x, y = get_buscoords(key)
    dx1, dy1 = calc_segs(x,y,1)[:2]
    circ = plt.Circle((x[0]+dx1,y[0]+dy1), rad, color=colr, fill=False)
    ax.add_artist(circ)


#line markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def brn_trace(brnflow):
    for brn in brnflow:
        if brn[0] in busMark and brn[1] in busMark:
            key = (brn[0],brn[1])
            rkey = tuple(reversed(key))
            colr, busname = get_busdetails(businfo,brn[0])
            place_lines(key,'brn',colr)
            if brn[4]>0: # check powerflow direction
                args = (key,0.5,6,colr,brn[2])
            else:
                args = (rkey,0.5,6,colr,brn[2])
            place_arrows_pfdata(*args)

#transformer markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def trn_trace(trnflow):
    for trn in trnflow:
        if trn[0] in busMark and trn[1] in busMark:
            key = (trn[0],trn[1])
            colr1, busname1 = get_busdetails(businfo,trn[0])
            rkey = tuple(reversed(key))
            colr2, busname2 = get_busdetails(businfo,trn[1])
            place_lines(key,'trn',colr1)
            place_lines(rkey,'trn',colr2)
            place_circles(key,2,colr1)
            place_circles(rkey,2,colr2)
            if trn[4] > 0:
                args = (key,0.5,6,colr1,trn[2] )
            else:
                args = (rkey,0.5,6,colr2,trn[2] )
            place_arrows_pfdata(*args)

#plot details ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    brn_trace(brnflow)  
    trn_trace(trfflow)
    bus_trace(mybusdat)

    ax.set_xlim(0,410)
    ax.set_ylim(0,287)
    ax.axes.get_xaxis().set_visible(True)
    ax.axes.get_yaxis().set_visible(True)
    #ax.set_title('load flow plot')
    plt.text(300, 270, 'Damodar Valley Corporation', fontsize=12)
    plt.text(300, 265, 'Gen in MW,', fontsize=10)
    plt.text(327, 265, 'Brnchflow in MVA,', fontsize=10)
    plt.text(368, 265, 'Load in MVA', fontsize=10)
    plt.text(300, 260, '--400KV', color='red', fontsize=10)
    plt.text(320, 260, '--220KV', color='blue', fontsize=10)
    plt.text(340, 260, '--132KV', color='green', fontsize=10)
    plt.show()

    fig.set_size_inches(16.5,11.7)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig("loadflow.pdf", bbox_inches=extent)

#--------------------------------------------
#Generate Pilot_Zone reports 

# buslst=[44102,44103,44109,44111,44118,44119,44121,44203,44204,44205,44207,
#         44217,44218,44134,44233,44234,44240,44241]
# psspy.bsys(sid=9, numbus=len(buslst), buses=buslst)
# pzonebrn = subsystem_info('brn',['FROMNAME','TONAME','ID','P'],sid=9)
# pzonetrn = subsystem_info('trn',['FROMNAME','TONAME','ID','P'],sid=9)
# pzonebus = subsystem_info('bus', ['NAME', 'PU'], sid=9)
# from collections import defaultdict
# d = defaultdict(list)
# for k, v in pzonebus: d[k].append(round(v,3))

# from prettytable import PrettyTable
# def add_trn_data(lst):
#     x = PrettyTable(["FbusV in pu", "Frombus name", "TbusV in pu",
#                      "Tobus name", "Ckt ID", "Flow in MW"])
#     x.align["FbusV in pu"] = "r"
#     x.align["Frombus name"] = "l"
#     x.align["TbusV in pu"] = "r"
#     x.align["Tobus name"] = "l"
#     x.align["Ckt ID"] = "l"
#     x.align["Flow in MW"] = "r"
#     for tup in lst:
#         x.add_row([d[tup[0]],tup[0],d[tup[1]],tup[1],tup[2],round(tup[3],2)])
#     mystr = x.get_string()
#     return (mystr)
# #print add_trn_data(pzonetrn)

# def add_brn_data(lst):
#     x = PrettyTable(["FbusV in pu", "Frombus name", "TbusV in pu",
#                      "Tobus name", "Ckt ID", "Flow in MW"])
#     x.align["FbusV in pu"] = "r"
#     x.align["Frombus name"] = "l"
#     x.align["TbusV in pu"] = "r"
#     x.align["Tobus name"] = "l"
#     x.align["Ckt ID"] = "l"
#     x.align["Flow in MW"] = "r"
#     for tup in lst:
#         x.add_row([d[tup[0]],tup[0],d[tup[1]],tup[1],tup[2],round(tup[3],2)])
#     mystr = x.get_string()
#     return (mystr)
# #print add_brn_data(pzonebrn)

# def add_gen_data(lst):
#     x = PrettyTable(["Bus Name", "Gen (MW)"])
#     x.align["Bus Name"] = "l"
#     x.align["Gen (MW)"] = "l"
#     for tup in lst:
#         x.add_row([tup[2],tup[1]])
#     mystr = x.get_string()
#     return (mystr)
# #print add_gen_data(mygeninfo)

# def add_load_data(lst):
#     x = PrettyTable(["Bus Name", "Load (MVA)"])
#     x.align["Bus Name"] = "l"
#     x.align["Gen (MW)"] = "l"
#     for tup in lst:
#         x.add_row([tup[2],round(abs(tup[1]),2)])
#     mystr = x.get_string()
#     return (mystr)
# #print add_load_data(myloadinfo)
# #--------------------------------------------

