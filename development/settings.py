import os,sys
import numpy as np

#PSSE_LOCATION = r"C:\Program Files\PTI\PSSE33\PSSBIN"
PSSE_LOCATION = r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE_LOCATION)
os.environ['PATH'] = os.environ['PATH'] + ';' +  PSSE_LOCATION 

import psspy
import redirect
redirect.psse2py()

from Q3_2015_16_file_map import * #PLAN_12TH_file_map
psspy.psseinit(9000)
psspy.case(SAVFILE_LOCATION + CASE)

from psse_utils import run_psse
from plot_utils import *
from plot_pdf import pdf_network
