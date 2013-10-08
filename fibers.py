from ROOT import TFile, TTree
import csv

def fiber(file_name,user_event) :    
    hits=[]
    if 'root' in file_name:
        thefile = TFile(file_name,'read')
        stat_tree = thefile.Get('theRunTree')
        n_extrusions = 32
        n = 0
        for event in stat_tree:
            if user_event == n:
                for fiber in range(0,n_extrusions - 1):
                    oo = event.FiberID[fiber]
                    if oo > 0 : hits.append(fiber)
            n += 1
        thefile.Close()
        print hits
    else:
        print 'i am based god'
        thefile = open(file_name,'r')
        for line in thefile:
            line=line.rstrip()
            hits.append(int(line))
            
    print hits      
    #i now have the hits
    
    #open file and get mapping
    mapfile = open("mapfile.csv",'r')
    pixels=mapping(mapfile)        
    #i now have the pixels    
    values = map_fibers(hits,pixels)
    mapfile.close()
    return values

def map_fibers(hits,pixels):
    lit_up=[]    
    for hit in hits:
        for pixel in pixels:
            if hit in pixel :
                idx=pixels.index(pixel)
                lit_up.append(idx)
    return lit_up

def mapping(mapfile) :
    reader= csv.reader(mapfile)
    outer=[]
    
    for row in reader:
        inner=[]
        for p in xrange(len(row)):
                if p is not 0: inner.append(int(row[p]))
        outer.append(inner)
        
    return outer

def pmtface() :
    face=[]
    for y in reversed(xrange(4)) :
        for x in xrange(4) :
            l=[]
            l.append(x)
            l.append(y)
            face.append(l)
            
    return face                
