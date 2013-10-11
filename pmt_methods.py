from ROOT import TPaveText, TH2D

def pmt_hist(values,face):
    peemt = TH2D("pmt","pmt",4,0,4,4,0,4)
    peemt.SetTitle(";;")
    for value in values :
        peemt.SetBinContent(face[value][0]+1,face[value][1]+1,peemt.GetBinContent(face[value][0]+1,face[value][1]+1)+1)
    return peemt

def pmtface() :
    face=[]
    for y in reversed(xrange(4)) :
        for x in xrange(4) :
            l=[]
            l.append(x)
            l.append(y)
            face.append(l)
    return face                

def tpaver(sayit,x,y):
    offset = 0.2
    tpt    = TPaveText(0.18+(x-1)*offset,0.8-(y-1)*offset,0.23+(x-1)*offset,0.85-(y-1)*offset,"brNDC")
    tpt.SetTextSize(25)
    tpt.SetTextFont(63)
    tpt.AddText(sayit)
    tpt.SetBorderSize(0)
    tpt.SetFillColor(0)
    tpt.SetFillStyle(0)
    return tpt

def pmttitle(sayit) :
   pt=TPaveText(0.1135057,0.9409283,0.2816092,0.9831224,"brNDC");
   pt.SetBorderSize(0)
   pt.SetFillColor(0)
   pt.SetFillStyle(0)
   pt.SetTextFont(63)
   pt.SetTextSize(27)
   pt.AddText(sayit);
   return pt
