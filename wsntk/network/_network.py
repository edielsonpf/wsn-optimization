# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor networks simulation."""

from abc import ABCMeta, abstractmethod
from wsntk.network import SensorNode
from wsntk.network import FreeSpaceRadioLink

from numpy.random import rand
import math
import numpy as np


class SensorNetwork(metaclass=ABCMeta):
    """
        Sensor network class.
        This class is implments a sensor network which involves elemts such as sensors and links.
        
        Required arguments:
        
          *nr_nodes*:
            Integer, the number of nodes.
          
          *dimensions*:
            Tuple of Integers, the x and y dimensions of the simulation area in kilometers.
    """
    def __init__(self, nr_nodes, dimensions, radio_type = "DEFAULT"):
        
        self.nr_nodes = nr_nodes
        self.dimensions = dimensions
        self.radio_type = radio_type
        
        self.nodes = self._init_simulator(nr_nodes, dimensions, radio_type)
        

    def _calc_dist(self,pos_a,pos_b):
        return (math.sqrt(((pos_a[0]-pos_b[0])**2)+((pos_a[1]-pos_b[1])**2)))

    def _update_links(self):
        links = {}
        for src_node in self.nodes:
            for dst_node in self.nodes:
                if src_node is not dst_node:
                    distance = self._calc_dist(src_node.get_position(), dst_node.get_position())
                    link = FreeSpaceRadioLink(distance, src_node.get_txpower(), dst_node.get_rxsensitivity(), dst_node.get_frequency())
                    links[src_node, dst_node] = link
                    print(distance)
                    print(link.get_status())
        return links

        # transforms the indirect graph in directed one
        #links = []
        #if self.__nxGraph:
        #    self.__nxGraph.clear()
        #else:
        #    self.__nxGraph = nx.Graph()
        
        ## generated a graph with connection between nodes initially unconnected
        #self.__graph = [[self.__unconnected for i in range(self.__numNodes)] for j in range(self.__numNodes)]
        
        #for node_a in self.__nodes:
        #    ValidConnection = False
        #    for node_b in self.__nodes:
        #        if node_a != node_b:
        #            dist = self.__calcEuclidianDist(node_a,node_b)
        #            if round(dist,2) <= round(self.__caldDistance(self.__power[self.__nodes.index(node_a)]),2):
        #                ValidConnection = True
        #                self.__graph[self.__nodes.index(node_a)][self.__nodes.index(node_b)] = dist
        #                self.__nxGraph.add_edge(self.__nodes.index(node_a), self.__nodes.index(node_b), weight = dist) 
        
        #    if ValidConnection == False:
        #        logging.warning('The graph is not connected!\r\n')
        #        self.__graph = []
        #        self.__nxGraph=[]
        #        break

    def _update_nodes(self):
        for node in self.nodes:
            position = node.get_position() + 0.5
            node.set_position(position)
            print(node.get_position())
 
    def _init_simulator(self, nr_nodes, dimensions, radio_type):
                
        ndim = len(dimensions)
        nodes = []
        
        #instantiate all nodes
        for i in range (nr_nodes):
            #instantiate a node
            node = SensorNode(radio = radio_type)
            #create initial randon position
            position = rand(ndim) * np.array(dimensions)
            node.set_position(position)
            nodes.append(node)
        
        return nodes 
    
    def __iter__(self):
        return self

    def __next__(self):
        self._update_nodes()
        self._update_links()
    
    

