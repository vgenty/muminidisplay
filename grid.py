import sys
from ROOT import TFile, TTree, TH2I, gStyle, TLatex, TCanvas, gPad
import fibers as f
import grid_methods as gm
'''
def gridit(root_file,user_event):
    gStyle.SetOptStat(0)
    n_extrusions = 32
    top_grid = TH2I('top_grid',
                    ';x [mm] (0 #rightarrow 7);y [mm] (8 #rightarrow 15)',
                    8,0,250,8,0,250)
    bot_grid = TH2I('bot_grid',
                    ';x [mm] (16 #rightarrow 23);y [mm] (24 #rightarrow 31)',
                    8,0,250,8,0,250)
    grid_list = [top_grid,bot_grid]
    hit_pixels = f.fiber(root_file,int(user_event))
    mapfile    = open('mapfile.csv')
    hit_map    = f.mapping(mapfile)

    grid_list = gm.fill_grid(grid_list,hit_pixels,hit_map)
                        
    gm.fix_grids(grid_list)

    return grid_list
'''
def gridit(root_file,user_event):
    gStyle.SetOptStat(0)
    n_extrusions = 32
    top_grid = TH2I('top_grid',
                    ';x (0 #rightarrow 7);y (8 #rightarrow 15)',
                    8,0,8,8,0,8)
    bot_grid = TH2I('bot_grid',
                    ';x (16 #rightarrow 23);y (24 #rightarrow 31)',
                    8,0,8,8,0,8)
    grid_list = [top_grid,bot_grid]
    hit_pixels = f.fiber(root_file,int(user_event))
    mapfile    = open('mapfile.csv')
    hit_map    = f.mapping(mapfile)

    grid_list = gm.fill_grid(grid_list,hit_pixels,hit_map)
                        
    gm.fix_grids(grid_list)

    return grid_list
