## Laboratorio #1: Arquitectura de Hardware (INFO1155)
Integrantes: Sofía Rodríguez & Paulo Villalobos

Fecha de Entrega: 30 de Abril, 2026 Profesor: Alberto Caro 


### 📋 Descripción del Proyecto
Este proyecto consiste en el desarrollo y análisis de procesamiento de señales digitales utilizando Python. El laboratorio abarca desde el análisis de frecuencias mediante la Transformada Rápida de Fourier (FFT) hasta la manipulación de archivos de audio binarios y el control de hardware/software mediante comunicación serial.

### 🛠️ Requisitos e Instalación
Para ejecutar los scripts de este repositorio, es necesario contar con un entorno de Python (recomendado 3.x) y las siguientes librerías:

```bash
pip install numpy matplotlib pywin32
```

Además, se requieren las siguientes herramientas externas:

* VSPE (Virtual Serial Ports Emulator): Para emular la comunicación serial.
* Audacity: Para la visualización y análisis de los archivos .wav generados.
* Winamp / AIMP: Reproductores multimedia para la prueba del protocolo de control.

### 📂 Estructura del Proyecto
#### 1. Transformada Rápida de Fourier (FFT) 

**Archivo:** Parte1_FFT.py

**Descripción:** Aplicación de la FFT mediante numpy para identificar frecuencias en señales con ruido.

**Objetivo:** Obtener las gráficas de la onda original, la onda ruidosa y el espectro de frecuencias resultante.

#### 2. Filtro Complementario 

**Archivo:** Parte2_Filtro.py

**Descripción:** Implementación de una función de filtrado para suavizar señales combinadas.

**Visualización:** Comparativa gráfica entre las señales originales (azul) y las señales filtradas (rojo).

#### 3. Control Serial de Media Player 

**Archivos:** cliente_serial.py y servidor_control.py

**Descripción:** Sistema de comunicación cliente-servidor vía puerto serial (VSPE).

**Funcionalidad:** El servidor utiliza User32.Keybd_event para simular presiones de teclas y controlar funciones como PLAY, STOP, y VOLUMEN en Winamp o AIMP.

#### 4. Generación de Audio Wave 

**Archivo:** Parte4_Audio.py

**Descripción:** Creación de archivos .wav desde cero utilizando los módulos wave y struct.

**Tareas Incluidas:**
* Generación de escalas musicales pentatónicas en diferentes tasas de muestreo (44.1kHz, 22.05kHz, 8kHz).
* Creación de ondas estereofónicas mediante fórmulas senoidales.
* Manipulación de volumen y limpieza de canales (izquierdo/derecho) vía software.

### 🚀 Cómo Ejecutar
Para señales: Ejecutar los scripts de la Parte 1 y 2 para generar las gráficas de Matplotlib.

Para el control multimedia: * Configurar un par de puertos virtuales en VSPE (ej. COM1-COM2).

* Ejecutar servidor_control.py.
* Ejecutar cliente_serial.py para enviar comandos.

Para audio: Ejecutar el script de la Parte 4 y abrir los archivos resultantes en Audacity para su verificación.

### 🧪 Resultados Esperados
Se espera que las gráficas de la FFT muestren picos claros en las frecuencias principales (Main y Ruido) y que el filtro complementario demuestre una reducción efectiva de las variaciones bruscas en la señal. Los archivos de audio deben reproducir las notas musicales correctamente según la tasa de muestreo configurada