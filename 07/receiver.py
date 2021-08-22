import socket

my_host='127.0.0.1'
my_port=50090

BUFSIZE=4096

r_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r_socket.bind((my_host, my_port))

r_socket.listen()
while True:
    print('listening...')
    soc, addr = r_socket.accept()
    msg = soc.recv(BUFSIZE)
    msg = msg.decode('utf-8')
    print('received: ' + msg)
    if msg == 'quit':
        break

r_socket.close()