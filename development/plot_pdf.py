from settings import *
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# helper functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def place_lines(key,mode,colr):
    xar, yar = get_intermediate_points(key)
    #import pdb; pdb.set_trace()
    if mode == 'brn':
        plt.plot(xar,yar,color=colr,zorder=1)
    elif mode == 'trn':
        mxar, myar = (xar[0]+xar[1])/2., (yar[0]+yar[1])/2.
        plt.plot([xar[0],mxar],[yar[0],myar],color=colr,zorder=1)
    elif mode == 'oln':
        plt.plot(xar,yar,color=colr,linestyle='--')

def place_arrows_pfdata(key,wid,fnt,colr,pdat):
    xtr, ytr = get_intermediate_points(key)
    dxt, dyt = get_poffsets(key)
    dxtr, dytr = calc_segs(xtr,ytr)[:2]
    ax.arrow(xtr[0],ytr[0],dxtr,dytr,head_width=wid,color=colr)
    plt.text(xtr[0]+dxt+dxtr+1, ytr[0]+dyt+dytr+1, int(pdat), fontsize=fnt)

def place_circles(key,rad,colr,fill=False):
    x, y = get_buscoords(key)
    dx1, dy1 = calc_segs(x,y,1)[:2]
    circ = plt.Circle((x[0]+dx1,y[0]+dy1), rad, color=colr, fill=False)
    ax.add_artist(circ)

#bus markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bus_trace(businfo,bdat,tiebusdat):
    for bus in bdat:
        if check_bus('bus',bus):
            colr, busname = get_busdetails(businfo,bus)
            x, y = get_buscoords(bus)
            ax.plot(x, y, color=colr, marker='o')
            dx, dy, ang = get_buoffsets(bus)
            plt.text(x+1+dx, y+1+dy, busname, fontsize=6, rotation=ang)
            if bus in tiebusdat:
                circ = plt.Circle((x,y), 2, color='black', fill=False)
                ax.add_artist(circ)

#generation markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def gen_trace(gdat):
    for bus in gdat:
        if check_bus('gen',bus):
            x, y = get_buscoords(bus[0])
            plt.annotate(int(bus[1]), xy=(x, y),
                        xytext=(x+2, y+5),
                        bbox=dict(boxstyle="round", fc="0.8"),
                        arrowprops=dict(arrowstyle="->"), fontsize=6)

#load markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def load_trace(ldat):
    for bus in ldat:
        if check_bus('load',bus):
            x, y = get_buscoords(bus[0])
            dx, dy, ang = get_ldoffsets(bus[0])
            plt.text(x+dx+2, y+dy-2.5, 'L', fontsize=6,rotation=ang)
            plt.text(x+dx+4, y+dy-2.5, int(abs(bus[1])), fontsize=6,
                     rotation=ang)

#line markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def outl_trace(linedict,brnflow,mybusdat):
    for key in linedict:
        if key[0] in mybusdat and key[1] in mybusdat:
            if not [tup for tup in brnflow if sorted(key) == sorted(tup[:2])]:
                place_lines(key,'oln','k')

def brn_trace(businfo,brnflow):
    for brn in brnflow:
        if check_bus('brn',brn):
            key = (brn[0],brn[1])
            rkey = tuple(reversed(key))
            colr, busname = get_busdetails(businfo,brn[0])
            place_lines(key,'brn',colr)
            if brn[4]>0: # check powerflow direction
                args = (key,1.5,6,colr,brn[2])
            else:
                args = (rkey,1.5,6,colr,brn[2])
            place_arrows_pfdata(*args)

#transformer markings ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def trn_trace(businfo,trnflow):
    for trn in trnflow:
        if check_bus('trn',trn):
            key = (trn[0],trn[1])
            colr1, busname1 = get_busdetails(businfo,trn[0])
            rkey = tuple(reversed(key))
            colr2, busname2 = get_busdetails(businfo,trn[1])
            place_lines(key,'trn',colr1)
            place_lines(rkey,'trn',colr2)
            place_circles(key,2,colr1)
            place_circles(rkey,2,colr2)
            if trn[4] > 0:
                args = (key,1.5,6,colr1,trn[2] )
            else:
                args = (rkey,1.5,6,colr2,trn[2] )
            place_arrows_pfdata(*args)

def pdf_network(case_title,*args):
    outl_trace(branchMark,args[5],args[1])
    brn_trace(args[0],args[5])
    trn_trace(args[0],args[6])
    bus_trace(args[0],args[1],args[9])
    gen_trace(args[3])
    load_trace(args[4])
    ax.set_xlim(0,410)
    ax.set_ylim(0,287)
    ax.axes.get_xaxis().set_visible(True)
    ax.axes.get_yaxis().set_visible(True)
    plt.text(300, 270, 'Damodar Valley Corporation', fontsize=12)
    plt.text(300, 265, 'Gen in MW,', fontsize=10)
    plt.text(327, 265, 'Branchflow in MVA,', fontsize=10)
    plt.text(370, 265, 'Load in MVA', fontsize=10)
    plt.text(300, 260, '-400KV', color='red', fontsize=10)
    plt.text(320, 260, '-220KV', color='blue', fontsize=10)
    plt.text(340, 260, '-132KV', color='green', fontsize=10)
    plt.text(360, 260, '- -OUT', color='black', fontsize=10)
    plt.text(300, 255, '{0}'.format(case_title), color='black', fontsize=10)
    tots = (args[7][1].real, args[8][1].real)
    plt.text(300, 250,
             'Totalgen(MW) = {0:.1f}, Totalload(MW) = {1:.1f}'.format(*tots),
             color='black', fontsize=10)
    fig.set_size_inches(16.5,11.7)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig("{0}.pdf".format(case_title), bbox_inches=extent)

    
#plot details ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##if __name__ == '__main__':
##
##    fig.set_size_inches(16.5,11.7)
##    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
##    fig.savefig("loadflow.pdf", bbox_inches=extent)

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

