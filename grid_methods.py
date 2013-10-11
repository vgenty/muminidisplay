def fill_grid(hists,hit_pixels,hit_map):
    for pixel_index in hit_pixels:         #Look in hit pixels for associated fibers
        for index in hit_map[pixel_index]: #for each fiber attached to the pixel
            for b in range(1,9):            #filling for dougs histo
                if index <= 7:
                    hists[0].SetBinContent(index+1,b,hists[0].GetBinContent(index+1,b)+1)
                elif index < 16 and index >7:
                    hists[0].SetBinContent(b,index%8+1,hists[0].GetBinContent(b,(index%8)+1)+1)
                if index >=16 and index < 24:
                    hists[1].SetBinContent((index%16)+1,b,hists[1].GetBinContent((index%16)+1,b)+1)
                elif index >=24:
                    hists[1].SetBinContent(b,(index%24)+1,hists[1].GetBinContent(b,(index%24)+1)+1)
    return hists

def fix_grids(glist):
    for grid in glist:
        grid.GetXaxis().CenterTitle()
        grid.GetXaxis().SetTitleOffset(2.85)
        grid.GetYaxis().CenterTitle()
        grid.GetYaxis().SetTitleOffset(2.40)
        grid.GetXaxis().SetLabelFont(63)
        grid.GetYaxis().SetLabelFont(63)
        grid.GetXaxis().SetTitleFont(63)
        grid.GetYaxis().SetTitleFont(63)
        grid.GetXaxis().SetLabelSize(25)
        grid.GetYaxis().SetLabelSize(25)
        grid.GetXaxis().SetTitleSize(25)
        grid.GetYaxis().SetTitleSize(25)
        grid.GetZaxis().SetLabelFont(63)
        grid.GetZaxis().SetLabelSize(25)
