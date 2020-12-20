# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

from wsntk.network import FreeSpaceRadioLink

#from pymobility.models.mobility import gauss_markov, reference_point_group, \
#    tvc, truncated_levy_walk, random_direction, random_waypoint, random_walk
#import numpy as np
#import logging
#from scipy.spatial.distance import cdist

#logging.basicConfig(format='%(asctime)-15s - %(message)s', level=logging.INFO)
#logger = logging.getLogger("simulation")

## set this to true if you want to plot node positions
#DRAW = True

## number of nodes
#nr_nodes = 10

## simulation area (units)
#MAX_X, MAX_Y = 50, 50
#DIM_REF = 50

## set this to true if you want to calculate node contacts
#CALCULATE_CONTACTS = False
## if calculating contacts, this is the range to be used
## (if a distance(a,b) < RANGE, then there is a contact betwen a and b)
#RANGE = 1.

#if DRAW:
#    import matplotlib.pyplot as plt
#    plt.ion()
#    ax = plt.subplot(111)
#    line, = ax.plot(range(MAX_X), range(MAX_X), linestyle='', marker='.')

#    if CALCULATE_CONTACTS:
#        for l in range(DIM_REF):
#            ax.plot([], [], 'b-')
        
#step = 0
#np.random.seed(0xffff)

#for xy in rw:
    
#    step += 1
#    if step%10000==0: logger.info('Step %s'% step)
#    if step < STEPS_TO_IGNORE: continue
    
#    if DRAW:
        
#        if CALCULATE_CONTACTS:
#            lnr = 1
#            # calculate the distance between all points represented in the xy matrix
#            d = cdist(xy,xy)
#            for (i,j) in zip(*np.where(d<RANGE)):
#                    if j > i:
#                        ax.lines[lnr].set_data([xy[i,0],xy[j,0]], [xy[i,1],xy[j,1]])
#                        lnr += 1
#            for i in xrange(lnr, 100):
#                ax.lines[i].set_data([],[])
        
#        line.set_data(xy[:,0],xy[:,1])
#        plt.draw()


link = FreeSpaceRadioLink(src_position = (-10,10), dst_position = (10,-10), threshold = 10)
print(link.get_link_distance())
print(link.get_link_status())

