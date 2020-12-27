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
        
          *nr_sensors*:
            Integer, the number of sensors.
          
          *dimensions*:
            Tuple of Integers, the x and y dimensions of the simulation area in kilometers.

          *loss function*
            String, the path loss function
          
          *sigma*
            Double, standard deviation applied to specific path loss models

          *gamma*
            Double, the path loss exponent

          *radio*
            String, the radio type usd on all sensors
    """

    link_models = {
        "FSPL": (FreeSpaceLink,),
        "LNPL": (LogNormalLink,),
    }

    def __init__(self, nr_sensors, dimensions, loss = "FSPL", sigma = 8.7, gamma = 2.2, radio = "DEFAULT"):
        
        self.nr_sensors = nr_sensors
        self.dimensions = dimensions
        self.radio = radio
        self.sigma = sigma
        self.gamma = gamma
        
        self.link = self._init_link(loss)
        self.sensors = self._init_sensors(nr_sensors, dimensions, radio)
            
    def _init_link(self, loss):
        """Get ``LinkClass`` object for str ``loss``. """
        try:
            link_ = self.link_models[loss]
            link_class, args = link_[0], link_[1:]
            if loss in ('LNPL'):
                args = (self.sigma, self.gamma)
            return link_class(*args)
        except KeyError as e:
            raise ValueError("The link loss %s is not supported. " % loss) from e


    def _init_sensors(self, nr_sensors, dimensions, radio):
        """Initializes the simulaiton creating all sensors with respective configuration. """                
        
        sensors = []
        #instantiate all sensors
        for i in range (nr_sensors):
            #instantiate a sensor
            sensor = SensorNode(dimensions, radio)
            #Add sensor to the network
            sensors.append(sensor)
        
        return sensors

    def _distance(self, pos_a, pos_b):
        """Calculate the euclidean distance between two positions"""
        return (math.sqrt(((pos_a[0]-pos_b[0])**2)+((pos_a[1]-pos_b[1])**2)))
    
    def __iter__(self):
        """Generator which returns the current links and sensors after update."""
        while True:
            sensors = self._update_sensors()
            links = self._update_links()
            yield sensors,links

    @abstractmethod
    def _update_sensors(self):
        """Update the sensors status: position, energy, etc."""
        raise NotImplementedError
    
    @abstractmethod
    def _update_links(self):
        """Update the links status based on the new sensors status."""
        raise NotImplementedError
       
    
class SensorNetwork(BaseNetwork):
    """
        Sensor network class.
        This class is implments a sensor network which involves elemts such as sensors and links.
        
        Required arguments:
        
          *nr_sensors*:
            Integer, the number of sensors.
          
          *dimensions*:
            Tuple of Integers, the x and y dimensions of the simulation area in kilometers.

          *loss function*
            String, the path loss function

          *sigma*
            Double, standard deviation applied to specific path loss models
          
          *gamma*
            Double, the path loss exponent

          *radio*
            String, the radio type usd on all sensors
    """
    def __init__(self, nr_sensors, dimensions, loss = "FSPL", sigma = 8.7, gamma = 2.2,  radio = "DEFAULT"):
        
        super(SensorNetwork, self).__init__(nr_sensors, dimensions, loss, sigma, gamma, radio)
    
    def _update_sensors(self):
        positions = np.empty((0, len(self.dimensions)))
        for sensor in self.sensors:
            position = next(iter(sensor))
            positions = np.append(positions, position.reshape(1,len(self.dimensions)), axis = 0)
            
        return positions
 
    def _link_status(self, rx_sensor, tx_sensor):
        
        if rx_sensor != tx_sensor:
            distance = self._distance(rx_sensor.get_position(), tx_sensor.get_position())
            loss = self.link.loss(distance, rx_sensor.frequency)
            rx_power = tx_sensor.tx_power - loss
            
            if(rx_power >= rx_sensor.rx_sensitivity):
                link_status = 1
            else:
                link_status = 0
        else:
            link_status = 0

        return link_status

    def _update_links(self):
        links = []
        for rx_sensor in self.sensors:
            aux_links = []
            for tx_sensor in self.sensors:
                    aux_links.append(self._link_status(rx_sensor, tx_sensor))
            links.append(aux_links)    
        
        return links
    
