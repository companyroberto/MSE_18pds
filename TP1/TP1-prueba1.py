# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:11:09 2019

@author: Roberto
"""

#Si quiero saber cuanto ruido, calcular la varianza (alterna de la señal).  Varianza = .var
#.Ventana deslizante, del 1 al 1024, luego 2 al 1025, luego del 3 al 1026…
#Se transmite una frecuencia de 1 y 0…
#La forma del pulso está en el sitio. Hay rebotes de la señal
#Lo importante no es reconstruir correctamente la señal, sino detectar los bit que se enviaron.
#La señal tiene más muestras que bits, hay que sub muestrar...
#Armar un filtro para eliminar el ruido. Analizar si es óptimo…
#Definir cuál es la línea que limita el 1 y 0. Analizar si es óptimo…
#El filtro óptimo maximiza la relacion señal ruido SNR y minimiza el error de bit.
#Entregarlo en un notebook de jupier
#Pulse es el archivo de muestra..
#Signal es la señal que recibimos con el ruido...


# Se dispone una trama digitalizada muestrada a 20 samples / pulso.
# Tomar una muestra de cada 20.
#un header de 16 bytes donde cada byte es: 10101100.


import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sc
from scipy import signal as sig


plt.close( 'all' )

pulse_1 = np.load('pulse.npy')
pulse_0 = pulse_1 * -1
signal = np.load('signal.npy')

# La señal original tiene 32560 muestras y como esta sobre muestrreada a 20 samples / pulso; existen 1628 pulsos
# La primer prueba consiste en tomar la primer muestra de cada 20.

N_vent      = 1628
signal_vent = [0.0]
signal_vent = np.pad(signal_vent, (0,N_vent-1), 'constant', constant_values=(0, 0))

x=0
y=0
for i in signal_vent:
    signal_vent[x] = signal[y]
    x = x + 1
    if y == 0:
        y = 19
    else:
        y = y + 20


plt.figure( 4, (10,5) )
plt.plot( signal_vent[:20] )
plt.title( 'signal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [V]')
plt.show()





