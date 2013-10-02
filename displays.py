#!/usr/bin/env python

import grid
import sys
import pmt

# './display.py filename.root events_number
def main():
    pp        = []
    file_name = sys.argv[1]
    event     = int(sys.argv[2])
    
    #pp.append(Process(target=grid.gridit, args=(file_name,event)))
    #pp.append(Process(target=pmt.pmt_draw, args=(file_name,event)))
    
    #for k in pp :
    #    k.start()
    #for j in pp :
    #    k.join()
    
    grid.gridit(file_name,event)
    pmt.pmt_draw(file_name,event)

if __name__ == '__main__':
    main()
