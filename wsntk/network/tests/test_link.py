# Author: Edielson P. Frigieri <edielsonpf@gmail.com>
#
# License: MIT

import pytest
import numpy as np

from wsntk import network
from wsntk.network import FreeSpaceLink, LogNormalLink

def test_free_space_link():
    # Test FreeSpace link creation with default values.
    
    link = FreeSpaceLink()
    
    assert link.loss(distance = 10, frequency = 933e6) == 111.83763287493002
    
def test_log_normal_link():
    # Test FreeSpace link creation with default values.
    np.random.seed(0xffff)

    link = LogNormalLink(sigma = 8.7, gamma = 2.2)
    
    assert link.loss(distance = 10, frequency = 933e6) ==  128.46425705711366