import wave #funciones para crear el archivo .wav
import math #funciones matematicas como el seno
import struct #para convertir los datos en bytes
import os #para manejar el directorio de salida

os.makedirs("ondas_generadas", exist_ok=True)

escalas = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

nombres_escalas = ["do", "re", "mi", "fa", "sol", "la", "si"]

escala_en_reversa = escalas[::-1]

def generar_escala(nombre, frecuencia, framerate, canales):
    print(f"Generando onda para {nombre} a {frecuencia} Hz")

    with wave.open(nombre, "w") as wav_file:
        
        # usamos el setnchannels para definir cuantos canales de audio tendtrá el archivo
        wav_file.setnchannels(canales) #numero de canales (1= mono: es un solo canal, 2= stereo: son dos canales)
     
        #usamos el setsampwidth para definir el tamaño de cada muestra de audio en bytes(resolución de audio)
        wav_file.setsampwidth(2) #tamaño de cada muestra (2 bytes = 16 bits) 16 bits es la calidad estandar
        #esto significa que cada muestra ocupa 16 bits, con valores entre -32768 y 32767
        #esto permite capturar mas detalles en la onda de audio

        #usamos el setframerate para definir la frecuencia de muestreo
        wav_file.setframerate(framerate) #frecuencia de muestreo (44100Hz = calidad cd)
        #esto significa que se toman 44100 muestras por segundo

        # recorremos cada frecuencia (escala musical)
        for freq in frecuencia:            
            #por cada frecuencia generamos 1 segundo de audio
            for i in range(framerate * 1): 

                #formula que genera una onda senosoidal, el 'freq' es la frecuencia (que tan agudo es el sonido)
                #el 'i' es el tiempo transcurrido
                #el framerate es el numero de muestras por segundo
                valor = int(32767.0 * math.sin(2.0 * math.pi * freq * i / framerate))

                if canales == 1:
                    # el '<h' es el numero entero de 16 bits 
                    wav_file.writeframes(struct.pack('<h', valor))
                else:
                    # el '<hh' son los dos enteros 16 bits (stereo) izquierdo y derecho
                    wav_file.writeframes(struct.pack('<hh', valor, valor))

# 1 MONO 44.100 
generar_escala("ondas_generadas/escala_mono_44100.wav", escalas, 44100, 1)

# 2 STEREO 22.050 
generar_escala("ondas_generadas/escala_stereo_22050.wav", escala_en_reversa, 22050, 2)
            
# 3 MONO 8000
generar_escala("ondas_generadas/escala_mono_8000.wav", escalas, 8000, 1)

#4 Onda stereo

def onda_stereo(nombre_archivo):
    sample_rate = 44100 
    with wave.open(nombre_archivo, "w") as wav_file:
        wav_file.setnchannels(2) #STEREO
        wav_file.setsampwidth(2)# 2 bytes = 16 bits
        wav_file.setframerate(sample_rate) #frecuencia

        for i in range(sample_rate * 10): #la duracion del audio es de 10 segundos
            y = int(8000 * math.sin(2* math.pi * 500.0 * i / sample_rate) + #como son dos ondas senosoidales se suman
                    8000 * math.sin(2* math.pi * 250.0 * i / sample_rate))
            wav_file.writeframes(struct.pack('<hh', y, y))

onda_stereo("ondas_generadas/onda_stereo.wav")

#5 Baje el volumen de la onda anterior en un 75% utilizando Python.

def bajar_volumen(archivo_salida, archivo_entrada):

    with wave.open(archivo_entrada, "r") as wav_file_entrada:
        #investigar
        parametros = wav_file_entrada.getparams() #es un objeto con toda la metadata del archivo

        with wave.open(archivo_salida, "w") as wav_file_salida:
            wav_file_salida.setparams(parametros) #usamos los mismos parametros de la onda original (Stereo 44100hz)
            frames = wav_file_entrada.readframes(wav_file_entrada.getnframes()) #obtenemos todos los frames (muestras)
        #16 bit = 2 bytes
            for i in range(0, len(frames), 4):

                izquierda, derecha = struct.unpack('<hh', frames[i:i+4]) #desempaqueta los dos valores
        
                #reduciendo el volumen a 75%
                izquierda = int(izquierda * 0.25)
                derecha = int(derecha * 0.25)

                wav_file_salida.writeframes(struct.pack('<hh', izquierda, derecha))

bajar_volumen("ondas_generadas/onda_stereo_baja.wav", "ondas_generadas/onda_stereo.wav")

# 6. Limpie el canal izquierdo de la señal anterior con Python y reproduzca con Audacity.

def limpiar_canal_izq(archivo_entrada, archivo_salida):
    with wave.open(archivo_entrada, "r") as wav_file_entrada:
        parametros = wav_file_entrada.getparams()
        with wave.open(archivo_salida, "w") as wav_file_salida:
            wav_file_salida.setparams(parametros)

            frames = wav_file_entrada.readframes(wav_file_entrada.getnframes())

            for i in range(0, len(frames), 4):
                izquierda, derecha = struct.unpack('<hh', frames[i:i+4])
                izquierda = 0
                wav_file_salida.writeframes(struct.pack('<hh', izquierda, derecha))

limpiar_canal_izq("ondas_generadas/onda_stereo_baja.wav", "ondas_generadas/onda_stereo_limpia.wav")

            
#TERMINADAAAA!!!!

        





        


            

        


