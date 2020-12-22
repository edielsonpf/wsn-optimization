# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Path loss models."""

from abc import ABCMeta, abstractmethod
from random import gauss
import math


class BaseLink(metaclass=ABCMeta):
    """Base class for path loss models."""
    
    def __init__(self):
        pass
    

    def _free_space(self, distance, frequency):
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

    
class FreeSpaceLink(BaseLink):
    """Base class for path loss models."""
    
    def __init__(self):
        super(FreeSpaceLink, self).__init__()
    
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
        return self._free_space(frequency, distance)



class LogNormalLink(BaseLink):
    """Base class for path loss models."""
    
    def __init__(self, sigma = 8.7):
        
        self.sigma = sigma
        super(LogNormalLink, self).__init__()
        
    def loss(self, distance, frequency):
        """
        Calculate the link loss.
        For distance and frequency in kilometers and megahertz, respectively. 
        
        The log-normal path-loss model may be considered as a generalization of the free-space Friis equation
        where a random variable is added in order to account for shadowing (large–scale fading) effects.
        See:    https://www.sciencedirect.com/topics/computer-science/path-loss-model
                https://en.wikipedia.org/wiki/Log-distance_path_loss_model

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
        return self._free_space(distance, frequency) + gauss(0, self.sigma)

    