# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor networks simulation."""

import math
from abc import ABCMeta, abstractmethod

LINK_STATUS_TYPE = {"disconnected": 0, "connected": 1}

class BaseLink(metaclass=ABCMeta):
    """Base class for network links between nodes."""
    
    def __init__(self, src_position, dst_position, threshold = 1.0):
        
        self.threshold = threshold
        self.src_position = src_position
        self.dst_positon = dst_position
        self.link_distance, self.link_status = self._get_link(src_position, dst_position, threshold)
    
    def _get_link_status_type(self, link_status):
        link_status = str(link_status).lower()
        try:
            return LINK_STATUS_TYPE[link_status]
        except KeyError as e:
            raise ValueError("Status %s is not supported." % link_status) from e

    def _calc_dist(self,pos_a,pos_b):
        return (math.sqrt(((pos_a[0]-pos_b[0])**2)+((pos_a[1]-pos_b[1])**2)))

    def _get_link(self, src_position, dst_position, threshold):
        
        distance = self._calc_dist(src_position, dst_position)

        if(distance <= threshold):
            link_status = self._get_link_status_type("connected")
        else:
            link_status = self._get_link_status_type("disconnected")
        
        return distance, link_status

    def get_link_distance(self):
        """Get link diatance
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current distance between src and dst nodes
        """
        return self.link_distance

    def get_link_status(self):
        """Get current link status based on defined threshold
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current configured transmission power
        """
        return self.link_status

    def set_link_threshold(self, threshold):
        """Get current link status based on defined threshold
        Parameters
        ----------
        float number
            The new link threshold
        Returns
        -------
        No return    
        """
        self.threshold = threshold
        self.link_distance, self.link_status = self._get_link(src_position, dst_position, threshold)

        return self.link_status

class RadioLink(BaseLink):
    """Network links between sensor nodes."""
    
    def __init__(self, src_position, dst_position, threshold = 1.0):
    
        super(RadioLink, self).__init__(src_position, dst_position, threshold)
          
    
