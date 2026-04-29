import numpy as np, matplotlib.pyplot as plt

FREQ_0 = 9000 ; FREQ_1 = 5000; FREQ_2 = 100  # Frecuencia 1, 2 y 3
SAMPLE = 20000 ; S_RATE = 20000.0 # Samples y Tasa de Muestreo
nMAX = 20000

# Ondas....
aW = [
    [2*np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)],
    [3*np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)],
    [9*np.sin(2*np.pi * FREQ_2 * i/S_RATE) for i in range(SAMPLE)]
]

#Signals...
aS = [
    np.array(aW[0]) + np.array(aW[1]),
    np.array(aW[0]) + np.array(aW[2]),
    np.array(aW[1]) * np.array(aW[2])
]

def Filter_Comp(aV, nA):
    # Se agregó la inicialización del arreglo aF para evitar el NameError
    aF = np.zeros(nMAX) 
    aF[0] = aV[0]
    for i in range(1, nMAX):
        aF[i] = nA * aV[i] + (1.0 - nA) * aF[i-1]
    return aF

# Filtramos las 3 señales. Usamos nA=0.1 (suavizado fuerte) 
# para que la línea roja se vea como en la imagen de referencia.
nA_val = 0.1 
aF_0 = Filter_Comp(aS[0], nA_val)
aF_1 = Filter_Comp(aS[1], nA_val)
aF_2 = Filter_Comp(aS[2], nA_val)

# Configuramos la gráfica
# Ponemos fondo gris claro a la figura para imitar el estilo de la captura
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), facecolor='lightgray')

# La imagen 5 muestra exactamente el rango de 0 a 200 en el eje X
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


