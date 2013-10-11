from ROOT import gStyle, TH2D

def style() :
    gStyle.SetOptStat(0)
    gStyle.SetTitleOffset(1.225,"x")
    #gStyle.SetTitleOffset(1.4,"y")
    gStyle.SetTitleOffset(1.1,"y")
    gStyle.SetLabelOffset(.012,"x")
    gStyle.SetLabelOffset(.012,"y")
    gStyle.SetPadTopMargin(0.08)
    gStyle.SetPadBottomMargin(0.12)
    gStyle.SetPadLeftMargin(0.1)
    gStyle.SetPadRightMargin(0.1)
    gStyle.SetFrameLineWidth(2)
    gStyle.SetLabelSize(25,"xyz")
    gStyle.SetLabelFont(63,"xyz")
    gStyle.SetTitleSize(25,"xyz")
    gStyle.SetTitleFont(63,"xyz")
    gStyle.SetHistLineWidth(2)
    
def fix_plot(plot) :
    plot.GetXaxis().SetRangeUser(0,4)
    plot.GetYaxis().SetRangeUser(0,4)
    plot.GetXaxis().CenterTitle()
    plot.GetYaxis().CenterTitle()
    plot.GetXaxis().SetNdivisions(4)
    plot.GetYaxis().SetNdivisions(4)
