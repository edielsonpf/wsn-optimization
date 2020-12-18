# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor networks simulation."""

from abc import ABCMeta, abstractmethod
import math

LINK_STATUS_TYPE = {"down": 0, "up": 1}

class BaseLink(metaclass=ABCMeta):
    """Base class for network links between nodes."""
    
    def __init__(self, distance, tx_power, rx_sensitivity, frequency):
        
        self.frequency = frequency
        self.tx_power = tx_power
        self.rx_sensitivity = rx_sensitivity
        self.distance = distance
        
        self.link_status = self._update_status()

    @abstractmethod
    def _calc_loss(self, distance, frequency):
        """calculate the link loss"""
        raise NotImplementedError
    
    @abstractmethod
    def _update_status(self):
        """Upddate the link status"""
        raise NotImplementedError

    def get_distance(self):
        """Get link diatance
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current distance between src and dst nodes
        """
        return self.distance

    def set_distance(self, distance):
        """Set link distance
        Parameters
        ----------
        float number
            The new distance 
        
        Returns
        -------
        No return
        """
        self.distance = distance
        self.link_status = self._update_status()        

    def get_txpower(self):
        """Get link diatance
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current transmission power
        """
        return self.distance

    def set_txpower(self, tx_power):
        """Set link distance
        Parameters
        ----------
        float number
            The transmission power 
        
        Returns
        -------
        No return
        """
        self.tx_power = tx_power
        self.link_status = self._update_status()        

    def get_status(self):
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

class FreeSpaceRadioLink(BaseLink):
    """Network links between sensor nodes."""
    def __init__(self, distance, tx_power, rx_sensitivity, frequency):
    
        super(FreeSpaceRadioLink, self).__init__(distance, tx_power, rx_sensitivity, frequency)
          
    def _calc_loss(self, distance, frequency):
        """calculate the link loss"""
        """For  distance and freqeuncy in kilometers and megahertz, respectively, the constant becomes 32.44"""
        return (32.44 + 20*math.log10(frequency/1e6) + 20*math.log10(distance))
    
    def _update_status(self):
        
        loss = self._calc_loss(self.distance, self.frequency)
        print(loss)
        rx_power = self.tx_power - loss
        print(rx_power)
        if(rx_power >= self.rx_sensitivity):
            link_status = self._get_status_type("up")
        else:
            link_status = self._get_status_type("down")
        
        return link_status

    def _get_status_type(self, link_status):
        link_status = str(link_status).lower()
        try:
            return LINK_STATUS_TYPE[link_status]
        except KeyError as e:
            raise ValueError("Status %s is not supported." % link_status) from e
    
    