import numpy as np, matplotlib.pyplot as plt

# el programa esta simulando procesamiento de señales digitales
# y se aplica un filtro complementario para suavizar las ondas


# Frec 0 = 9000 Hz -> onda rapida
# Frec 1 = 5000 Hz -> media
# Frec 2 = 100 Hz -> lenta

FREQ_0 = 9000 ; FREQ_1 = 5000; FREQ_2 = 100  # Frecuencia 1, 2 y 3

# con el S_RATE tomamos 20000 muestras de cada onda, 
# 20000/9000 = 2.22 ciclos
# 20000/5000 = 4 ciclos
# 20000/100 = 200 ciclos

# y con el SAMPLE tomamos la duración de cada onda en segundos
SAMPLE = 20000 ; S_RATE = 20000.0 # Samples y Tasa de Muestreo
nMAX = 20000

# Ondas....
# tomamos la formula de sin(2*pi*frecuencia*tiempo)
# y lo multiplicamos por un valor cualquiera (2, 3, 9) para cambiar la amplitud

# i/S_RATE es el tiempo transcurrido 
#2*pi*frecuencia es la frecuencia angular, que es la velocidad a la que oscila la onda
# esto significa que la onda de 100hz tiene mayor amplitud 
aW = [
    [2*np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)],
    [3*np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)],
    [9*np.sin(2*np.pi * FREQ_2 * i/S_RATE) for i in range(SAMPLE)]
]

#Signals...
# creamos las señales, para la señal 1 se suma la onda 0 y la onda 1 (señal ruidosa)
# la señal 2 es la suma de la onda 0 y la onda 2 (mezcla de rápido y lento)
# la señal 3 es la multiplicacion de la onda 1 y la onda 2 (se distorsiona por completo)
aS = [
    np.array(aW[0]) + np.array(aW[1]),
    np.array(aW[0]) + np.array(aW[2]),
    np.array(aW[1]) * np.array(aW[2])
]

# es un filtro que pasa-bajos simple (suaviza la señal)
#y[i]=α⋅x[i]+(1−α)⋅y[i−1]
# el x[i] es la señal original
# el y[i] es la señal filtrada
# a(nA) es que tanto confiamos en el valor nuevo, si es mas cercano a 1 es menos suave y viceversa

def Filter_Comp(aV, nA):
    # Se agregó la inicialización del arreglo aF para evitar el NameError
    aF = np.zeros(nMAX) 
    aF[0] = aV[0]
    for i in range(1, nMAX):
        aF[i] = nA * aV[i] + (1.0 - nA) * aF[i-1]
    return aF

# Filtramos las 3 señales. Usamos nA=0.1 (suavizado fuerte) 
nA_val = 0.1 
aF_0 = Filter_Comp(aS[0], nA_val)
aF_1 = Filter_Comp(aS[1], nA_val)
aF_2 = Filter_Comp(aS[2], nA_val)

# Configuramos la gráfica, 3 gráficos (uno por señal)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), facecolor='lightgray')

#muestra exactamente el rango de 0 a 200 en el eje X
VIEW_LIMIT = 200

# Graficamos Signal 1
ax1.plot(aS[0][:VIEW_LIMIT], 'b-', linewidth=1) # Original azul
ax1.plot(aF_0[:VIEW_LIMIT], 'r-', linewidth=1)  # Filtrada roja
ax1.set_title('Signal 1')
ax1.set_xlim(0, 200)

# Graficamos Signal 2
ax2.plot(aS[1][:VIEW_LIMIT], 'b-', linewidth=1)
ax2.plot(aF_1[:VIEW_LIMIT], 'r-', linewidth=1)
ax2.set_title('Signal 2')
ax2.set_xlim(0, 200)

# Graficamos Signal 3
ax3.plot(aS[2][:VIEW_LIMIT], 'b-', linewidth=1)
ax3.plot(aF_2[:VIEW_LIMIT], 'r-', linewidth=1)
ax3.set_title('Signal 3')
ax3.set_xlim(0, 200)

# Ajustar espaciado y mostrar
plt.tight_layout()
plt.savefig('grafica_filtro_complementario.png', facecolor=fig.get_facecolor())
plt.show()


