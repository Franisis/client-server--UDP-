import socket
 
# Creamos un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
# Enviamos un mensaje al servidor
server_address = ('locaLhost', 5000)  # Cambia '192.168.1.x' por la IP local del servidor
message = 'Mensaje desde el cliente'
sock.sendto(message.encode(), server_address)
 
# Esperamos la respuesta del servidor
print('Esperando respuesta del servidor...')
data, address = sock.recvfrom(4096)
print('Recibido {} bytes de la dirección {}'.format(len(data), address))
print(data.decode())
 
# Cerramos el socket
sock.close()
