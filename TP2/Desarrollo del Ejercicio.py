# -*- coding: utf-8 -*-


import numpy as np


"""
5) Calcular el filtro para 𝑁 valores de una realización de la señal 𝑢(𝑖)=𝑠𝑒𝑛(2𝜋𝜔0𝑖+𝜙0)+0.02𝑛(𝑖)
   siendo 𝜔0=3, 𝜙0=𝜋/4 y 𝑛(𝑖) un ruido gaussiano de varianza unitaria. Tomar N = 100 y M = 4.
"""
########################################################################################################################
# 𝑢(𝑖) = 𝑠𝑒𝑛 ( 2 * 𝜋 * w0 * i + p0 ) + 0.02 n(i)
# siendo: w0 = 3, p0 = pi / 4 y n(i) gaussiano. N = 100, M = 4

w0 = 3
p0 = np.pi / 4
n1 = 100
M  = 4
i  = np.linspace(0.0, (n1-1)/n1, n1, endpoint=False)
u  = np.sin( 2 * np.pi * w0 * i + p0 )

import matplotlib.pyplot as plt

plt.figure( 1, (10,5) )
plt.title( 'Señal original')
plt.grid(which='both', axis='both')
plt.plot( i, u, color='b' )
plt.show()

np.random.seed(42) # Utilizo semilla para generar siempre el mismo ruido
ruido = np.random.normal(0, 0.02, n1) #Draw random samples from a normal (Gaussian) distribution.

signal = u + ruido

plt.figure( 2, (10,5) )
plt.title( 'Señal con ruido')
plt.grid(which='both', axis='both')
plt.plot( i, signal, color='r' )
plt.show()

########################################################################################################################
# Crear la matriz de M por N de correlación los taps de entrada

u_ori = u
u = signal # vector de la señal
N = u.size # elementos del vector
M = 4      # cantidad de taps del filtro

matrizH = np.zeros((M, N-M))
for x in range(N-M):
    instante = u[x:M+x]
    matrizH[:,x] = instante[::-1]

##matrizH
########################################################################################################################
#La matriz A es directamente la traspuesta.
matriz = matrizH.transpose()  

##matriz
########################################################################################################################
# El vector de correlación cruzada 𝑀 por 1 entre los taps de entrada del predictor y la respuesta deseada 𝑢(𝑖)

# Para generar el vector de la respuesta deseada puedo usar la señal sin ruido generada antes:
d = u_ori[:M]     # Tomo los m primeros taps de la señal original
d = u_ori[M-1:-1] # Tomo los últimos M-1 taps de la señal original

dh = d.transpose()

#El vector z es la matriz hermítica por el vector de la respuesta deseada
z = matrizH @ d

##z
########################################################################################################################
#Existe un error de aproximación generado en la señal al analizarla y es blanco, afecta por igual, y es aditivo.
#El minimo error cuadratico medio entre la senial obtenida y la deseada esta determinado por la sig formula:

Emin = dh @ d  -  dh @ matriz @ ( np.linalg.inv(matrizH @ matriz) ) @ matrizH @ d

##Emin
########################################################################################################################
# El vector de taps esta determinado por la sig formula:
w = ( np.linalg.inv(matrizH @ matriz) ) @ ( matrizH @ d )

# Aplicando el filtro sería:
filtrada = matriz @ w
##filtrada

plt.figure( 3, (10,5) )
plt.title( 'Señal filtrada')
plt.grid(which='both', axis='both')
plt.plot( i[M:], filtrada, color='r' )
plt.show()
