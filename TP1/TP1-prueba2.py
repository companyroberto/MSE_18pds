# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:11:09 2019

@author: Roberto
"""

#Si quiero saber cuanto ruido, calcular la varianza (alterna de la señal).  Varianza = .var
#.Ventana deslizante, del 1 al 1024, luego 2 al 1025, luego del 3 al 1026… No lo hice así ¿esta bien que cada 20 es un pulso?
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
#signal = np.load('signalLowSNR.npy')

#signal = np.sqrt(signal)

#plt.figure( 1, (10,5) )
#plt.plot( pulse_1 )
#plt.title( 'pulse_1')
#plt.xlabel('Muestras')
#plt.ylabel('Amplitud [V]')
#plt.show()
#
#plt.figure( 2, (10,5) )
#plt.plot( pulse_0 )
#plt.title( 'pulse_0')
#plt.xlabel('Muestras')
#plt.ylabel('Amplitud [V]')
#plt.show()


#N_p1 = len(pulse_1)
#spectrum_p1 = np.abs(sc.fft(pulse_1))
#spectrum_p1 = (1/max(spectrum_p1)) * spectrum_p1     #Amplitud Normalizada\n",
#half_p1 = spectrum_p1[:N_p1//2]
#
#plt.figure( 3, (10,5) )
#plt.stem( half_p1 )
#plt.title( 'half_p1')
#plt.xlabel('Frecuencia [Hz]')
#plt.ylabel('Amplitud [V]')
#plt.show()


# La señal original tiene 32560 muestras y como esta sobre muestreada a 20 samples / pulso; existen 1628 pulsos
# La primer prueba consiste en tomar la primer muestra de cada 20 y aplicar filtro diferenciador.
# La segunda es hacer el promedio de las 20 muestras y registrar en ventana.

#N_vent      = 1024
#signal_vent = signal[:N_vent]


N_vent      = 1628
signal_vent = [0.0]
signal_vent = np.pad(signal_vent, (0,N_vent-1), 'constant', constant_values=(0, 0))

N_pulse_vent = 20
pulse_vent   = [0.0]
pulse_vent   = np.pad(pulse_vent, (0,N_pulse_vent-1), 'constant', constant_values=(0, 0))

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

print('signal.var() = ' + str( signal.var() ))
print('signal_vent.var() = ' + str( signal_vent.var() ))
    

plt.figure( 4, (10,5) )
plt.plot( signal_vent[:40] )
plt.title( 'signal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud [V]')
plt.show()


#plt.figure( 5, (10,5) )
#plt.plot( pulse_vent )
#plt.title( 'pulse_vent')
#plt.xlabel('Muestras')
#plt.ylabel('Amplitud [V]')
#plt.show()
#
##pulse_vent = pulse_vent - pulse_1
### Filtro promediador
#fil_promediador = np.array([1, 1])
#signal_filtrada = sig.filtfilt(fil_promediador, 1, pulse_vent)
#plt.figure( 6, (10,5) )
#plt.plot( signal_filtrada )
#plt.title( 'signal_filtrada')
#plt.xlabel('Muestras')
#plt.ylabel('Amplitud [V]')
#plt.show()

## Filtro diferenciador para detectar flancos
#fil_diferenciador = np.array([-1, 1])
#signal_filtrada = sig.filtfilt(fil_diferenciador, 1, signal_vent)
#plt.figure( 5, (10,5) )
#plt.plot( signal_filtrada )
#plt.title('signal_filtrada')
#plt.xlabel('Muestras')
#plt.ylabel('Amplitud')
#plt.show()



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
