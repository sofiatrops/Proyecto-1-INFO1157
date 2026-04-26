import numpy as np
import matplotlib.pyplot as plt

# Parámetros base del proyecto [cite: 22, 23, 26, 28]
FREQ_0 = 1000      # Frecuencia principal (Hz)
FREQ_1 = 150       # Frecuencia de ruido (Hz)
S_RATE = 44100.0   # Tasa de muestreo (Samples/seg)
SAMPLE = 44100     # Total de muestras (1 segundo de audio)

# 1. Creación de las señales (Ondas Senoidales) [cite: 29, 30]
t = np.arange(SAMPLE) / S_RATE
s1 = np.sin(2 * np.pi * FREQ_0 * t)
s2 = np.sin(2 * np.pi * FREQ_1 * t)
w12 = s1 + s2  # Suma de ambas ondas [cite: 31]

# 2. Cálculo de la FFT utilizando Numpy [cite: 4, 82]
# Obtenemos la transformada y las frecuencias correspondientes
fft_result = np.fft.fft(w12)
fft_freq = np.fft.fftfreq(SAMPLE, 1/S_RATE)

# Solo nos interesa la mitad positiva del espectro (magnitud)
mag = np.abs(fft_result)

# 3. Visualización de resultados [cite: 5, 73]
plt.figure(figsize=(12, 8))

# Gráfica en el tiempo (Primeras 500 muestras para ver la forma)
plt.subplot(2, 1, 1)
plt.plot(t[:500], w12[:500])
plt.title("Señal Original + Ruido (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.grid(True)

# Gráfica en frecuencia (FFT)
plt.subplot(2, 1, 2)
plt.plot(fft_freq[:SAMPLE//2], mag[:SAMPLE//2]) # Solo frecuencias positivas
plt.title("Espectro de Frecuencia (FFT)")
plt.xlabel("Frecuencia [Hz]")
plt.xlim(0, 1500) # Zoom para ver los picos de 150 y 1000 Hz
plt.grid(True)

plt.tight_layout()
plt.show()