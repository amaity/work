from settings import *
#---------------------------------------------------------------------

from itertools import groupby
from operator import itemgetter
attr_type = itemgetter(0)


def subsystem_info(name, attributes, sid=-1, flag=1, ties=1):
    name = name.lower()
    gettypes = getattr(psspy, 'a%stypes' % name)
    apilookup = {
        'I': getattr(psspy, 'a%sint' % name),
        'R': getattr(psspy, 'a%sreal' % name),
        'X': getattr(psspy, 'a%scplx' % name),
        'C': getattr(psspy, 'a%schar' % name), }
    result = []
    ierr, attr_types = gettypes(attributes)
    for k, group in groupby(zip(attr_types, attributes), key=attr_type):
        func = apilookup[k]
        strings = list(zip(*group)[1])
        ierr, res = func(sid, flag, ties=3 if name=='brn' else None,
                          string=strings)
        result.extend(res)
    return zip(*result)

#--------------------------------------------------------------------
##for i in range(len(out_buses)):
##     psspy.load_data_3(i, intgar1=0)
##
##ierr = psspy.bsys(sid=2, numbus=len(out_buses), buses=out_buses)
##ierr, in_branches = psspy.abrnint(sid=2, string=['FROMNUMBER', 'TONUMBER'],
##                                  flag=1)
##for i in range(len(in_branches[0])):
##     psspy.branch_data(in_branches[0][i], in_branches[1][i], intgar1=0)
##ierr, in_trfs = psspy.atrnint(sid=2, string=['FROMNUMBER', 'TONUMBER'],
##                                  flag=1)
##for i in range(len(in_trfs[0])):
##     psspy.two_winding_data(in_trfs[0][i], in_trfs[1][i], intgar1=0)

###------------------------


def run_psse():
    ierr = psspy.bsys(sid=1, numzone=1, zones=DVC_ZONE)
    ierr, all_buses = psspy.abusint(sid=1, string=["NUMBER"], flag=2)
    all_buses = all_buses[0]
    ierr, in_buses = psspy.abusint(sid=1, string=['NUMBER'], flag=1)
    in_buses = in_buses[0]
    out_buses = list(set(all_buses)-set(in_buses))
    ierr = psspy.bsys(sid=2, numbus=len(out_buses), buses=out_buses)
    ierr = psspy.extr(sid=2, all=0, status2=0)
    
    status, scalval = [0,1,4,0], []
    ierr, totals, moto = psspy.scal(sid=1, all=0, apiopt=1, status=status,
                                    scalval=scalval)
    scalval = [0.,0.,totals[2],totals[3],totals[4],totals[5],0.95]
    ierr, totals, moto = psspy.scal(sid=1, all=0, apiopt=2, status=status,
                                    scalval=scalval)

    psspy.solution_parameters_3(intgar2=150, realar6=1.0) #, realar17=10.1, realar18=10.00001)
    #psspy.solv((1,0,0,0,0,0))
    psspy.fdns(options6=0) # 1 = flat start
    psspy.fnsl((1,0,0,0,0,0,99,1))
    #psspy.solv((1,0,0,0,0,0))
    #psspy.fnsl((1,0,0,0,0,0,99,1))
    #psspy.pout(sid=1, all=0)
    #n = psspy.totbus()
    #psspy.ascc_3(sid=1, all=0, status1=1, status11=1, scfile="scfile.sc")
    #psspy.ascc_scfile("scfile.sc")

    businfo = subsystem_info('bus', ['NUMBER', 'BASE', 'NAME'], sid=-1) #get list of all busses in the study file
    mybusinfo = subsystem_info('bus', ['NUMBER', 'BASE', 'NAME'], sid=1)
    mygeninfo = subsystem_info('mach', ['NUMBER', 'PGEN', 'NAME', 'ID'], sid=1)
    myloadinfo = subsystem_info('load', ['NUMBER', 'MVAACT', 'NAME'], sid=1)
    branchinfo = subsystem_info('brn', ['FROMNUMBER', 'TONUMBER', 'MVA', 'P'], sid=1)
    trfinfo = subsystem_info('trn', ['FROMNUMBER', 'TONUMBER', 'MVA', 'P'], sid=1)

    a = list(reduce(tuple.__add__,[x[:2] for x in branchinfo])) #get all the bus info from the in service branches in my zone
    b = list(reduce(tuple.__add__,[x[:2] for x in trfinfo])) #get all the bus info from the in service transfomers in my zone
    c = [x[0] for x in mybusinfo]
    d = [x[0] for x in mygeninfo]
    mybusdat = list(set(a+b+c))
    rbusdat = list(set(mybusdat).difference(d)) #my bus list sans my gen busses
    rbusinfo = [i for i in businfo for j in rbusdat if i[0]==j] #get the full details of each bus
    tiebusdat = list(set(a)-set(c)) 
    #print mybusinfo
    rbus=[]; rgenbus=[]
    for gen in mygeninfo:
        ierr, cmpval = psspy.macdt2(ibus=gen[0], id=gen[3], string="XTRAN") 
        if np.iscomplex(cmpval): #check if GT is implicit
            rbus.append(gen)  
        else:
            temp = [tup[1:] for tup in trfinfo if tup[0] == gen[0]] #if GT is explicit get remote bus num
            rbus.append(temp[0])
    #print rbus
    rbus.sort()
    for key, group in groupby(rbus, lambda x:x[0]):
        gentot=0
        for rgen in group:
            gentot += rgen[1]
        rgenbus.append((rgen[0], gentot))
    #print rgenbus
    brnflow=[]
    for key, group in groupby(branchinfo, lambda x: (x[0], x[1])):
        flow=0; fdir=0; ckt=0
        for brn in group:
            flow += brn[2]
            fdir += brn[3]
            ckt  += 1
        brnflow.append((brn[0], brn[1], int(flow), ckt, round(fdir,2) ))
    #print brnflow
    
    trfflow=[]
    for key, group in groupby(trfinfo, lambda x: (x[0], x[1])):
        flow=0; fdir=0; ckt=0
        for trf in group:
            flow += trf[2]
            fdir += trf[3]
            ckt  += 1
        trfflow.append((trf[0], trf[1], int(flow), ckt, int(fdir)))
    #print trfflow

    totgen = psspy.zndat(DVC_ZONE, "GEN")
    totload = psspy.zndat(DVC_ZONE, "LOAD")
    
    args = (businfo, mybusdat, rbusinfo, rgenbus, myloadinfo, brnflow,
            trfflow, totgen, totload, tiebusdat)
    return  args

if __name__ == '__main__':
    args = run_psse()
    

