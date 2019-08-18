# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt



w0 = 3
p0 = np.pi / 4
n1 = 100
M  = 4
i  = np.linspace(0.0, (n1-1)/n1, n1, endpoint=False)
u  = np.sin( 2 * np.pi * w0 * i + p0 )

plt.figure( 1, (10,5) )
plt.title( 'Señal original')
plt.grid(which='both', axis='both')
plt.plot( i, u, color='b' )
plt.show()

# Aumentando el nivel de ruido y la cantidad de taps a la señal.

np.random.seed(42) # Utilizo semilla para generar siempre el mismo ruido
ruido = np.random.normal(0, 0.1, n1)
signal = u + ruido

plt.figure( 2, (10,5) )
plt.title( 'Señal con ruido')
plt.grid(which='both', axis='both')
plt.plot( i, signal, color='r' )
plt.show()

u_ori = u
u = signal # vector de la señal
N = u.size # elementos del vector
M = 10     # cantidad de taps del filtro

# Crear la matriz hermitica de M por N de correlación los taps de entrada
matrizH = np.zeros((M, N-M))
for x in range(N-M):
    instante = u[x:M+x]
    matrizH[:,x] = instante[::-1]

#La matriz A es directamente la traspuesta.
matriz = matrizH.transpose()  

# El vector de correlación cruzada 𝑀 por 1 entre los taps de entrada del predictor y la respuesta deseada 𝑢(𝑖)
d = u_ori[M-1:-1] # Tomo los últimos M-1 taps de la señal original
dh = d.transpose()

#El vector z es la matriz hermítica por el vector de la respuesta deseada
z = matrizH @ d

#Calcular el minimo error cuadratico medio entre la senial obtenida y la deseada
Emin = dh @ d  -  dh @ matriz @ ( np.linalg.inv(matrizH @ matriz) ) @ matrizH @ d

# El vector de taps esta determinado por la sig formula:
w = ( np.linalg.inv(matrizH @ matriz) ) @ ( matrizH @ d )

# Aplicando el filtro sería:
filtrada = matriz @ w

plt.figure( 3, (10,5) )
plt.title( 'Señal filtrada')
plt.grid(which='both', axis='both')
plt.plot( i[M:], filtrada, color='r' )
plt.show()