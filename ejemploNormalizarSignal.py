# -*- coding: utf-8 -*-
from typing import Any, Union

import numpy as np
import matplotlib.pyplot as plt

# abrimos el archivo txt que contiene a la señal

# path = 'C:\Users\Juan Pablo\Downloads\workshop_UNTREF-master\Clase_02\notebooks' #'../..Clase_02/notebooks/'
# comento el path porque guardo el txt en la carpeta del proyecto
from numpy.core.multiarray import ndarray

signal = np.loadtxt('array.txt') # completar
# en caso de no comentar path usar : np.loadtxt(pth + archivo.txt)

# calculoamos el máximo y el mínimo de la señal
mini = min(signal)# a completar
maxi = max(signal)
print ('El máximo de la señal es: ', maxi) # completar
print('El minimo de la señal es:', mini ) # completar

signal_norm = signal/maxi # normalizo dividiendo por el máximo

# podemos ver como el maximo nos da 1 ahora
plt.plot(signal_norm)# completar
plt.show()

#################################################

# otra forma de normalización:

# primero convertimos a un formato mas conveniente
signal_int = signal.astype() # formato entero 16 bits con signo
signal_norm = # divido por el máximo valor posible del formato

# guardamos en un text
np.savetxt()