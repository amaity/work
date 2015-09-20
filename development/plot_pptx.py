from plot_utils import get_buscoords, get_busdetails, get_buoffsets, \
                       rect, polar, calc_segs, reformat, RGB, \
                       get_intermediate_points, get_poffsets, check_bus
from psse_utils import run_psse
businfo, mybusdat, rbusinfo, rgenbus, myloadinfo, brnflow, trfflow = run_psse()

# from pptx import Presentation
# from pptx.enum.shapes import MSO_SHAPE
# from pptx.util import Mm, Pt, Inches
# from pptx.dml.color import RGBColor

import win32com.client
from MSO import * # MSPPT
# Open PowerPoint
Application = win32com.client.Dispatch("PowerPoint.Application")
"""
Run Python/Lib/site-packages/win32com/client/makepy.py and pick 
'Microsoft Office 12.0 Object Library' and 'Microsoft PowerPoint 12.0 Object Library'. 
(If you have a version of Office other than 12.0, pick your version.)

This creates two Python files. Rename these files as MSO.py and MSPPT.py and do this:

g = globals()
for c in dir(MSO.constants):    g[c] = getattr(MSO.constants, c)
for c in dir(MSPPT.constants):  g[c] = getattr(MSPPT.constants, c)

This makes constants like ppLayoutBlank, msoShapeRectangle, etc. available. 
Now a blank slide can be created and a rectangle added in Python just like in Visual Basic.
"""
# Powerflow plot sized for A3 paper (420x297)mm ~ (16.5x11.7)in ~ (1190x842)pt
# Slide default size is 10"x7.5" (254x190)mm ~ (1024x768)pixels @ 96dpi
# Viewport/slide coordinates : (720x540)pt (w x h)
# Following data in points:
shp_width = 9 
shp_height = 9 
txt_width = 55
txt_height = 1 

def pptx_bus_trace(bdat):
	for bus in bdat:
		if check_bus('bus',bus):
			dot, busname = get_busdetails(businfo,bus)
			x, y = get_buscoords(bus)
			shp_left = ((720./420.)*x)-(shp_width/2.)
			shp_top = (540.-(540./297.)*y)-(shp_height/2.)
			oshp = Slide.Shapes.AddShape( msoShapeOval, shp_left, shp_top, 
				shp_width, shp_height)
			colr, busname = get_busdetails(businfo,bus)
			r,g,b = reformat(colr)
			oshp.Line.Visible = msoFalse
			fill = oshp.Fill
			fill.Solid
			fill.ForeColor.RGB = RGB(r,g,b)
			txt_left = shp_left+1
			txt_top = shp_top
			txBox = Slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 
				txt_left, txt_top, txt_width, txt_height)
			tf = txBox.TextFrame.TextRange
			tf.Text = busname
			tf.Font.Name = 'Calibri'
			tf.Font.Size = 8

from itertools import tee, izip

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def pptx_add_lines(xar,yar,colr):
	arr = zip(xar,yar)
	for pair in pairwise(arr):
		x0, y0, x1, y1 = [elem for tup in pair for elem in tup]
		StartX = (720./420.)*x0
		StartY = 540.-(540./297.)*y0
		EndX = (720./420.)*x1
		EndY = 540.-(540./297.)*y1
		line = Slide.Shapes.AddLine(StartX, StartY, EndX, EndY)
		line.Line.Weight = 1.5
		r,g,b = reformat(colr)
		line.Line.ForeColor.RGB = RGB(r,g,b)

def pptx_place_arrows_pfdata(xar,yar,colr,pdat):
	pass

def pptx_brn_trace(brndat):
    for brn in brndat:
        if check_bus('brn',brn):
            key = (brn[0],brn[1])
            rkey = tuple(reversed(key))
            colr, busname = get_busdetails(businfo,brn[0])
            xar, yar = get_intermediate_points(key)
            line = pptx_add_lines(xar,yar,colr)
            
            # if brn[4]>0: # check powerflow direction
            #     args = (key,0.5,6,colr,brn[2])
            # else:
            #     args = (rkey,0.5,6,colr,brn[2])
            # place_arrows_pfdata(*args)

        
if __name__ == '__main__':
	# Add a presentation
	Presentation = Application.Presentations.Add()
	Slide = Presentation.Slides.Add(1, ppLayoutTitle)
	Slide.Shapes.Title.TextFrame.TextRange.Text = "DVC NETWORK"
	Slide.Shapes(2).TextFrame.TextRange.Text = "System Planning & Engineering"
	Slide = Presentation.Slides.Add(2, ppLayoutBlank)
	pptx_brn_trace(brnflow)
	pptx_bus_trace(mybusdat)
	Presentation.SaveAs("E:\Code\work\development\dvc.pptx")
	Presentation.Close


	# prs = Presentation()
	# title_slide_layout = prs.slide_layouts[0]
	# slide = prs.slides.add_slide(title_slide_layout)
	# title = slide.shapes.title
	# subtitle = slide.placeholders[1]
	# title.text = "Damodar Valley Corporation"
	# subtitle.text = "System Planning & Engineering"
	# slide = prs.slides.add_slide(prs.slide_layouts[6])
	# shapes = slide.shapes
	# pptx_bus_trace(mybusdat)
 #    #trn_trace(trfflow)
 #    #bus_trace(mybusdat)
	# prs.save('dvc.pptx')
