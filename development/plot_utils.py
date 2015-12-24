from dvc_mapping import busMark, branchMark
import math
import numpy as np


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

def check_bus(elem,var):
	if elem == 'bus':
		if var in busMark:
			return True
	elif elem == 'load' or elem == 'gen':
		if var[0] in busMark:
			return True
	elif elem == 'brn' or elem == 'trn':
		if var[0] in busMark and var[1] in busMark:
			return True


def get_buscoords(bus):
	if isinstance(bus, (int, long)):
		x, y = (busMark[bus]['buloc'][0], busMark[bus]['buloc'][1])
	else:
		x, y = zip(*(busMark[bus[0]]['buloc'],busMark[bus[1]]['buloc']) )
	return x, y

def reformat (color):
	return int (round (color[0] * 255)), \
			int (round (color[1] * 255)), \
			int (round (color[2] * 255))

def RGB(r,g,b):
	return r + g*256 + b*256**2

def get_busdetails(businfo,bus):
        coltup = (0,0,0)
	mybus = [tup for tup in businfo if tup[0] == bus]
	if mybus[0][1] == 132.0:
		coltup = (0,0.5,0) 
	elif mybus[0][1] == 220.0:
		coltup = (0,0,1) 
	elif mybus[0][1] == 400.0:
		coltup = (1,0,0) 
	return coltup, mybus[0][2]

def get_buoffsets(bus):
	if 'buoffset' in busMark[bus]:
		tup0, tup1, tup2 = busMark[bus]['buoffset'] 
	else:
		tup0, tup1, tup2 = 0,0,0
	return tup0, tup1, tup2

def get_ldoffsets(bus):
	if 'ldoffset' in busMark[bus]:
		tup0, tup1, tup2 = busMark[bus]['ldoffset'] 
	else:
		tup0, tup1, tup2 = 0,0,0
	return tup0, tup1, tup2

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

    
