# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor networks simulation."""

from wsntk.network import SensorNode
from wsntk.network import FreeSpaceRadioLink

from abc import ABCMeta, abstractmethod

from numpy.random import rand
import math
import numpy as np

LINK_STATUS = {"down": 0, "up": 1}

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
    def __init__(self, nr_nodes, dimensions, radio = "DEFAULT"):
        
        self.nr_nodes = nr_nodes
        self.dimensions = dimensions
        self.radio = radio
        
        self.nodes = self._init_nodes(nr_nodes, dimensions, radio)
            
    def _init_nodes(self, nr_nodes, dimensions, radio):
                
        ndim = len(dimensions)
        nodes = []
        
        #instantiate all nodes
        for i in range (nr_nodes):
            #create initial randon position
            position = rand(ndim) * dimensions
            #instantiate a node
            node = SensorNode(position, radio)
            #Add node to the network
            nodes.append(node)
        
        return nodes

    def _get_link_status_type(self, link_status):
        link_status = str(link_status).lower()
        try:
            return LINK_STATUS[link_status]
        except KeyError as e:
            raise ValueError("Status %s is not supported." % link_status) from e

    @abstractmethod
    def _link_status(self, src_node, dst_node):
        """returns the link status between two nodes"""
        raise NotImplementedError

    @abstractmethod
    def _calc_loss(self, distance, frequency):
        """calculate the link loss"""
        raise NotImplementedError

    @abstractmethod
    def _calc_dist(self, pos_a, pos_b):
        """Calculate the distance between two positions"""
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        """Interator"""
        raise NotImplementedError

           
    
class FreeSpaceSensorNetwork(SensorNetwork):
    """
        Sensor network class.
        This class is implments a sensor network which involves elemts such as sensors and links.
        
        Required arguments:
        
          *nr_nodes*:
            Integer, the number of nodes.
          
          *dimensions*:
            Tuple of Integers, the x and y dimensions of the simulation area in kilometers.
    """
    def __init__(self, nr_nodes, dimensions, radio = "DEFAULT"):
        
        super(FreeSpaceSensorNetwork, self).__init__(nr_nodes, dimensions, radio)
       
    def _calc_loss(self, distance, frequency):
        """
            Calculate the link loss.
            For distance and freqeuncy in kilometers and megahertz, respectively, 
            the constant becomes 32.44
        """
        return (32.44 + 20*math.log10(frequency/1e6) + 20*math.log10(distance))

    def _calc_dist(self, pos_a, pos_b):
        """Calculate the euclidean distance between two positions"""
        return (math.sqrt(((pos_a[0]-pos_b[0])**2)+((pos_a[1]-pos_b[1])**2)))

    def _link_status(self, src_node, dst_node):
        
        if src_node != dst_node:
            distance = self._calc_dist(src_node.get_position(), dst_node.get_position())
            loss = self._calc_loss(distance, dst_node.frequency)
            rx_power = src_node.tx_power - loss
        
            if(rx_power >= dst_node.rx_sensitivity):
                link_status = self._get_link_status_type("up")
            else:
                link_status = self._get_link_status_type("down")
        else:
            link_status = self._get_link_status_type("down")

        return link_status

    
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
        nodes_position = np.empty((0, len(self.dimensions)))
        for node in self.nodes:
            node_iterator = iter(node)
            position = next(node_iterator)
            nodes_position = np.append(nodes_position, position.reshape(1,len(self.dimensions)), axis = 0)
        return nodes_position
 
    def _update_links(self):
        links = []
        for src_node in self.nodes:
            aux_links = []
            for dst_node in self.nodes:
                    aux_links.append(self._link_status(src_node, dst_node))
            links.append(aux_links)    

        return links
    
    def __iter__(self):
        while True:
            
            nodes = self._update_nodes()
            links = self._update_links()
        
            yield nodes,links

    
    

