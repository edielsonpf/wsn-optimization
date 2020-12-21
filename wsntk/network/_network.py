# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor networks simulation."""

from wsntk.network import SensorNode
from wsntk.network import FreeSpaceLink

from abc import ABCMeta, abstractmethod

from numpy.random import rand
import math
import numpy as np

class BaseNetwork(metaclass=ABCMeta):
    """
        Sensor network class.
        This class is implments a sensor network which involves elemts such as sensors and links.
        
        Required arguments:
        
          *nr_nodes*:
            Integer, the number of nodes.
          
          *dimensions*:
            Tuple of Integers, the x and y dimensions of the simulation area in kilometers.

          *loss function*
            String, the path loss function
          
          *radio*
            String, the radio type usd on all sensors
    """

    link_models = {
        "FSPL": (FreeSpaceLink,),
    }

    def __init__(self, nr_nodes, dimensions, loss = "FSPL", radio = "DEFAULT"):
        
        self.nr_nodes = nr_nodes
        self.dimensions = dimensions
        self.radio = radio
        
        self.link = self._get_link(loss)
        self.nodes = self._init_nodes(nr_nodes, dimensions, radio)
            
    def _get_link(self, loss):
        """Get ``LinkClass`` object for str ``loss``. """
        try:
            link_ = self.link_models[loss]
            link_class, args = link_[0], link_[1:]
            return link_class(*args)
        except KeyError as e:
            raise ValueError("The link loss %s is not supported. " % loss) from e


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

    def __iter__(self):
        while True:
            
            nodes = self._update_nodes()
            links = self._update_links()
            yield nodes, links

    @abstractmethod
    def _update_nodes(self):
        """Update the nodes status: position, energy, etc."""
        raise NotImplementedError
    
    @abstractmethod
    def _update_links(self):
        """Update the links status based on the new nodes status."""
        raise NotImplementedError
       
    
class SensorNetwork(BaseNetwork):
    """
        Sensor network class.
        This class is implments a sensor network which involves elemts such as sensors and links.
        
        Required arguments:
        
          *nr_nodes*:
            Integer, the number of nodes.
          
          *dimensions*:
            Tuple of Integers, the x and y dimensions of the simulation area in kilometers.

          *loss function*
            String, the path loss function
          
          *radio*
            String, the radio type usd on all sensors
    """
    def __init__(self, nr_nodes, dimensions, loss = "FSPL", radio = "DEFAULT"):
        
        super(SensorNetwork, self).__init__(nr_nodes, dimensions, loss, radio)
       
    
    def _update_nodes(self):
        nodes_position = np.empty((0, len(self.dimensions)))
        for node in self.nodes:
            node_iterator = iter(node)
            position = next(node_iterator)
            nodes_position = np.append(nodes_position, position.reshape(1,len(self.dimensions)), axis = 0)
        return nodes_position
 
    def _link_status(self, src_node, dst_node):
        
        if src_node != dst_node:
            distance = self.link.distance(src_node.get_position(), dst_node.get_position())
            loss = self.link.loss(distance, dst_node.frequency)
            rx_power = src_node.tx_power - loss
        
            if(rx_power >= dst_node.rx_sensitivity):
                link_status = 1
            else:
                link_status = 0
        else:
            link_status = 0

        return link_status

    def _update_links(self):
        links = []
        for src_node in self.nodes:
            aux_links = []
            for dst_node in self.nodes:
                    aux_links.append(self._link_status(src_node, dst_node))
            links.append(aux_links)    

        return links
    