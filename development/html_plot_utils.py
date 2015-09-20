import json
from psse_utils import run_psse
from dvc_mapping import busMark, branchMark

def to_json(*args):
    buskeys = ["bnum","base","name"]
    brnkeys = ["from","to","flow","nckts","flowdir"]
    nodes = [dict(zip(buskeys,row)) for row in args[2]]
    mybrnlstofdicts = [dict(zip(brnkeys,row)) for row in args[5]]
    mytrnlstofdicts = [dict(zip(brnkeys,row)) for row in args[6]]
    links = mybrnlstofdicts + mytrnlstofdicts
    #print links
    with open('data.json', 'w') as f:
        json.dump({"nodes":nodes, "links":links, "nodelocations":busMark,
                   "linkpaths":{str(k): v for k, v in branchMark.iteritems()}},f)


if __name__ == '__main__':
    args = run_psse()
    #print args[1]
    to_json(*args)
    

