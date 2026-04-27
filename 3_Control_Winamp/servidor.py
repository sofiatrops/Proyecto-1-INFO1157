import time
import sys

# Se intenta importar librerías exclusivas de Windows
try:
    import serial
    import win32api
    import win32con
except ImportError:
    print("ERROR: Este script requiere las librerías 'pyserial' y 'pywin32' instaladas en un entorno Windows.")
    print("Para instalarlas ejecuta: pip install pyserial pywin32")
    sys.exit(1)

# Códigos Virtuales de Teclas Multimedia para Windows
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_STOP = 0xB2
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_VOLUME_UP = 0xAF
VK_VOLUME_DOWN = 0xAE


diccionario_comandos = {
    b'PLAY\n': VK_MEDIA_PLAY_PAUSE,
    b'PAUSE\n': VK_MEDIA_PLAY_PAUSE,
    b'STOP\n': VK_MEDIA_STOP,
    b'NEXT\n': VK_MEDIA_NEXT_TRACK,
    b'PREV\n': VK_MEDIA_PREV_TRACK,
    b'VOL+\n': VK_VOLUME_UP,
    b'VOL-\n': VK_VOLUME_DOWN
}

def simular_tecla(vk_code):
    # Simula presionar y soltar una tecla usando win32api
    # Presionar la tecla (keybd_event(bVk, bScan, dwFlags, dwExtraInfo))
    win32api.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.1) # Pequeño delay
    # Soltar la tecla (KEYEVENTF_KEYUP = 2)
    win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)

def iniciar_servidor(puerto_com, baudrate=9600):
    try:
        # Iniciamos la conexión serial
        ser = serial.Serial(puerto_com, baudrate, timeout=1)
        print(f"Servidor escuchando en {puerto_com} a {baudrate} baudios...")
        print("Esperando comandos del cliente...")
        
        while True:
            #si llega algo lo lee y se procesa
            if ser.in_waiting > 0:
                comando = ser.readline()
                print(f"Comando recibido: {comando.decode('utf-8').strip()}")
                
                #verifica que el comando existe
                if comando in diccionario_comandos:
                    #obtiene el codigo virtual de la tecla
                    vk_code = diccionario_comandos[comando]
                    #simula la pulsacion de la tecla
                    simular_tecla(vk_code)
                    print(f"--> Ejecutado: {comando.decode('utf-8').strip()}")
                else:
                    print(f"--> Comando no reconocido.")
                    
    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial {puerto_com}: {e}")
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Puerto serial cerrado.")

if __name__ == "__main__":
    # Cambia 'COM2' por el puerto virtual configurado en VSPE para el servidor
    PUERTO = "COM2"
    iniciar_servidor(PUERTO)
