import sys
from ROOT import TFile, TTree, TH2I, gStyle, TLatex, TCanvas, gPad
import fibers as f

def gridit(root_file,user_event):
    gStyle.SetOptStat(0)
    n_extrusions = 32
    top_grid = TH2I('top_grid',
                    ';x [mm] (extrusions 0 #rightarrow 7);y [mm] (extrusions 8 #rightarrow 15)',
                    8,0,250,8,0,250)
    bot_grid = TH2I('bot_grid',
                    ';x [mm] (extrusions 16 #rightarrow 23);y [mm] (extrusions 24 #rightarrow 31)',
                    8,0,250,8,0,250)
    hit_pixels = f.fiber(root_file,int(user_event))
    mapfile    = open('mapfile.csv')
    hit_map    = f.mapping(mapfile)

    for pixel_index in hit_pixels:
        if hit_map[pixel_index][0] == 0 or hit_map[pixel_index][1] == 0:
            for b in range(1,9):
                top_grid.SetBinContent(1,b,top_grid.GetBinContent(1,b)+1)
        elif hit_map[pixel_index][0] == 1 or hit_map[pixel_index][1] == 1:
            for b in range(1,9):
                top_grid.SetBinContent(2,b,top_grid.GetBinContent(2,b)+1)
        elif hit_map[pixel_index][0] == 2 or hit_map[pixel_index][1] == 2:
            for b in range(1,9):
                top_grid.SetBinContent(3,b,top_grid.GetBinContent(3,b)+1)
        elif hit_map[pixel_index][0] == 3 or hit_map[pixel_index][1] == 3:
            for b in range(1,9):
                top_grid.SetBinContent(4,b,top_grid.GetBinContent(4,b)+1)
        elif hit_map[pixel_index][0] == 4 or hit_map[pixel_index][1] == 4:
            for b in range(1,9):
                top_grid.SetBinContent(5,b,top_grid.GetBinContent(5,b)+1)
        elif hit_map[pixel_index][0] == 5 or hit_map[pixel_index][1] == 5:
            for b in range(1,9):
                top_grid.SetBinContent(6,b,top_grid.GetBinContent(6,b)+1)
        elif hit_map[pixel_index][0] == 6 or hit_map[pixel_index][1] == 6:
            for b in range(1,9):
                top_grid.SetBinContent(7,b,top_grid.GetBinContent(7,b)+1)
        elif hit_map[pixel_index][0] == 7 or hit_map[pixel_index][1] == 7:
            for b in range(1,9):
                top_grid.SetBinContent(8,b,top_grid.GetBinContent(8,b)+1)
        elif hit_map[pixel_index][0] == 8 or hit_map[pixel_index][1] == 8:
            for b in range(1,9):
                top_grid.SetBinContent(b,1,top_grid.GetBinContent(b,1)+1)
        elif hit_map[pixel_index][0] == 9 or hit_map[pixel_index][1] == 9:
            for b in range(1,9):
                top_grid.SetBinContent(b,2,top_grid.GetBinContent(b,2)+1)
        elif hit_map[pixel_index][0] == 10 or hit_map[pixel_index][1] == 10:
            for b in range(1,9):
                top_grid.SetBinContent(b,3,top_grid.GetBinContent(b,3)+1)
        elif hit_map[pixel_index][0] == 11 or hit_map[pixel_index][1] == 11:
            for b in range(1,9):
                top_grid.SetBinContent(b,4,top_grid.GetBinContent(b,4)+1)
        elif hit_map[pixel_index][0] == 12 or hit_map[pixel_index][1] == 12:
            for b in range(1,9):
                top_grid.SetBinContent(b,5,top_grid.GetBinContent(b,5)+1)
        elif hit_map[pixel_index][0] == 13 or hit_map[pixel_index][1] == 13:
            for b in range(1,9):
                top_grid.SetBinContent(b,6,top_grid.GetBinContent(b,6)+1)
        elif hit_map[pixel_index][0] == 14 or hit_map[pixel_index][1] == 14:
            for b in range(1,9):
                top_grid.SetBinContent(b,7,top_grid.GetBinContent(b,7)+1)
        elif hit_map[pixel_index][0] == 15 or hit_map[pixel_index][1] == 15:
            for b in range(1,9):
                top_grid.SetBinContent(b,8,top_grid.GetBinContent(b,8)+1)

        if hit_map[pixel_index][0] == 16 or hit_map[pixel_index][1] == 16:
            for b in range(1,9):
                bot_grid.SetBinContent(1,b,bot_grid.GetBinContent(1,b)+1)
        elif hit_map[pixel_index][0] == 17 or hit_map[pixel_index][1] == 17:
            for b in range(1,9):
                bot_grid.SetBinContent(2,b,bot_grid.GetBinContent(2,b)+1)
        elif hit_map[pixel_index][0] == 18 or hit_map[pixel_index][1] == 18:
            for b in range(1,9):
                bot_grid.SetBinContent(3,b,bot_grid.GetBinContent(3,b)+1)
        elif hit_map[pixel_index][0] == 19 or hit_map[pixel_index][1] == 19:
            for b in range(1,9):
                bot_grid.SetBinContent(4,b,bot_grid.GetBinContent(4,b)+1)
        elif hit_map[pixel_index][0] == 20 or hit_map[pixel_index][1] == 20:
            for b in range(1,9):
                bot_grid.SetBinContent(5,b,bot_grid.GetBinContent(5,b)+1)
        elif hit_map[pixel_index][0] == 21 or hit_map[pixel_index][1] == 21:
            for b in range(1,9):
                bot_grid.SetBinContent(6,b,bot_grid.GetBinContent(6,b)+1)
        elif hit_map[pixel_index][0] == 22 or hit_map[pixel_index][1] == 22:
            for b in range(1,9):
                bot_grid.SetBinContent(7,b,bot_grid.GetBinContent(7,b)+1)
        elif hit_map[pixel_index][0] == 23 or hit_map[pixel_index][1] == 23:
            for b in range(1,9):
                bot_grid.SetBinContent(8,b,bot_grid.GetBinContent(8,b)+1)
        elif hit_map[pixel_index][0] == 24 or hit_map[pixel_index][1] == 24:
            for b in range(1,9):
                bot_grid.SetBinContent(b,1,bot_grid.GetBinContent(b,1)+1)
        elif hit_map[pixel_index][0] == 25 or hit_map[pixel_index][1] == 25:
            for b in range(1,9):
                bot_grid.SetBinContent(b,2,bot_grid.GetBinContent(b,2)+1)
        elif hit_map[pixel_index][0] == 26 or hit_map[pixel_index][1] == 26:
            for b in range(1,9):
                bot_grid.SetBinContent(b,3,bot_grid.GetBinContent(b,3)+1)
        elif hit_map[pixel_index][0] == 27 or hit_map[pixel_index][1] == 27:
            for b in range(1,9):
                bot_grid.SetBinContent(b,4,bot_grid.GetBinContent(b,4)+1)
        elif hit_map[pixel_index][0] == 28 or hit_map[pixel_index][1] == 28:
            for b in range(1,9):
                bot_grid.SetBinContent(b,5,bot_grid.GetBinContent(b,5)+1)
        elif hit_map[pixel_index][0] == 29 or hit_map[pixel_index][1] == 29:
            for b in range(1,9):
                bot_grid.SetBinContent(b,6,bot_grid.GetBinContent(b,6)+1)
        elif hit_map[pixel_index][0] == 30 or hit_map[pixel_index][1] == 30:
            for b in range(1,9):
                bot_grid.SetBinContent(b,7,bot_grid.GetBinContent(b,7)+1)
        elif hit_map[pixel_index][0] == 31 or hit_map[pixel_index][1] == 31:
            for b in range(1,9):
                bot_grid.SetBinContent(b,8,bot_grid.GetBinContent(b,8)+1)
        
        if hit_map[pixel_index][0] < 0 or hit_map[pixel_index][1] < 0:
            print 'Something went way wrong.'
        if hit_map[pixel_index][0] > 31 or hit_map[pixel_index][1] > 31:
            print 'Something went way wrong.'


    grid_list = [top_grid,bot_grid]
    for grid in grid_list:
        grid.GetXaxis().CenterTitle()
        grid.GetXaxis().SetTitleOffset(2.85)
        grid.GetYaxis().CenterTitle()
        grid.GetYaxis().SetTitleOffset(2.40)
        grid.GetXaxis().SetLabelFont(63)
        grid.GetYaxis().SetLabelFont(63)
        grid.GetXaxis().SetTitleFont(63)
        grid.GetYaxis().SetTitleFont(63)
        grid.GetXaxis().SetLabelSize(18)
        grid.GetYaxis().SetLabelSize(18)
        grid.GetXaxis().SetTitleSize(18)
        grid.GetYaxis().SetTitleSize(18)
        grid.GetZaxis().SetLabelFont(63)
        grid.GetZaxis().SetLabelSize(18)
    ct = TCanvas('ct','ct',0,0,650,1100)
    ct.Divide(1,2)
    ct.cd(1)
    top_grid.Draw('colz')
    ct.SetGridx()
    ct.SetGridy()
    ct.Update()
    ct.Modified()
    ct.cd(2)
    bot_grid.Draw('colz')
    ct.SetGridx()
    ct.SetGridy()
    ct.Update()
    ct.Modified()
    raw_input('')
