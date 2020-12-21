# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

from wsntk.simulator import NetSim
import numpy as np
import logging

#from scipy.spatial.distance import cdist

logging.basicConfig(format='%(asctime)-15s - %(message)s', level=logging.INFO)
logger = logging.getLogger("network simulation")

## set this to true if you want to plot node positions
DRAW = True

## number of nodes
nr_nodes = 5

## simulation area (km)
max_x, max_y = 15, 15

np.random.seed(0xffff)

net = NetSim(nr_nodes, dimensions=(max_x, max_y))

if DRAW:
    import matplotlib.pyplot as plt
    plt.ion()
    ax = plt.subplot(111)
    line, = ax.plot(range(max_x), range(max_x), 'C3', zorder=1, lw=3, linestyle='', marker='o')
       
        
step = 0

for nodes,links in net:
    
    step = step+1
    if step%10 == 0: 
        logger.info('Step %s'% step)
        #print(nodes)
        #print(links)
    
    if DRAW:
        for l in range(len(nodes)):
            ax.plot([], [], 'b-')    
            
        i = 0
        lnr = 0
        for node in links:
            for link in node:
                if link == 1:
                    j = node.index(link)
                    ax.lines[lnr].set_data([nodes[i,0],nodes[j,0]], [nodes[i,1],nodes[j,1]])
                    lnr += 1
            i = i + 1

        for l in range(lnr, len(nodes)):
            ax.lines[l].set_data([],[])
        
        line.set_data(nodes[:,0],nodes[:,1])
        
        plt.draw()
        plt.pause(0.5)
