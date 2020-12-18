# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Sensor nodes for wirelesss sensor networks simulation."""

from abc import ABCMeta, abstractmethod

RADIO_CONFIG = {"DEFAULT":          {"min_tx_power": -15.0, "max_tx_power": 27.0, "rx_sensitivity": -80.0, "frequency": 933.0e6},
                "ESP32-WROOM-32U":  {"min_tx_power": -12.0, "max_tx_power": 9.0, "rx_sensitivity": -97.0, "frequency": 2.4e9}}

class BaseNode(metaclass=ABCMeta):
    """Base class for sensor node."""
    
    def __init__(self, position = (0.0, 0.0)):
        
        self.position = position
                         
    def set_position(self, position):
        """
        Set node position
        
        Parameters
        ----------
        position : tuple of Integers
           The x and y position of the sensor.
        
        Returns
        -------
        No data returned
        """
        
        self.position = position    
        
    def get_position(self):
        """
        Get node position
        
        Parameters
        ----------
        No parameters.
        
        Returns
        -------
        Tuple of Integers
           The current x and y position of the sensor
        """
        return self.position

class SensorNode(BaseNode):
    """
    Sensor node class.
        
    Required arguments:
        
        *position*:
        Tuple of Integers, the x and y position of the sensor.
          
        *radio*:
        Enumerator <RADIO_CONFIG>, the radio type to be used in the sensor.
    """
    def __init__(self, position = (0.0, 0.0), radio = "DEFAULT"):
        
        self._set_radio_config(radio)
        super(SensorNode, self).__init__(position)
    
    def _set_radio_config(self, radio_type):
        
        radio_params = self._get_radio_params(radio_type)
        for param in radio_params: 
            if param == "max_tx_power":
               self.max_tx_power = radio_params[param]
            elif param == "min_tx_power":
               self.min_tx_power = radio_params[param]
            elif param == "rx_sensitivity":
               self.rx_sensitivity = radio_params[param]
            elif param == "frequency":
               self.frequency = radio_params[param]
            else:
                raise ValueError("Radio parameter not expected: %s." %(param))
        
        #initialize radio with maximun tx_power                    
        self.tx_power = self.max_tx_power        

    def _get_radio_params(self, radio_type):
        radio_type = str(radio_type).upper()
        try:
            return RADIO_CONFIG[radio_type]
        except KeyError as e:
            raise ValueError("Radio %s is not supported." % radio_type) from e


    def set_txpower(self, tx_power):
        """
        Set radio transmission power
        
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
        """
        Get radio transmission power
        
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current configured transmission power
        """
        return self.tx_power

    def get_rxsensitivity(self):
        """
        Get radio receiver sensitivity
        
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current configured receiver sensitivity
        """
        return self.rx_sensitivity

    def get_frequency(self):
        """
        Get the radio frequency
        
        Parameters
        ----------
        No parameters
        
        Returns
        -------
        float number
            The current configured receiver sensitivity
        """
        return self.frequency

        
   


