#!/usr/bin/env python

import grid
import sys
import pmt
import styles as s
from ROOT import TCanvas, TPaveText, TH2D, TH2I
from ROOT import gStyle

def fixtpt(tpt):
    tpt.SetTextFont(63)
    tpt.SetTextSize(22)
    tpt.SetFillColor(0)
    tpt.SetBorderSize(0)

# './display.py filename.root events_number
def main():

    file_name = sys.argv[1]
    event     = int(sys.argv[2])
    
    #Draw 2D event display
    my_grid = grid.gridit(file_name,event)
    grid_can = TCanvas('grid_can','grid_can',650,1100)
    grid_can.Divide(1,2)
    grid_can.cd(1)
    my_grid[0].Draw('colz')
    tpt1 = TPaveText(0.1287989,0.9150066,0.3688949,0.9585823,'brNDC')
    tpt1.AddText('Top Grid')
    fixtpt(tpt1)
    tpt1.Draw('same')
    grid_can.cd(2)
    my_grid[1].Draw('colz')
    tpt2 = TPaveText(0.1287989,0.9150066,0.3688949,0.9585823,'brNDC')
    tpt2.AddText('Bottom Grid')
    fixtpt(tpt2)
    tpt2.Draw('same')

    #Draw PMT view
    s.style()
    pmt_canvas=TCanvas("pmt_canvas","pmt_canvas")
    pmt_canvas.cd()
    pmt_canvas.SetGridx()
    pmt_canvas.SetGridy()
    p = pmt.pmt_draw(file_name,event)
    p[0].Draw("COLZ")
    for y in p[1]:
        y.Draw("SAMES")
    p[2].Draw("SAMES")
    pmt_canvas.Update()
    pmt_canvas.Modified()
    
    sys.stdin.readline()
    
if __name__ == '__main__':
    main()

