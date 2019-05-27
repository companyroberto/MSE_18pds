# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:11:09 2019

@author: Roberto
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sc
from scipy import signal as sig


plt.close( 'all' )


pulse_1 = np.load('pulse.npy')
pulse_0 = pulse_1 * -1
signal = np.load('signal.npy')
#signal = np.load('signalLowSNR.npy')


N_vent      = 1628
signal_vent = [0.0]
signal_vent = np.pad(signal_vent, (0,N_vent-1), 'constant', constant_values=(0, 0))


promedio = 0.0
x=0
y=0
p=19
p_vent = 0
for i in signal_vent:
    promedio = promedio + signal[y]    
    if y == p:
        signal_vent[x] = promedio / 20
        promedio = 0.0
        p_vent= 0
        x = x + 1
        p = p + 20

    y = y + 1
    p_vent = p_vent + 1

media = signal_vent.mean()
print("Media de la señal: " + str(media))

for muestra in signal_vent[:100]:
    if (muestra > media):
        print('1')
    else:
        print('0')

plt.figure( 4, (10,5) )
plt.plot( signal_vent[:40] )
plt.title( 'signal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [V]')
plt.show()
