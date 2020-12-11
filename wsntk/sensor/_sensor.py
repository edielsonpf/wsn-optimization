# Authors: Edielson P. Frigieri <edielsonpf@gmail.com> (main author)
#
# License: MIT

"""Sensor nodes for wirelesss sensor networks simulation."""

from abc import ABCMeta, abstractmethod

#SENSOR_NODE_TYPES = {"ESP32-WROOM-32U": {"min_tx_power": -12.0, "max_tx_power": 9.0, "rx_sensitivity": -97.0}}

class BaseNode(metaclass=ABCMeta):
    """Base class for sensor nodes."""
    def __init__(self, position):
        self.position = position

    def set_position(self, position):
        self.position = position    
        
    def get_position(self):
        return self.position


class SensorNode(BaseNode):

    """Base class for sensor nodes."""
    def __init__(self, position = (0.0, 0.0), tx_power = 5.0, min_tx_power = -12.0, max_tx_power = 9.0, rx_sensitivity = -97.0):
         super().__init__(position)
         self.tx_power = tx_power
         self.min_tx_power = min_tx_power
         self.max_tx_power = max_tx_power
         self.rx_sensitivity = rx_sensitivity 
         
    def set_txpower(self, tx_power):
        """Set radio transmission power
        Parameters
        ----------
        tx_power : {float}
            Transmission power to be configured in the radio
        
        Returns
        -------
        No data returned
        """
        
        if((tx_power >= self.min_tx_power) and (tx_power <= self.max_tx_power)):
            self.tx_power = tx_power    
        else:
            raise ValueError("Parameter out of radio power specification. Expected value from %s dBm to %s dBm." %(self.min_tx_power, self.max_tx_power))
                        

    def get_txpower(self):
        """Get radio transmission power
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current configured transmission power
        """
        return self.tx_power

