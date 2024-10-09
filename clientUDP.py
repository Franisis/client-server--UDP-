from dotenv import load_dotenv
import socket
import os

load_dotenv()


# Creamos un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = os.getenv("HOST")
# Enviamos un mensaje al servidor
server_address = (HOST, 5000)  # Cambia '192.168.1.x' por la IP local del servidor
message = 'Mensaje desde el cliente'
sock.sendto(message.encode(), server_address)
 
# Esperamos la respuesta del servidor
print('Esperando respuesta del servidor...')
try:
    data, address = sock.recvfrom(4096)
except:
    print("??????")
print('Recibido {} bytes de la dirección {}'.format(len(data), address))
print(data.decode())
 
# Cerramos el socket
sock.close()
