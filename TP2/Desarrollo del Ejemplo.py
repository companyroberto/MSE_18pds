# -*- coding: utf-8 -*-


import numpy as np


"""
Resolución
Nota: En Filtrado.pdf (pag. 27) se expresa la forma de la matriz hermitica (AH) que se debe generar de acuerdo a un vector dado con las señales de entrada. La señal de entrada se denomina ‘u’ y tiene ‘n’ coeficientes. El objetivo es estimar cuál es el filtro que hace que los ‘n’ coeficientes de ‘u’ entreguen la mejor aproximación por un filtro lineal de nuestra señal deseada ‘d’ (que debemos conocer). Este filtro representa el caso general, filtro adaptativo, y en el TP1 vimos el filtro adaptado determinista que es un caso especial a partir de este. Cabe aclarar que este no es el filtro de winner porque para calcularlo necesito conocer la estadistica de la señal de entrada y la correlación cruzada con la señal deseada.

Por convenencia se define una matriz A hermitica que se arma con los N vectores de entrada que vamos teniendo en el primer vector que ya esta cargado en el filtro, que va desde el u(M) hasta el u(1). Cuando pasa un instante, tenemos el segundo vector columna con u(M+1) hasta u(2).. el último va desde u(N) hasta (N-M). La matriz A es su transpuesta.

Ejemplo: Para el vector u = [3, 2, 1, -1] Definiendo M = 2 (cantidad de taps del filtro)

La matriz correspondiente es la siguiente:

instante 1 instante 2
u2=2 u3=1
u1=3 u2=2

M establece la cantidad de filas de la matriz y la cantidad de columnas esta dada por: (Cantidad de muestras) - (cantidad de taps del filtro)

1) Encontrar la matriz de M por N de correlación los taps de entrada
"""
########################################################################################################################
u = [3, 2, 1, -1] # vector de ejemplo 
N = 4 # elementos del vector
M = 2 # cantidad de taps del filtro

matrizH = np.zeros((M, N-M))
for i in range(N-M):
    instante = u[i:M+i]
    matrizH[:,i] = instante[::-1]

#matrizH = matrizH.conjugate() # Al ser valores reales no hace falta conjugar los valores.
##matrizH

#La matriz A es directamente la traspuesta.
matriz = matrizH.transpose()  

##matriz


"""
2) El vector de correlación cruzada 𝑀 por 1 entre los taps de entrada del predictor y la respuesta deseada 𝑢(𝑖)
"""
########################################################################################################################
d = np.array([ 3, 2 ]) # vector deseado de ejemplo
dh = d.transpose() 

# Nota: Los vectores se crean del tipo columna y no funciona la operación transpuesta.
# Para transponer el vector columna y hacerlo fila se realiza de la siguiente forma: dh = np.reshape(d,(1,2))

#El vector z es la matriz hermítica por el vector de la respuesta deseada
z = matrizH @ d
##z


"""
3) El valor mínimo de 𝑒𝑓
"""
########################################################################################################################
#Existe un error de aproximación generado en la señal al analizarla y es blanco, afecta por igual, y es aditivo.

#El minimo error cuadratico medio entre la senial obtenida y la deseada esta determinado por la sig formula:
Emin = dh @ d  -  dh @ matriz @ ( np.linalg.inv(matrizH @ matriz) ) @ matrizH @ d
##Emin


"""
4) El vector de taps w
"""
########################################################################################################################
# El vector de taps esta determinado por la sig formula:
w = ( np.linalg.inv(matrizH @ matriz) ) @ ( matrizH @ d )
##w

# Aplicando el filtro sería:
filtrada = matriz @ w
##filtrada



