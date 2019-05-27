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


## Filtro promediador
fil_promediador = np.array([1, 1])
signal_filtrada_p = sig.filtfilt(fil_promediador, 1, signal)
plt.figure( 6, (10,5) )
plt.plot( signal_filtrada_p[:50] )
plt.title( 'signal_filtrada (promediador)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [V]')
plt.show()

# Filtro diferenciador para detectar flancos
fil_diferenciador = np.array([-1, 1])
signal_filtrada_d = sig.filtfilt(fil_diferenciador, 1, signal)
plt.figure( 5, (10,5) )
plt.plot( signal_filtrada_d[:50] )
plt.title('signal_filtrada (diferenciador)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()



"""
tt  = np.linspace(0.0, (N-1)/fs, N).flatten()
ecg = ecg_lead[N1:N2]

frec = np.linspace(0.0, fs/2, N/2, endpoint=False)

plt.grid(which='both', axis='both')

# Respuesta en frecuencia
#                            b         , a)
ww, hh = sig.freqz(np.array([1, 0, -1]), 1)
#Normalizo el vector de frecuencias\n",
ww = ww / np.pi

# Respuesta de módulo
plt.figure(5)
plt.plot(ww, 20 * np.log10(abs(hh)), label='Modulo')
plt.title('FIR diferenciador')
plt.xlabel('Frequencia normalizada')
plt.ylabel('Modulo [dB]')
plt.grid(which='both', axis='both')
axes_hdl = plt.gca()
axes_hdl.legend()
plt.show()
"""
