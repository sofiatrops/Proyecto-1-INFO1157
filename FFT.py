import numpy as np
import matplotlib.pyplot as plt

FREQ_PRINCIPAL = 1000
FREQ_RUIDO = 50
SAMPLE = 44100  # Numero de muestras (cuántos datos tenemos en total)
S_RATE = 44100.0  # Muestras por segundo (frecuencia de muestreo). Es el tamano EN TIEMPO de las muestras.

# VALORES/DATOS en cada instante de tiempo para cada onda
valoresOndaPrincipal = [np.sin(2 * np.pi * FREQ_PRINCIPAL * i / SAMPLE) for i in range(SAMPLE)] 
    # Señal senoidal de 1000 Hz (la onda completa se repite 1000 veces por segundo)
valoresOndaRuido = [np.sin(2 * np.pi * FREQ_RUIDO * i / SAMPLE) for i in range(SAMPLE)] 
    # Señal senoidal de 50 Hz (la onda completa se repite 50 veces por segundo)

# Los arrays de NumPy almacenan datos de un solo tipo (homogéneos)
# lo que permite mayor eficiencia en memoria y cálculos numéricos vectorizados.

# Guardamos los valores de cada onda en arrays para poder operar con ellos. Ya que numpy trabaja con arrays, no con listas.
arrayPrincipal = np.array(valoresOndaPrincipal)
arrayRuido = np.array(valoresOndaRuido)

# Superposición de señales: mezcla de la onda principal y el ruido
sumaFREQ = arrayPrincipal + arrayRuido

# Aqui se genera un ARRAY de tiempo que corresponde a cada muestra de la señal combinada. 
t = np.arange(len(sumaFREQ)) / S_RATE
    # El tiempo se calcula dividiendo el índice de cada muestra por la frecuencia de muestreo (S_RATE), 
    # lo que da el tiempo en segundos para cada muestra.
    # NO DA EL TIEMPO TOTAL, DA EL TIEMPO DE CADA MUESTRA.


# FFT
    # Hasta ahora solo teniamos los datos de la señal combinada en el dominio del tiempo. 
    # La FFT nos permite transformar esa señal al dominio de la frecuencia.
    # Lo que nos muestra qué frecuencias (Cada cuanto se repite la Onda) están presentes en la señal y con qué intensidad 

fft_valores = np.abs(np.fft.fft(sumaFREQ))
    # abs devuelve el valor absoluto de cada componente de la FFT, nos quedamos solo con la MAGNITUD de cada componente.
    # Intensidad = (Amplitud "Punto maximo y minimo").
freqs = np.fft.fftfreq(len(sumaFREQ), 1/S_RATE)
    # Lista de frequencias dentro del array sumaFREQ. 

# Con ambos podemos ver que frecuencias están presentes en la señal combinada y con qué intensidad.

# FIGURA
plt.figure(figsize=(10,8))

# 1) Señal original (solo un pedazo)
plt.subplot(4,1,1)
plt.plot(t[:1000], arrayPrincipal[:1000])
plt.title("Onda Original (1000 Hz)")

# 2) Ruido
plt.subplot(4,1,2)
plt.plot(t[:1000], arrayRuido[:1000])
plt.title("Ruido (50 Hz)")

# 3) Señal combinada
plt.subplot(4,1,3)
plt.plot(t[:1000], sumaFREQ[:1000])
plt.title("Señal combinada")

# 4) FFT
plt.subplot(4,1,4)
plt.plot(freqs, fft_valores)
plt.xlim(0, 2000)
plt.title("FFT")

plt.tight_layout()
plt.show()