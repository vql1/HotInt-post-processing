# -*- coding: utf-8 -*-
"""
$Id: read_hotint_output_2.py,v 1.4 2018/05/05 11:55:01 vql Exp vql $
Created on Wed Apr 25 18:09:25 2018

@author: vql
"""

# import module os for operating system interface
# https://docs.python.org/3/library/os.html
import os
# import module re for regular expressions
# https://docs.python.org/3/library/re.html
import re
# import module fnmatch for Unix filename pattern matching
# https://docs.python.org/3/library/fnmatch.html
import fnmatch
# import module numnp for numerical python
import numpy as np
# import module matplotlib.pyplot for plotting
import matplotlib.pyplot as plt

# open file snap-map.txt to write
# snap = open('snap-map.txt', 'a')
snap = open('junk.txt', 'a')

# input min and max values for np1 to append to file snap
np1_min = int(input("input np1_min to append to snap-map = "))
print("np1_min = ", str(np1_min))
np1_max = int(input("input np1_max to append to snap-map = "))
print("np1_max = ", str(np1_max))

# input min and max values for fa to append to file snap
fa_min = int(input("input fa_min to append to snap-map = "))
print("fa_min = ", str(fa_min))
fa_max = int(input("input fa_max append to snap-map = "))
print("fa_max = ", str(fa_max))

# set beam fundamental oscillation period
period_1 = 4.9436258569

# loop over each file in the directory
# os.listdir('.') = list current directory
for file in os.listdir('.'):
    
    # test whether the current file has pattern "output*.txt"
    if fnmatch.fnmatch(file, 'output*.txt'):
        
        # print output separator
        print("")
        print("================================================")
        
        # print filename
        print(file)
        
        # strip filename to get only the values of np1 and fa
        # substitute "output-np1=" by nothing (remove it)
        s1 = re.sub("output-np1=", '', file)
        # substitute "-fa=" by 4 blank spaces
        s2 = re.sub("-fa=", '    ', s1)
        # substituge "-sensor-outputs.txt" by nothing
        s3 = re.sub("-sensor-outputs.txt", '', s2)
        # print the values of np1 and fa as text string
        print(s3)
        
        # split up variable s3 into array m, using blank space as delimiter
        # m[0]=np1, m[1]=' ', m[2]=' ', m[3]=' ', m[4]=fa
        m = (re.split(' ', s3))
        print('m[0]= ', m[0], ' m[4]= ', m[4])
       
        # convert np1 and fa from text to floating point numbers
        # to compare with their desired min and max values 
        np1 = float(m[0])
        fa  = float(m[4])
        print("np1= ", np1, " fa= ", fa)
        
        # test whether np1 and fa are within the desired range
        if (np1 < np1_min or np1 > np1_max) or (fa < fa_min or fa > fa_max):
            
            # np1 or fa is outside desired range, skip to next output file 
            continue
        
        # load current output "file" into array "data"
        # comments = comment line starts with '%'
        # usecols = use only columns 0, 1, 2, 4
        data = np.loadtxt(file, comments='%', usecols=(0, 1, 2, 4))
                
        # print max and min mid-span transverse disp in (2nd) column 1
        print(np.amax(data[:,1]), np.amin(data[:,1]))

        # test whether there was a snap through, if yes, plot
        # if (max disp + min disp) < max disp / 2, then plot
        # we could use another test closer to the one in the hid file
        disp_min = np.amin(data[:,1])
        print("disp_min = ", disp_min)
        disp_max = np.amax(data[:,1])
        print("disp_max = ", disp_max)
    
        # if np.amax(data[:,1]) + np.amin(data[:,1]) < np.amax(data[:,1]) / 2:
        # if disp_min < 0 and abs(abs(disp_min) - disp_max) < 0.1 * disp_max:
        # need to use the same test as in hid file, otherwise miss some dots
        if disp_min < 0 and abs(abs(disp_min) - 1.7) < 0.1 * 1.7:
    
            # plot midspan displacement versus time
            plt.plot(data[:,0], data[:,1])
            plt.show()
        
            # max time and cycle number
            time_max = np.amax(data[:,0])
            print("time_max= ", time_max)
            
            # cycle number
            cycle_number = int(time_max / (np1 * period_1) + 1)
            print("cycle_number= ", cycle_number)
            
            # write to snap-map.txt
            # text = "m[0] m[4] str(cycle_number)"
            snap.write(m[0] + '    ' + m[4] + '    ' + str(cycle_number) + '\n')
            
snap.close()

