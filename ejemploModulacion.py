# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fc = 1000 # frecuencia de la portadora
fm = 250 # frecuencia de la moduladora
m = 0.5# indice de la modulacion
t = 1  # duración de 1 segundo
pii = np.pi
sr = fc*10 # frecuencia de muestreo para construir el vector

# Construyo el vector tiempo
x = np.linspace(0, t, sr, dtype=np.float16 )

# Señales portadora y moduladora
signal_c = np.sin(2*pii*fc*x)# portadora
signal_m = np.cos(2*pii*fm*x)#moduladora

signal_y = (1+ m*signal_m) * signal_c# Señal AM

#y(t) = [1 + n*cos(2*pi*fm*t)]*A * sin(2*pi*fc*t)



#====================================================================================================================
# GRAFICOS
#====================================================================================================================

plt.figure()
plt.plot(x[0:300], signal_y[0:300])

plt.xlabel('tiempo(seg)')
plt.ylabel('amplitud')
plt.grid()
plt.show()