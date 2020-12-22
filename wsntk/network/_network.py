# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor networks simulation."""

from wsntk.network import SensorNode
from wsntk.network import FreeSpaceLink, LogNormalLink

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
          
          *sigma*
            Double, standard deviation applied to specific path loss models

          *radio*
            String, the radio type usd on all sensors
    """

    link_models = {
        "FSPL": (FreeSpaceLink,),
        "LNPL": (LogNormalLink,),
    }

    def __init__(self, nr_nodes, dimensions, loss = "FSPL", sigma = 8.7, radio = "DEFAULT"):
        
        self.nr_nodes = nr_nodes
        self.dimensions = dimensions
        self.radio = radio
        self.sigma = sigma
        
        self.link = self._init_link(loss)
        self.nodes = self._init_nodes(nr_nodes, dimensions, radio)
            
    def _init_link(self, loss):
        """Get ``LinkClass`` object for str ``loss``. """
        try:
            link_ = self.link_models[loss]
            link_class, args = link_[0], link_[1:]
            if loss in ('LNPL'):
                args = (self.sigma,)
            return link_class(*args)
        except KeyError as e:
            raise ValueError("The link loss %s is not supported. " % loss) from e


    def _init_nodes(self, nr_nodes, dimensions, radio):
        """Initializes the simulaiton creating all nodes with respective configuration. """                
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

    def _distance(self, pos_a, pos_b):
        """Calculate the euclidean distance between two positions"""
        return (math.sqrt(((pos_a[0]-pos_b[0])**2)+((pos_a[1]-pos_b[1])**2)))
    
    def __iter__(self):
        """Generator which returns the current links and nodes after update."""
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

          *sigma*
            Double, standard deviation applied to specific path loss models
          
          *radio*
            String, the radio type usd on all sensors
    """
    def __init__(self, nr_nodes, dimensions, loss = "FSPL", sigma = 8.7, radio = "DEFAULT"):
        
        super(SensorNetwork, self).__init__(nr_nodes, dimensions, loss, sigma, radio)
       
    
    def _update_nodes(self):
        nodes_position = np.empty((0, len(self.dimensions)))
        for node in self.nodes:
            node_iterator = iter(node)
            position = next(node_iterator)
            nodes_position = np.append(nodes_position, position.reshape(1,len(self.dimensions)), axis = 0)
        return nodes_position
 
    def _link_status(self, rx_node, tx_node):
        
        if rx_node != tx_node:
            distance = self._distance(rx_node.get_position(), tx_node.get_position())
            loss = self.link.loss(distance, rx_node.frequency)
            rx_power = tx_node.tx_power - loss
        
            if(rx_power >= rx_node.rx_sensitivity):
                link_status = 1
            else:
                link_status = 0
        else:
            link_status = 0

        return link_status

    def _update_links(self):
        links = []
        for rx_node in self.nodes:
            aux_links = []
            for tx_node in self.nodes:
                    aux_links.append(self._link_status(rx_node, tx_node))
            links.append(aux_links)    

        return links
    
