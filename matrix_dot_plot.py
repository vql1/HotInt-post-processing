# matrix dot plot
# $Id: matrix_dot_plot.py,v 1.9 2018/05/04 22:12:17 vql Exp vql $

import numpy as np
import matplotlib.pyplot as plt
#
# open input file containing a matrix, using command open
# inputfile = open("C:/Users/vql/Documents/HOTINT simulations/clamped-clamped beam GEO-EX/matrix.txt")
# inputfile = open("C:/Users/vql/Documents/HOTINT simulations/clamped-clamped beam GEO-EX/snap-map.txt")
inputfile = open('snap-map.txt')

# load matrix m as text from input file, using command loadtxt of numpy
m = np.loadtxt(inputfile)
# print matrix m and coefficient [0,0] to verify
# print(m)
# print(m[0,0])

# extract (1st) column 0 as x array
x = m[:,0]
# print(x)

# extract (2nd) column 1 as y array
y = m[:,1]
# print(y)

# extract (3rd) column 2 as cycle array
cycle = m[:,2]
# print(cycle)
cycle_max = np.amax(m[:,2])
cycle_min = np.amin(m[:,2])
print("cycle_max= ", cycle_max, " cycle_min= ", cycle_min)

# set array areas containing the area (size) of the circular dots, inversely proportional to the cycle number
areas = np.pi * (20 / cycle)**2

# set colors for the dots
# array “colors” is of the same dimension as array “cycle”, but with values between 0 and 1 for color map
# np.amax finds the maximum of an array
# colors = cycle / np.amax(cycle)
# colors = 10 * (cycle - cycle_min) / (cycle_max - cycle_min)
# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
# colors = [0,1,2,3,4,5,6,7,8,9]
colors = [None] * len(cycle)
print("length of array colors", len(colors))
for i in range(len(colors)):
    # print("cycle[i]= ", cycle[i])
    if cycle[i] == 1.0:
        colors[i] = 'b'
    elif cycle[i] == 2.0:
        colors[i] = 'g'
    elif cycle[i] == 3.0:
        colors[i] = 'r'
    elif cycle[i] == 4.0:
        colors[i] = 'c'
    elif cycle[i] == 5.0:
        colors[i] = 'm'
    elif cycle[i] == 6.0:
        colors[i] = 'y'
    elif cycle[i] == 7.0:
        colors[i] = '#1f77b4'
    else:
        colors[i] = 'k'
# print("array colors")
# print(colors)

# do scatter plot of matrix m
# set figure size to be 10 in x 40 in
plt.figure(figsize=(10,40))
# plt.scatter(x, y, s=areas, c=colors)
plt.scatter(x, y, s=areas, c=colors)

# show plot
plt.show()

# inquire for submatrix plot
submatrix_plot = input("want submatrix plot ? (y or any) = ")
print("your answer is ", submatrix_plot)

# continue to do submatrix plot if answer is yes
while submatrix_plot == 'y':

    # fa max
    fa_max = np.amax(y)
    print("max fa = ", fa_max)
    # fa min
    fa_min = np.amin(y)
    print("min fa = ", fa_min)

    # input min and max values for np1 for submatrix plot
    np1_min_s = int(input("input np1_min_s to plot = "))
    print("np1_min = ", str(np1_min_s))
    np1_max_s = int(input("input np1_max_s to plot = "))
    print("np1_max = ", str(np1_max_s))

    # input min and max values for fa for submatrix plot
    fa_min_s = int(input("input fa_min_s to plot = "))
    print("fa_min_s = ", str(fa_min_s))
    fa_max_s = int(input("input fa_max_s to plot = "))
    print("fa_max_s = ", str(fa_max_s))

    # input figure size for submatrix plot
    # x size
    fig_size_x = input("input figure size in x direction = ")
    if fig_size_x == '':
        # if answer is empty (CR), use the default x size 10
        fig_size_x = 10
    else:
        fig_size_x = int(fig_size_x)
    print("fig_size_x = ", str(fig_size_x))
    
    # y size
    fig_size_y = input("input figure size in y direction = ")
    if fig_size_y == '':
        # if answer is empty (CR), use the default y size 10
        fig_size_y = 10    
    else:
        fig_size_y = int(fig_size_y)   
    print("fig_size_y = ", str(fig_size_y))
    

    # list xs for submatrix plot
    x_s = []
    # list ys for submatrix plot
    y_s = []
    # list cycle_s for submatrix plot
    cycle_s = []
    # list colors_s for submatrix plot
    colors_s = []

    # loop over the rows of array x
    for j in range(int(len(x))):
    
        # print("row j of x() = ", j, " x(j) = ", x[j])
        if (x[j] >= np1_min_s and x[j] <= np1_max_s) and (y[j] >= fa_min_s and y[j] <= fa_max_s):
        
            # print("x, y = ", x[j], y[j])
        
            x_s.append(x[j])
            y_s.append(y[j])
            cycle_s.append(float(cycle[j]))
            colors_s.append(colors[j])
        

    # print("============================")
    # print("x_s = ", x_s)
    # print("y_s = ", y_s)
    # print("cycle_s = ", cycle_s)
    # print("colors_s = ", colors_s)

    # areas of dots for submatrix
    # convert python list cycle_s to Numpy array cycle_s before performing numerical operations
    # http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html
    tmp = np.array(cycle_s)
    areas_s = np.pi * (20.0 / tmp)**2
        
    # plot subplot
    # set figure size to be 5 in x 5 in
    plt.figure(figsize=(fig_size_x, fig_size_y))
    plt.scatter(x_s, y_s, s=areas_s, c=colors_s)
    plt.scatter(x_s, y_s, c=colors_s)
        
    # show plot
    plt.show()
    
    # inquire for submatrix plot
    submatrix_plot = input("want submatrix plot ? (y or any) = ")
    print("your answer is ", submatrix_plot)

# explicitly close the inputfile
# https://docs.python.org/3/tutorial/inputoutput.html
inputfile.close()


    
