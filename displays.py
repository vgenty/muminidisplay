#!/usr/bin/env python

import grid
import sys
import pmt
import styles as s
from ROOT import TCanvas, TPaveText, TH2D, TH2I
from ROOT import gStyle

# './display.py filename.root events_number
def main():
    file_name = sys.argv[1]
    event     = int(sys.argv[2])
    
    my_grid = grid.gridit(file_name,event)
    grid_can = TCanvas('grid_can','grid_can',650,1100)
    grid_can.Divide(1,2)
    grid_can.cd(1)
    my_grid[0].Draw('colz')
    grid_can.cd(2)
    my_grid[1].Draw('colz')
    
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

