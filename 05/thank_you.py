import socket

my_host='127.0.0.1'
my_port=50090
the_other_host='127.0.0.1'
the_other_port=50092

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((my_host, my_port))

my_socket.listen()
while True:
    soc, addr = my_socket.accept()
    content=soc.recv(4096)
    print(content)
    soc.sendall('thank you'.encode('utf-8'))
    soc.close()