from dvc_mapping import busMark, branchMark

def get_buscoords(key):
    if isinstance(key, (int, long)):
        x, y = (busMark[key]['buloc'][0], busMark[key]['buloc'][1])
    else:
        x, y = zip(*(busMark[key[0]]['buloc'],busMark[key[1]]['buloc']) )
    return x, y

def reformat (color):
    return int (round (color[0] * 255)), \
            int (round (color[1] * 255)), \
            int (round (color[2] * 255))

def get_busdetails(businfo,bus):
    mybus = [tup for tup in businfo if tup[0] == bus]
    if mybus[0][1] == 132.0:
        arg = (0,1,0) #'g'
    elif mybus[0][1] == 220.0:
        arg = (0,0,1) #'b'
    elif mybus[0][1] == 400.0:
        arg = (1,0,0) #'r'
    return arg, mybus[0][2]

