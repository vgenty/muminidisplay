import styles      as s
import fibers      as f
import pmt_methods as m
import sys
from ROOT import TCanvas, TH2D, gStyle, TFile
from ROOT import TPaveText  


def pmt_draw(the_file,event):
    s.style()    
    c=TCanvas("c1","c1");
    face=m.pmtface()
    #Create Text
    text = [m.tpaver("%s" % str(x+4*y),float((x+1)%16),float((y+1)%16)) for x in xrange(4) for y in xrange(4)]    
    title=m.pmttitle("PMT View")
    
    #Create pixel map
    values = f.fiber(the_file,event)
    pmt = m.pmt_hist(values,face)

    #Fix plot and draw it on a grid
    s.fix_plot(pmt)
    pmt.SetTitle(";Column;Row")
    pmt.Draw("COLZ")
    c.SetGridy()
    c.SetGridx()
    c.Update()
    c.Modified()

    #Draw text
    for y in text :
        y.Draw("sames")
    title.Draw("sames")
    c.Update()
    c.Modified()
    
    sys.stdin.readline()
