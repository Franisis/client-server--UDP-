from dotenv import load_dotenv
import socket
import os
import time

load_dotenv()


# Creamos un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = os.getenv("HOST")
# Enviamos un mensaje al servidor
server_address = (HOST, 5000)  # Cambia '192.168.1.x' por la IP local del servidor
message = 'Mensaje desde el cliente'
sock.sendto(message.encode(), server_address)
 
# Esperamos la respuesta del servidor

while True:
    print('Esperando respuesta del servidor...')
    try:
        data, address = sock.recvfrom(4096)
        print('Recibido {} bytes de la dirección {}'.format(len(data), address))
        print(data.decode())
    except:
        print("??????")
    print('Comienza a esperar 60 segundos antes de enviar el siguiente mensaje')
    time.sleep(5) #duerme 60 segundos

 
# Cerramos el socket
sock.close()
