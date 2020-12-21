# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Path loss models."""

from abc import ABCMeta, abstractmethod
import math

class BaseLink(metaclass=ABCMeta):
    """Base class for path loss models."""
    
    def __init__(self):
        pass

    @abstractmethod
    def loss(self, distance, frequency):
        """
        evaluate the loss function
        
        Parameters
        ----------
        distance : double
           The distance between two nodes.
        
        frequency: double
            The frequency of operation  
        
        Returns
        -------
        double
            The loss evaluated for `distance` and `frequency`.
        """
        raise NotImplementedError

    @abstractmethod
    def distance(self, src_position, dst_position):
        """
        calculate the diatance between two coordinates
        
        Parameters
        ----------
        src_position : tuple of double
           The position of the source node.
        
        dst_position : tuple of double
           The position of the destination node.
        
        Returns
        -------
        double
            The diatance between the two nodes.
        """
        raise NotImplementedError


class FreeSpaceLink(BaseLink):
    """Base class for path loss models."""
    
    def __init__(self):
        super(FreeSpaceLink, self).__init__()
        pass

    def loss(self, distance, frequency):
        """
        Calculate the link loss.
        For distance and frequency in kilometers and megahertz, respectively, 
        the constant becomes 32.44
        
        Parameters
        ----------
        distance : double
           The distance between two nodes (Km).
        
        frequency: double
            The frequency of operation (MHz).  
        
        Returns
        -------
        double
            The loss evaluated for `distance` and `frequency`.
        """
        return (32.44 + 20*math.log10(frequency/1e6) + 20*math.log10(distance))

    def distance(self, pos_a, pos_b):
        """Calculate the euclidean distance between two positions"""
        return (math.sqrt(((pos_a[0]-pos_b[0])**2)+((pos_a[1]-pos_b[1])**2)))