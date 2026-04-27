import time
import sys

try:
    import serial
except ImportError:
    print("ERROR: Este script requiere la librería 'pyserial'.")
    print("Para instalarla ejecuta: pip install pyserial")
    sys.exit(1)

def mostrar_menu():
    print("\n" + "="*30)
    print("   CONTROL REMOTO WINAMP/AIMP")
    print("="*30)
    print("1. PLAY / PAUSE")
    print("2. STOP")
    print("3. NEXT (Siguiente)")
    print("4. PREV (Anterior)")
    print("5. VOL+ (Subir Volumen)")
    print("6. VOL- (Bajar Volumen)")
    print("7. SALIR")
    print("="*30)

def iniciar_cliente(puerto_com, baudrate=9600):
    try:
        #se conecta al puerto virtual
        ser = serial.Serial(puerto_com, baudrate, timeout=1)
        print(f"Conectado exitosamente al puerto {puerto_com}.")
        
        while True:
            mostrar_menu()
            opcion = input("Selecciona un comando: ")
            
            #el b'' es de bytes
            comando = b''
            if opcion == '1':
                comando = b'PLAY\n'
            elif opcion == '2':
                comando = b'STOP\n'
            elif opcion == '3':
                comando = b'NEXT\n'
            elif opcion == '4':
                comando = b'PREV\n'
            elif opcion == '5':
                comando = b'VOL+\n'
            elif opcion == '6':
                comando = b'VOL-\n'
            elif opcion == '7':
                print("Saliendo del cliente...")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")
                continue
            
            #envia el comando por el puerto serial
            ser.write(comando)
            print(f"Comando enviado: {comando.decode('utf-8').strip()}")
            time.sleep(0.5) # Pequeño delay para no saturar
        
        
    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial {puerto_com}: {e}")
    except KeyboardInterrupt:
        print("\nCliente detenido por el usuario.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Puerto serial cerrado.")

if __name__ == "__main__":
    # Cambia 'COM1' por el puerto virtual configurado en VSPE para el cliente
    PUERTO = "COM1"
    iniciar_cliente(PUERTO)
