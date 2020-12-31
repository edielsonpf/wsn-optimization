# coding: utf-8
#
# Copyright (C) 2020 wsn-toolkit
#
# This program was written by Edielson P. Frigieri <edielsonpf@gmail.com>

from wsntk.models import FreeSpace, LogDistance

import numpy as np
import matplotlib.pyplot as plt
import math

distance = [i for i in np.linspace(1,32,32)]

FS_link = FreeSpace()
LD_link = LogDistance()

frequency = 2.4e9
FS_loss_24 = []
LD_loss_24 = []
for d in distance:
	FS_loss_24.append(FS_link.loss(d, frequency))
	LD_loss_24.append(LD_link.loss(d, frequency))
	
frequency = 5.0e9
FS_loss_5 = []
LD_loss_5 = []
for d in distance:
	FS_loss_5.append(FS_link.loss(d, frequency))
	LD_loss_5.append(LD_link.loss(d, frequency))

print(FS_loss_24)
print(LD_loss_24)

fig, axs = plt.subplots(2, 1)

axs[0].plot(distance,FS_loss_24, color='b')
axs[0].plot(distance,FS_loss_5, color='r')
axs[0].set_xlabel('distance [m]')
axs[0].set_ylabel('Loss [dBm]')
axs[0].grid(True)
axs[0].semilogx(base=2)

axs[1].plot(distance,LD_loss_24, color='b')
axs[1].plot(distance,LD_loss_5, color='r')
axs[1].set_xlabel('distance [m]')
axs[1].set_ylabel('Loss [dBm]')
axs[1].grid(True)
axs[1].semilogx(base=2)


fig.tight_layout()
plt.show()
