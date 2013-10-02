import styles      as s
import fibers      as f
import pmt_methods as m
from ROOT import TH2D, TFile
from ROOT import TPaveText  


def pmt_draw(the_file,event):
    #Map PMT - 4X4 grid
    face=m.pmtface()
    
    #Create Text
    text = [m.tpaver("%s" % str(x+4*y),float((x+1)%16),float((y+1)%16)) for x in xrange(4) for y in xrange(4)]    
    title=m.pmttitle("PMT View")
    
    #Create pixel map
    values = f.fiber(the_file,event)
    pmt = m.pmt_hist(values,face)

    s.fix_plot(pmt)
    pmt.SetTitle(";Column;Row")
    
    #Return
    for_display=[]
    for_display.append(pmt)
    for_display.append(text)
    for_display.append(title)

    return for_display
