# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Sensor nodes for wirelesss sensor networks simulation."""

from abc import ABCMeta, abstractmethod
from numpy.random import rand

RADIO_CONFIG = {"DEFAULT":          {"min_tx_power": -15.0, "max_tx_power": 27.0, "rx_sensitivity": -80.0, "frequency": 933e6},
                "ESP32-WROOM-32U":  {"min_tx_power": -12.0, "max_tx_power": 9.0, "rx_sensitivity": -97.0, "frequency": 2.4e9}}

class BaseNode(metaclass=ABCMeta):
    """Base class for sensor node."""
    
    def __init__(self, dimensions):
        
        self.dimensions = dimensions
        self._init_node()

    def _init_node(self):
        ndim = len(self.dimensions)
        self.position = rand(ndim) * self.dimensions

    def set_position(self, position):
        """
        Set node position
        
        Parameters
        ----------
        position : tuple of Double
           The x and y position of the sensor.
        
        Returns
        -------
        No data returned
        """
        ndim = len(self.dimensions)

        if(ndim != len(position)):
            raise ValueError("Position lenght different then expected. Expected %s, received %s." %(ndim, len(position)))    
        
        for index in range(ndim):
            if (position[index] > self.dimensions[index]):
                raise ValueError("Position exceeded dimensions limits.")
        
        self.position = position    
        
    def get_position(self):
        """
        Get node position
        
        Parameters
        ----------
        No parameters.
        
        Returns
        -------
        Tuple of Double
           The current x and y position of the sensor
        """
        return self.position

    def _update_position(self):
        """ Update the sensor position based on mobility models """
        #ndim = len(self.position)
        #step = 0.1*rand(ndim)
        #self.position = self.position + step
        pass

    @abstractmethod
    def __iter__(self):
        """Used to return an iteractor from a node"""
        raise NotImplementedError
    
    @abstractmethod
    def __next__(self):
        """Interator next"""
        raise NotImplementedError

class SensorNode(BaseNode):
    """
    Sensor node class.
        
    Required arguments:
        
        *dimensions*:
        Tuple of doubles, the area limits of the sensor.
          
        *radio*:
        Enumerator <RADIO_CONFIG>, the radio type to be used in the sensor.
    """
    def __init__(self, dimensions, radio = "DEFAULT"):
        
        super(SensorNode, self).__init__(dimensions)
        #initialize radio configuration
        self._set_radio_config(radio)
        
    def _set_radio_config(self, radio_type):
        """ Collect the radio parameters used in the sensor """

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
        """ Retrieve the radio parameters based on specified type """
        radio_type = str(radio_type).upper()
        try:
            return RADIO_CONFIG[radio_type]
        except KeyError as e:
            raise ValueError("Radio %s is not supported." % radio_type) from e

    def _update_energy(self):
        """ Update the sensor energy based on consumption models """
        pass
    
    def set_txpower(self, tx_power):
        """
        Set radio transmission power
        
        Parameters
        ----------
        tx_power : {double}
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
        double number
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
        double number
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
        double number
            The current configured receiver sensitivity
        """
        return self.frequency

    def __iter__(self):
        """Interator"""
        return self
    
    def __next__(self):
        self._update_position()
        self._update_energy()
        return self.position
           


