# Author: Edielson P. Frigieri <edielsonpf@gmail.com>
#
# License: MIT

import pytest

from wsntk import network
from wsntk.network import FreeSpaceRadioLink

def test_radio_link():
    # Test SensorNode creation with default values.
    
   src_position = (-10,10)
   dst_position = (10,-10)
   
   link = RadioLink(src_position, dst_position, threshold)

   assert round(link.get_link_distance(),2) == 28.28

   assert link.get_link_status() == 0
