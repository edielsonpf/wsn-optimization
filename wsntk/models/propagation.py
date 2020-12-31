# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Path loss models."""

from abc import ABCMeta, abstractmethod
import numpy as np
import math

DEFAULT_C = 2.998e8
MIN_LOSS = 0

class BasePropagationModel(metaclass=ABCMeta):
	"""Base class for propagation loss models."""

	def __init__(self):
		pass
	
	def _friis_loss(self, distance, frequency):
		"""
		Calculate the path loss based on Friss propagation loss model.
				
		Formula:
				PL0 = 10*log10(Gr*Gt*((4*pi*d*f)/c)^2)
				
		Parameters
		----------
		distance : double
		   The distance (m).
		
		frequency: double
			The frequency of operation (Hz).  
		
		Returns
		-------
		double
			The Friss loss in decibels [dBm] evaluated for `distance` and `frequency`.
		"""
		Gr=1
		Gt=1
				
		return 10*math.log10(Gr*Gt*((4*math.pi*distance*frequency)/DEFAULT_C)**2) 
		
	@abstractmethod
	def loss(self, distance, frequency):
		"""Calculate the path loss."""
		raise NotImplementedError
		

class FreeSpace(BasePropagationModel):
	"""Class for Log-nomal propagation models."""

	def __init__(self):
		super(FreeSpace).__init__()
		
	def loss(self, distance, frequency):
		"""
		Calculate the link loss.
		For distance and frequency in meters and hertz, respectively. 
		
		Calculates the loss based on the free-space Friis equation
		
		Parameters
		----------
		distance : double
		   The distance between two nodes (m).
		
		frequency: double
			The frequency of operation (Hz).  
		
		Returns
		-------
		double
			The loss evaluated for `distance` and `frequency`.
		"""
		if distance > 0.01:
			L = self._friis_loss(distance, frequency)
		else:
			L = MIN_LOSS
			
		return L


class LogDistance(BasePropagationModel):
	"""Class for Log-nomal propagation models."""

	def __init__(self, d0 = 1.0, sigma = 0.0, gamma = 2.0):
		self.d0 = d0
		self.sigma = sigma
		self.gamma = gamma
		super(LogDistance).__init__()
		
	def loss(self, distance, frequency):
		"""
		Calculate the link loss.
		For distance and frequency in meters and hertz, respectively. 
		
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
		
		Formula:
				PL = PL0 + 10*gamma*log10(d/d0) + X_sigma
				
		Parameters
		----------
		distance : double
		   The distance between two nodes (m).
		
		frequency: double
			The frequency of operation (Hz).  
		
		Returns
		-------
		double
			The loss evaluated for `distance` and `frequency`.
		"""
		if distance > self.d0:
			L = self._friis_loss(self.d0, frequency) + self.gamma*10*math.log10(distance/self.d0) + np.random.normal(0, self.sigma)
		else:
			L = self._friis_loss(distance, frequency)
			
		return L
