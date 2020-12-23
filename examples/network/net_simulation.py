# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

from wsntk.simulator import SimuNet
import numpy as np
import logging

#from scipy.spatial.distance import cdist

logging.basicConfig(format='%(asctime)-15s - %(message)s', level=logging.INFO)
logger = logging.getLogger("network simulation")

## set this to true if you want to plot node positions
DRAW = True

## number of nodes
nr_nodes = 10

## simulation area (km)
max_x, max_y = 15, 15

np.random.seed(0xffff)

## Free Space path loos-based simulation
#net = SimuNet(nr_nodes, dimensions=(max_x, max_y), loss = "FSPL", sigma = 8.7, gamma = 2.2, radio = "DEFAULT")

## Log-Normal path loos-based simulation
#net = SimuNet(nr_nodes, dimensions=(max_x, max_y), loss = "LNPL", sigma = 8.7, gamma = 2.2, radio = "DEFAULT")

## Log-Normal path loos-based simulation with ESP32-WROOM-32U radio sensors
net = SimuNet(nr_nodes, dimensions=(max_x, max_y), loss = "LNPL", sigma = 8.7, gamma = 2.2, radio = "ESP32-WROOM-32U")


if DRAW:
    import matplotlib.pyplot as plt
    # Create new Figure and an Axes which fills it.
    ax = plt.subplot(111)
    ax.set_xlim(0, max_x)
    ax.set_ylim(0, max_y)

    # Construct the scatter which will be update during simulation 
    scat = ax.scatter([], [], s=60, lw=0.5, zorder=2)
    lines = [ax.plot([],[], 'C3', zorder=1, lw=0.3)[0] for j in range(nr_nodes*nr_nodes)]
        
step = 0
for nodes,links in net:
    
    step = step+1
    if step%10 == 0: 
        logger.info('Step %s'% step)
        #print(nodes)
        print(links)
    
    if DRAW:
        #cleanup all lines
        for line in lines:
            line.set_data([],[])
        
        #update only the lines which represents a valid link
        lnr = 0
        i = 0
        for link_set in links:
            j = 0
            for link in link_set:
                if link == 1:
                    lines[lnr].set_data([nodes[i,0],nodes[j,0]], [nodes[i,1],nodes[j,1]])
                    lnr += 1
                j = j + 1
            i = i + 1

        #update the nodes position
        scat.set_offsets(nodes)
        
        plt.draw()
        plt.pause(0.5)
