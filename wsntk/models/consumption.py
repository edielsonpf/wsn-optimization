# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

"""Path loss models."""

from abc import ABCMeta, abstractmethod
import numpy as np
import math

class BaseConsumptionModel(metaclass=ABCMeta):
	"""Base class for propagation loss models."""

	def __init__(self):
		pass
	
	@abstractmethod
	def consumption(self, tx_power):
		"""Calculate the consumption based on the consumption model."""
		raise NotImplementedError
		

class NoConsumption(BaseConsumptionModel):
	"""Class for no consumption models."""

	def __init__(self):
		super(NoConsumption).__init__()
		
	def consumption(self, tx_power):
		"""
		Implements a model without consumption, which always returns 0 
		
		Parameters
		----------
		current_level : double
		   The normalized battery level 0 to 100.
		
		tx_power: double
			The transmission power in dBm.  
		
		Returns
		-------
		double
			The consumption for `tx_power` in units of normalized battery level.
		"""
			
		return 0

class ConstantConsumption(BaseConsumptionModel):
	"""Class for contant consumption models."""

	def __init__(self, scaling = 1.0):
		
		self.scaling = scaling
		super(ConstantConsumption).__init__()
		
	def consumption(self, tx_power):
		"""
		Implements a model with a consumption proportional to a hardware-dependent and battery-dependent constant. 
		
		Parameters
		----------
		current_level : double
		   The normalized battery level 0 to 100.
		
		tx_power: double
			The transmission power in dBm.  
		
		Returns
		-------
		double
			The consumption for `tx_power`.
		"""
		
		#converts the power from dBm to watts
		Ptx_w = 10**(tx_power/10)*0.001	
		return self.scaling*Ptx_w