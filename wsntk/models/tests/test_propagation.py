# Author: Edielson P. Frigieri <edielsonpf@gmail.com>
#
# License: MIT

import pytest
import numpy as np

from wsntk import models
from wsntk.models import FreeSpace, LogNormal

def test_free_space():
	# Test FreeSpace link creation with default values.

	link = FreeSpace()

	loss = link.loss(distance = 10, frequency = 933e6)

	assert round(loss,2) == 111.84
	
	

def test_log_normal():
	# Test FreeSpace link creation with default values.

	np.random.seed(0xffff)
	link = LogNormal(sigma = 8.7, gamma = 2.2)

	loss = link.loss(distance = 10, frequency = 933e6)
	assert round(loss,2) ==  128.46
		