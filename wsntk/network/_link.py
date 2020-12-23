# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Path loss models."""

from abc import ABCMeta, abstractmethod
import numpy as np
import math


class BaseLink(metaclass=ABCMeta):
    """Base class for path loss models."""
    
    def __init__(self):
        pass
    
    def _friss(self, distance, frequency):
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
        return self._friss(frequency, distance)



class LogNormalLink(BaseLink):
    """Base class for path loss models."""
    
    def __init__(self, sigma = 8.7, gamma = 2.2):
        
        self.sigma = sigma
        self.gamma = gamma
        super(LogNormalLink, self).__init__()
        
    def loss(self, distance, frequency):
        """
        Calculate the link loss.
        For distance and frequency in kilometers and megahertz, respectively. 
        
        The log-normal path-loss model may be considered as a generalization of the free-space Friis equation
        where a random variable is added in order to account for shadowing (large–scale fading) effects.
        See:    https://www.sciencedirect.com/topics/computer-science/path-loss-model
                https://en.wikipedia.org/wiki/Log-distance_path_loss_model

                Building Type	            Frequency of Transmission	gamma 	sigma [dB]
                Vacuum, infinite space		                            2.0	    0
                Retail store	            914 MHz	                    2.2	    8.7
                Grocery store	            914 MHz	                    1.8	    5.2
                Office with hard partition	1.5 GHz	                    3.0	    7
                Office with soft partition	900 MHz	                    2.4	    9.6
                Office with soft partition	1.9 GHz	                    2.6	    14.1
                Textile or chemical	        1.3 GHz	                    2.0	    3.0
                Textile or chemical	        4 GHz	                    2.1	    7.0, 9.7
                Office	                    60 GHz	                    2.2	    3.92
                Commercial	                60 GHz	                    1.7	    7.9

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
        return self._friss(distance, frequency) - 10*self.gamma*math.log10(distance) + np.random.normal(0, self.sigma)

    