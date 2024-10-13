from dotenv import load_dotenv
import socket
import os

load_dotenv()

HOST = os.getenv("HOST")
# Creamos un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(HOST)

# Enlazamos el socket a la IP de la red local y puerto
server_address = (HOST, 5000)  # Cambia '192.168.1.x' por la IP local del servidor
sock.bind(server_address)

# Escuchamos las peticiones entrantes
while True:
    print('Esperando a recibir un mensaje...')
    data, address = sock.recvfrom(4096)

    print('Recibido {} bytes de la dirección {}'.format(len(data), address))
    print(data.decode())

    # Enviamos una respuesta al cliente
    message = 'Respuesta desde el servidor'
    sock.sendto(message.encode(), address)
