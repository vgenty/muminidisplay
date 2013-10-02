import sys
from ROOT import TFile, TTree, TH2I, gStyle, TLatex, TCanvas, gPad
import fibers as f
import grid_methods as gm

def gridit(root_file,user_event):
    gStyle.SetOptStat(0)
    n_extrusions = 32
    top_grid = TH2I('top_grid',
                    ';x [mm] (extrusions 0 #rightarrow 7);y [mm] (extrusions 8 #rightarrow 15)',
                    8,0,250,8,0,250)
    bot_grid = TH2I('bot_grid',
                    ';x [mm] (extrusions 16 #rightarrow 23);y [mm] (extrusions 24 #rightarrow 31)',
                    8,0,250,8,0,250)
    grid_list = [top_grid,bot_grid]
    hit_pixels = f.fiber(root_file,int(user_event))
    mapfile    = open('mapfile.csv')
    hit_map    = f.mapping(mapfile)

    grid_list = gm.fill_grid(grid_list,hit_pixels,hit_map)
                        
    #    grid_list = [top_grid,bot_grid]
    gm.fix_grids(grid_list)

    return grid_list
