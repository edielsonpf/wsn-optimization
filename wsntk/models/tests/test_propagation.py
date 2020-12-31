# Author: Edielson P. Frigieri <edielsonpf@gmail.com>
#
# License: MIT

import pytest
import numpy as np

from wsntk import models
from wsntk.models import FreeSpace, LogDistance

def test_free_space():
	# Test LogDistance link creation with default values.

	link = FreeSpace()

	loss = link.loss(distance = 2, frequency = 933e6)

	assert round(loss,2) == 37.87
	
	

def test_log_normal():
	# Test LogDistance link creation with different parameters.

	np.random.seed(0xffff)
	link = LogDistance(d0 = 1.0, sigma = 0.0, gamma = 2.0)

	loss = link.loss(distance = 2, frequency = 933e6)
	assert round(loss,2) ==  37.87
		
		
def test_log_normal_diffent_gamma():
	# Test LogDistance link creation with different parameters.

	np.random.seed(0xffff)
	link = LogDistance(d0 = 1.0, sigma = 0.0, gamma = 2.2)

	loss = link.loss(distance = 10, frequency = 933e6)
	assert round(loss,2) ==  53.85		